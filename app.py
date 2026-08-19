# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Репетитор", layout="wide")

# --- 1. Подключение к Google Таблицам ---
# Эта строка создает "мост" между твоим приложением и Таблицами.
# Все секреты подхватятся автоматически из secrets.toml.
conn = st.connection("gsheets", type=GSheetsConnection)

# --- 2. Загрузка данных (с кешированием) ---
@st.cache_data(ttl=600) # Кешируем на 10 минут, чтобы не дёргать API каждую секунду
def load_data(sheet_name):
    # Если нужно читать разные листы в одной таблице
    return conn.read(worksheet=sheet_name, ttl=600)

# Загружаем данные из разных листов твоей Google Таблицы
# Названия листов должны соответствовать тем, что в твоем файле
df_schedule = load_data("Расписание") # Например, лист с расписанием
df_students = load_data("Ученики")    # Лист с данными учеников
df_reviews = load_data("Отзывы")      # Лист с отзывами

# --- 3. Навигация (Боковое меню) ---
st.sidebar.title("📚 Навигация")
page = st.sidebar.radio("Перейти на страницу:", 
                        ["Главная", "Образование", "Опыт", "Отзывы", "Личный кабинет"])

# --- 4. Страница "Главная" ---
if page == "Главная":
    st.title("Привет! Я [Твое Имя], репетитор по [Предмету]")
    st.write("Здесь будет твоя основная информация: чем ты занимаешься, как проходят уроки и т.д.")

# --- 5. Страница "Образование" и "Опыт" ---
elif page == "Образование":
    st.header("🎓 Мое образование")
    # Текст с твоим образованием

elif page == "Опыт":
    st.header("💼 Опыт работы")
    # Текст с твоим опытом

# --- 6. Страница "Отзывы" ---
elif page == "Отзывы":
    st.header("⭐ Отзывы моих учеников")
    if not df_reviews.empty:
        for _, row in df_reviews.iterrows():
            st.write(f"**{row['Имя']}**: {row['Отзыв']} ★ {row['Оценка']}")
    else:
        st.write("Пока нет отзывов.")

# --- 7. Страница "Личный кабинет" ---
elif page == "Личный кабинет":
    st.header("🔐 Личный кабинет")
    
    # --- Простая аутентификация (пока что) ---
    # В будущем ты сможешь сделать вход по логину и паролю из твоей Google Таблицы
    # Например, использовать библиотеку streamlit-authenticator-sheets [citation:2]
    
    # Допустим, для примера, пользователь ввел свое имя
    student_name = st.text_input("Введи свое имя для входа (демо-режим)")
    
    if student_name:
        st.subheader(f"Здравствуй, {student_name}!")
        
        # Фильтруем расписание для этого ученика
        user_schedule = df_schedule[df_schedule['Ученик'] == student_name]
        
        if not user_schedule.empty:
            st.write("### 📅 Твои занятия")
            for _, lesson in user_schedule.iterrows():
                status = "✅ Состоялось" if lesson['Состоялось'] == "Да" else "⏳ Запланировано"
                st.write(f"**{lesson['Дата']}** - {status}")
                
                # Блок с материалами к занятию
                if lesson['Состоялось'] == "Да":
                    with st.expander("📎 Материалы занятия"):
                        st.write(f"🔗 Ссылка на встречу: {lesson['Ссылка']}")
                        st.write(f"📄 Домашнее задание: {lesson['ДЗ']}")
                        st.write(f"📝 Конспект урока: {lesson['Конспект']}")
        else:
            st.write("У тебя нет запланированных занятий.")

        # --- Трекер оплат ---
        st.write("### 💰 Трекер оплат")
        # Здесь ты тоже можешь загрузить данные по оплатам из другого листа
        # и показать их, например, в виде таблицы.
