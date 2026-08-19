# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Репетитор по физике", layout="wide")

# --- 1. Подключение к Google Таблицам ---
conn = st.connection("gsheets", type=GSheetsConnection)

# --- 2. Загрузка данных ---
@st.cache_data(ttl=600)
def load_data(sheet_name):
    try:
        return conn.read(worksheet=sheet_name, ttl=600)
    except Exception as e:
        st.error(f"Ошибка загрузки из '{sheet_name}': {str(e)}")
        return pd.DataFrame()

df_schedule = load_data("Schedule")
df_students = load_data("Students")
df_reviews = load_data("Reviews")

# --- 3. Навигация ---
st.sidebar.title("📚 Навигация")
page = st.sidebar.radio("Перейти на страницу:", 
                        ["Главная", "Образование", "Опыт", "Отзывы", "Личный кабинет"])

# --- 4. Главная ---
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
        - @no8kaij
        """)

# --- 5. Образование ---
elif page == "Образование":
    st.header("🎓 Мое образование")
    
    st.subheader("📌 Сейчас я здесь:")
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            **🏛️ МГУ имени М.В.Ломоносова**
            
            **Направление:** Оптика  
            **Уровень:** Аспирантура (очная форма)  
            **Курс:** 2  
            **Дата зачисления:** 01.10.2024  
            """)
        with col2:
            st.success("🎯 **Аспирантура**\n\n*2024 - н.в.*")
    
    st.divider()
    
    st.subheader("🎓 Магистратура")
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            **🏛️ МГУ имени М.В.Ломоносова**
            
            **Направление:** ФИЗИКА  
            **Программа:** ФИЗИКА. ВОЛНЫ В СТРУКТУРИРОВАННЫХ СРЕДАХ  
            **Квалификация:** МАГИСТР  
            **Дата выдачи:** 29.06.2024  
            **Серия:** ААУ 2905592
            """)
        with col2:
            st.info("📘 **Магистратура**\n\n*2022 - 2024*")
    
    st.subheader("📚 Бакалавриат")
    with st.container(border=True):
        col1, col2 = st.columns([3, 1])
        with col1:
            st.markdown("""
            **🏛️ МГУ имени М.В.Ломоносова**
            
            **Направление:** ФИЗИКА  
            **Программа:** ФИЗИКА. ОБЩИЙ  
            **Квалификация:** БАКАЛАВР  
            **Дата выдачи:** 30.06.2022  
            **Серия:** ААТ 2804072
            """)
        with col2:
            st.info("📗 **Бакалавриат**\n\n*2018 - 2022*")
    
    st.divider()
    
    st.subheader("🏆 Достижения")
    achievements = [
        {"event": "Научные достижения", "stage": "https://istina.msu.ru/workers/353635785/"},
        {"year": "2021-2022", "event": "Универсиада «Ломоносов»", "stage": "Заключительный этап", "achievement": "🥇 Победитель"},
        {"year": "2017-2018", "event": "Всероссийская олимпиада школьников", "stage": "Региональный (Брянская обл.)", "achievement": "🥉 Призер"},
        {"year": "2017-2018", "event": "Олимпиада «Физтех» по физике", "stage": "Заключительный этап", "achievement": "🥈 Призер"}
    ]
    for ach in sorted(achievements, key=lambda x: x["year"], reverse=True):
        with st.expander(f"📅 {ach['year']} — {ach['event']}"):
            st.write(f"**Этап:** {ach['stage']}")
            st.write(f"**Достижение:** {ach['achievement']}")

# --- 6. Опыт ---
elif page == "Опыт":
    st.header("💼 Опыт работы")
    col1, col2 = st.columns(2)
    with col1:
        with st.container(border=True):
            st.subheader("📖 Репетиторская деятельность")
            st.markdown("**2016 - н.в.**\n- Подготовка к ОГЭ и ЕГЭ\n- Помощь со школьной программой\n- Более 100 успешных учеников")
    with col2:
        with st.container(border=True):
            st.subheader("🏫 Преподавательская практика")
            st.markdown("**2022 - н.в.**\n- Ведение семинаров по физике\n- Разработка учебных материалов")
    st.divider()
    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("📈 Средний балл ЕГЭ", "85")
    with col2: st.metric("🎯 Поступили в вуз", "95%")
    with col3: st.metric("👨‍🎓 Учеников", "150+")
    with col4: st.metric("⭐ Отзывов", "50+")

# --- 7. Отзывы ---
elif page == "Отзывы":
    st.header("⭐ Отзывы моих учеников")
    
    if df_reviews.empty:
        st.info("Пока нет отзывов. Будьте первым! 😊")
    else:
        cols = df_reviews.columns.tolist()
        name_col = next((c for c in cols if any(word in c.lower() for word in ['имя', 'name', 'ученик'])), cols[0] if cols else None)
        review_col = next((c for c in cols if any(word in c.lower() for word in ['отзыв', 'review', 'текст'])), cols[1] if len(cols) > 1 else None)
        
        if name_col and review_col:
            for _, row in df_reviews.iterrows():
                st.write(f"**{row[name_col]}**: {row[review_col]}")
        else:
            st.warning("Показываю все данные:")
            st.dataframe(df_reviews)

# --- 8. Личный кабинет ---
elif page == "Личный кабинет":
    st.header("🔐 Личный кабинет")
    
    student_name = st.text_input("Введи свое имя для входа (демо-режим)")
    
    if student_name:
        st.subheader(f"Здравствуй, {student_name}! 👋")
        
        if df_schedule.empty:
            st.warning("Нет данных о расписании. Добавьте занятия в Google Таблицу.")
        else:
            # Ищем точное совпадение по колонке "Ученик"
            if 'Ученик' in df_schedule.columns:
                user_schedule = df_schedule[df_schedule['Ученик'].astype(str).str.strip() == student_name]
                
                if not user_schedule.empty:
                    st.write("### 📅 Твои занятия")
                    
                    for _, lesson in user_schedule.iterrows():
                        date_val = lesson.get('Дата', 'дата не указана')
                        time_val = lesson.get('Время', '')
                        status_val = lesson.get('Состоялось', '')
                        
                        # Определяем статус
                        if pd.notna(status_val) and str(status_val).strip():
                            status_str = "✅ Состоялось" if str(status_val).lower() in ['да', 'yes', 'true', '1'] else "⏳ Запланировано"
                        else:
                            status_str = "📅 Запланировано"
                        
                        st.write(f"**{date_val} {time_val}** - {status_str}")
                        
                        # Показываем материалы занятия
                        with st.expander("📎 Подробнее"):
                            if 'Ссылка' in lesson and pd.notna(lesson['Ссылка']) and str(lesson['Ссылка']).strip():
                                st.write(f"🔗 **Ссылка на встречу:** {lesson['Ссылка']}")
                            if 'ДЗ' in lesson and pd.notna(lesson['ДЗ']) and str(lesson['ДЗ']).strip():
                                st.write(f"📄 **Домашнее задание:** {lesson['ДЗ']}")
                            if 'Конспект' in lesson and pd.notna(lesson['Конспект']) and str(lesson['Конспект']).strip():
                                st.write(f"📝 **Конспект урока:** {lesson['Конспект']}")
                else:
                    st.info(f"У ученика {student_name} нет запланированных занятий.")
            else:
                st.error("В таблице нет колонки 'Ученик'!")
        
                # --- Трекер оплат ---
        st.divider()
        st.write("### 💰 Трекер оплат")
        
        # Проверяем, есть ли данные об ученике
        if not df_students.empty and 'Имя' in df_students.columns:
            student_data = df_students[df_students['Имя'].astype(str).str.strip() == student_name]
            if not student_data.empty:
                # Здесь можно вывести статус оплаты, если он есть в таблице Students
                # Например, если есть колонка "Оплачено"
                st.write("**Статус оплаты:**")
                st.info("💳 Информация об оплатах будет отображаться здесь")
            else:
                st.info("Данные об оплатах не найдены")
        else:
            st.info("Здесь будут данные об оплатах")
        
        # --- Ссылка на оплату ---
        st.write("---")
        st.write("### 💳 Оплатить занятия")
        st.markdown("""
        **Для оплаты занятий перейдите по ссылке ниже:**
        
        [🔗 Перейти к оплате](https://pro.selfwork.ru/kassa/fizmater)
        
        > *В сумму оплаты включены налог и комиссия платежной системы.*
        """)
        
        # Показываем информацию об оплатах из таблицы Students
        if not df_students.empty and 'Имя' in df_students.columns:
            student_data = df_students[df_students['Имя'].astype(str).str.strip() == student_name]
            if not student_data.empty:
                st.write("**Статус оплаты:**")
                # Здесь можно добавить колонку с оплатой в таблицу Students
                st.info("💳 Информация об оплатах будет отображаться здесь")
            else:
                st.info("Данные об оплатах не найдены")
        else:
            st.info("Здесь будут данные об оплатах (скоро появится)")
