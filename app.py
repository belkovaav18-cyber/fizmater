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
    
    # --- Достижения ---
    st.subheader("🏆 Достижения и публикации")
    
    # Разделим на две категории: с годами и без
    achievements_with_year = [
        {"year": "2021-2022", "event": "Универсиада «Ломоносов»", "stage": "Заключительный этап", "achievement": "🥇 Победитель"},
        {"year": "2017-2018", "event": "Всероссийская олимпиада школьников", "stage": "Региональный (Брянская обл.)", "achievement": "🥉 Призер"},
        {"year": "2017-2018", "event": "Олимпиада «Физтех» по физике", "stage": "Заключительный этап", "achievement": "🥈 Призер"}
    ]
    
    achievements_without_year = [
        {"event": "Научные достижения", "stage": "https://istina.msu.ru/workers/353635785/"}
    ]
    
    # Сортируем достижения с годами (от новых к старым)
    for ach in sorted(achievements_with_year, key=lambda x: x["year"], reverse=True):
        with st.expander(f"📅 {ach['year']} — {ach['event']}"):
            st.write(f"**Этап:** {ach['stage']}")
            st.write(f"**Достижение:** {ach['achievement']}")
    
    # Показываем достижения без года отдельно
    for ach in achievements_without_year:
        with st.expander(f"🔬 {ach['event']}"):
            st.write(f"**Ссылка:** {ach['stage']}")

# --- 6. Опыт ---
elif page == "Опыт":
    st.header("💼 Опыт работы")
    
    # ---- 1. Текущие места работы ----
    st.subheader("📍 Текущие места работы")
    
    col1, col2 = st.columns(2)
    
    with col1:
        with st.container(border=True):
            st.markdown("""
            **🏛️ Международный центр квантовой оптики и квантовых технологий**
            
            **Должность:** Младший научный сотрудник  
            **Группа:** Группа Белотелова  
            **Дата начала:** 10.04.2026  
            **Условия:** Неполный рабочий день
            """)
    
    with col2:
        with st.container(border=True):
            st.markdown("""
            **🏛️ Физический факультет МГУ имени М.В.Ломоносова**
            
            **Должность:** Младший научный сотрудник  
            **Кафедра:** Нанофотоники 19/23-НФ  
            **Дата начала:** 17.04.2026  
            **Условия:** По совместительству
            """)
    
    # Второй ряд текущих мест
    col3, col4 = st.columns(2)
    
    with col3:
        with st.container(border=True):
            st.markdown("""
            **🏛️ Физический факультет МГУ имени М.В.Ломоносова**
            
            **Должность:** Младший научный сотрудник  
            **Кафедра:** Нанофотоники 12/24-НФ  
            **Дата начала:** 17.04.2026  
            **Условия:** По совместительству
            """)
    
    with col4:
        with st.container(border=True):
            st.markdown("""
            **📖 Репетиторская деятельность**
            
            **Должность:** Репетитор по физике  
            **Период:** 2016 - настоящее время  
            **Направления:** Подготовка к ОГЭ, ЕГЭ, помощь со школьной программой
            """)
    
    st.divider()
    
    # ---- 2. Предыдущий опыт работы ----
    st.subheader("📋 Предыдущие места работы")
    
    # Используем вкладки для категорий
    tab1, tab2, tab3 = st.tabs(["🏫 Научные организации", "📚 Образовательные учреждения", "📄 Полная хронология"])
    
    with tab1:
        st.markdown("""
        **Международный центр квантовой оптики и квантовых технологий**
        - Младший научный сотрудник (01.10.2020 - 06.04.2022)
        - Группа Белотелова
        
        **Физический факультет МГУ имени М.В.Ломоносова**
        - Младший научный сотрудник, кафедра фотоники и физики микроволн (01.08.2023 - 31.12.2023), по совместительству
        - Лаборант, кафедра фотоники и физики микроволн (07.02.2024 - 31.12.2024)
        - Лаборант, кафедра нанофотоники 19/23-НФ (18.12.2024 - 31.12.2024)
        - Лаборант, кафедра нанофотоники 12/24-НФ (18.12.2024 - 31.12.2024), по совместительству
        - Младший научный сотрудник, кафедра нанофотоники 19/23-НФ (25.03.2025 - 31.12.2025)
        - Младший научный сотрудник, кафедра нанофотоники 12/24-НФ (25.03.2025 - 31.12.2025), по совместительству
        """)
    
    with tab2:
        st.markdown("""
        **ГБОУ Школа № 1253**
        - Учитель (03.02.2023 - 09.01.2024)
        
        **ГБОУ Школа № 2101**
        - Педагог дополнительного образования (14.04.2025 - 30.08.2025), по совместительству
        """)
    
    with tab3:
        # Создаем DataFrame для хронологии
        experience_data = {
            "Дата": [
                "10.04.2026", "17.04.2026", "17.04.2026",
                "14.04.2025 - 30.08.2025", "25.03.2025 - 31.12.2025", "25.03.2025 - 31.12.2025",
                "18.12.2024 - 31.12.2024", "18.12.2024 - 31.12.2024",
                "07.02.2024 - 31.12.2024", "01.08.2023 - 31.12.2023",
                "03.02.2023 - 09.01.2024", "01.10.2020 - 06.04.2022"
            ],
            "Организация": [
                "МЦКОиКТ", "МГУ (19/23-НФ)", "МГУ (12/24-НФ)",
                "Школа № 2101", "МГУ (19/23-НФ)", "МГУ (12/24-НФ)",
                "МГУ (19/23-НФ)", "МГУ (12/24-НФ)",
                "МГУ (фотоника)", "МГУ (фотоника)",
                "Школа № 1253", "МЦКОиКТ"
            ],
            "Должность": [
                "Мл. научный сотрудник", "Мл. научный сотрудник", "Мл. научный сотрудник",
                "Педагог ДО", "Мл. научный сотрудник", "Мл. научный сотрудник",
                "Лаборант", "Лаборант",
                "Лаборант", "Мл. научный сотрудник",
                "Учитель", "Мл. научный сотрудник"
            ]
        }
        df_exp = pd.DataFrame(experience_data)
        st.dataframe(df_exp, use_container_width=True, hide_index=True)
    
    st.divider()
    
    # ---- 3. Общий стаж ----
    st.subheader("📊 Сводка")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("🏛️ Научных организаций", "3")
    with col2:
        st.metric("📚 Образовательных учреждений", "2")
    with col3:
        st.metric("📅 Общий научный стаж", "~5 лет")
    
    st.caption("Данные основаны на записях в трудовой книжке")


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
