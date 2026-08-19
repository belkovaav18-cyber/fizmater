# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Репетитор по физике", layout="wide")

# --- 1. Подключение к Google Таблицам ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- 2. Загрузка данных (с кешированием) ---
@st.cache_data(ttl=600)
def load_data(sheet_name):
    return conn.read(worksheet=sheet_name, ttl=600)

# Загружаем данные
df_schedule = load_data("Schedule")
df_students = load_data("Students")
df_reviews = load_data("Reviews")

# --- 3. Навигация ---
st.sidebar.title("📚 Навигация")
page = st.sidebar.radio("Перейти на страницу:", 
                        ["Главная", "Образование", "Опыт", "Отзывы", "Личный кабинет"])

# --- 4. Страница "Главная" ---
if page == "Главная":
    st.title("👋 Привет! Я Александра")
    st.subheader("Репетитор по физике с восьмилетним стажем")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.write("""
        ### 📖 Обо мне
        Я помогаю ученикам понять физику и полюбить этот предмет. 
        Мои ученики успешно сдают ОГЭ, ЕГЭ и поступают в ведущие вузы страны.
        
        **Что вы получите на моих занятиях:**
        - Индивидуальный подход
        - Понятное объяснение сложных тем
        - Подготовку к экзаменам
        - Домашние задания с проверкой
        """)
    with col2:
        st.info("""
        **📅 Запись на занятия**
        
        Свяжитесь со мной:
        - ✉️ alexandra@email.com
        - 📱 +7 (XXX) XXX-XX-XX
        - 📍 Москва (онлайн)
        """)

# --- 5. Страница "Образование" ---
elif page == "Образование":
    st.header("🎓 Мое образование")
    
    # Текущее обучение в аспирантуре (самое важное - вверху)
    st.subheader("📌 Сейчас я здесь:")
    
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            **🏛️ Федеральное государственное бюджетное образовательное учреждение высшего образования 
            «Московский государственный университет имени М.В.Ломоносова»**
            
            **Направление:** Оптика  
            **Уровень образования:** Высшее - аспирантура (очная форма)  
            **Курс:** 2  
            **Дата зачисления:** 01.10.2024  
            **Номер приказа:** 3411ас от 15.07.2024
            """)
        with col2:
            st.success("🎯 **Аспирантура**\n\n*2024 - н.в.*")
    
    st.divider()
    
    # Магистратура (2022-2024)
    st.subheader("🎓 Магистратура")
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            **🏛️ Московский государственный университет имени М.В.Ломоносова**
            
            **Направление:** ФИЗИКА  
            **Программа:** ФИЗИКА. ВОЛНЫ В СТРУКТУРИРОВАННЫХ СРЕДАХ  
            **Квалификация:** МАГИСТР  
            **Дата выдачи:** 29.06.2024  
            **Серия и номер:** ААУ 2905592  
            **Регистрационный номер:** 03Ю-0033-311
            """)
        with col2:
            st.info("📘 **Магистратура**\n\n*2022 - 2024*")
    
    # Бакалавриат (2018-2022)
    st.subheader("📚 Бакалавриат")
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            **🏛️ Московский государственный университет имени М.В.Ломоносова**
            
            **Направление:** ФИЗИКА  
            **Программа:** ФИЗИКА. ОБЩИЙ  
            **Квалификация:** БАКАЛАВР  
            **Дата выдачи:** 30.06.2022  
            **Серия и номер:** ААТ 2804072  
            **Регистрационный номер:** 03Д-0034-212
            """)
        with col2:
            st.info("📗 **Бакалавриат**\n\n*2018 - 2022*")
    
    st.divider()
    
    # Достижения и олимпиады
    st.subheader("🏆 Достижения")
    
    # Сортируем достижения по году (от новых к старым)
    achievements = [
        {
            "year": "2021-2022",
            "event": "Универсиада «Ломоносов»",
            "stage": "Заключительный (итоговый) этап",
            "achievement": "🥇 Победитель"
        },
        {
            "year": "2017-2018",
            "event": "Всероссийская олимпиада школьников (Региональный этап)",
            "stage": "Региональный (Брянская область)",
            "achievement": "🥉 Призер"
        },
        {
            "year": "2017-2018",
            "event": "Олимпиада школьников «Физтех» по физике",
            "stage": "Заключительный этап",
            "achievement": "🥈 Призер"
        }
    ]
    
    for ach in sorted(achievements, key=lambda x: x["year"], reverse=True):
        with st.expander(f"📅 {ach['year']} — {ach['event']}"):
            st.write(f"**Этап:** {ach['stage']}")
            st.write(f"**Достижение:** {ach['achievement']}")

# --- 6. Страница "Опыт" ---
elif page == "Опыт":
    st.header("💼 Опыт работы")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.subheader("📖 Репетиторская деятельность")
            st.markdown("""
            **2016 - настоящее время**
            
            - Подготовка к ОГЭ и ЕГЭ по физике
            - Помощь в освоении школьной программы
            - Подготовка к олимпиадам
            - Проведение занятий онлайн и очно
            - **Более 100 успешных учеников**
            """)
    
    with col2:
        with st.container(border=True):
            st.subheader("🏫 Преподавательская практика")
            st.markdown("""
            **2022 - настоящее время**
            
            - Ведение семинарских занятий по физике
            - Разработка учебных материалов
            - Проверка контрольных работ
            - Консультации студентов
            """)
    
    st.divider()
    
    st.subheader("📊 Мои результаты:")
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📈 Средний балл ЕГЭ", "85", "из 100")
    with col2:
        st.metric("🎯 Поступили в вуз", "95%", "учеников")
    with col3:
        st.metric("👨‍🎓 Количество учеников", "150+", "за 8 лет")
    with col4:
        st.metric("⭐ Отзывов", "50+", "положительных")

# --- 7. Страница "Отзывы" ---
elif page == "Отзывы":
    st.header("⭐ Отзывы моих учеников")
    if not df_reviews.empty:
        for _, row in df_reviews.iterrows():
            st.write(f"**{row['Имя']}**: {row['Отзыв']} ★ {row['Оценка']}")
    else:
        st.info("Пока нет отзывов. Будьте первым! 😊")

# --- 8. Страница "Личный кабинет" ---
elif page == "Личный кабинет":
    st.header("🔐 Личный кабинет")
    
    student_name = st.text_input("Введи свое имя для входа (демо-режим)")
    
    if student_name:
        st.subheader(f"Здравствуй, {student_name}! 👋")
        
        user_schedule = df_schedule[df_schedule['Ученик'] == student_name]
        
        if not user_schedule.empty:
            st.write("### 📅 Твои занятия")
            
            # Группируем занятия по статусу
            upcoming = user_schedule[user_schedule['Состоялось'] != "Да"]
            completed = user_schedule[user_schedule['Состоялось'] == "Да"]
            
            if not upcoming.empty:
                st.write("#### ⏳ Предстоящие занятия")
                for _, lesson in upcoming.iterrows():
                    st.write(f"**{lesson['Дата']}** - {lesson.get('Время', '')}")
            
            if not completed.empty:
                st.write("#### ✅ Прошедшие занятия")
                for _, lesson in completed.iterrows():
                    with st.expander(f"📚 {lesson['Дата']}"):
                        if 'Ссылка' in lesson and pd.notna(lesson['Ссылка']):
                            st.write(f"🔗 Ссылка на встречу: {lesson['Ссылка']}")
                        if 'ДЗ' in lesson and pd.notna(lesson['ДЗ']):
                            st.write(f"📄 Домашнее задание: {lesson['ДЗ']}")
                        if 'Конспект' in lesson and pd.notna(lesson['Конспект']):
                            st.write(f"📝 Конспект урока: {lesson['Конспект']}")
        else:
            st.info("У тебя нет запланированных занятий.")
        
        st.divider()
        
        st.write("### 💰 Трекер оплат")
        st.info("Здесь будут данные об оплатах (скоро появится)")
