# streamlit_app.py

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

# --- Настройка страницы (должна быть первой) ---
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

# Загружаем данные
df_schedule = load_data("Schedule")
df_students = load_data("Students")
df_reviews = load_data("Reviews")

# --- 3. Навигация ---
st.sidebar.title("📚 Навигация")

# Кнопка обновления
if st.sidebar.button("🔄 Обновить данные из таблицы"):
    st.cache_data.clear()
    st.rerun()

page = st.sidebar.radio("Перейти на страницу:", 
                        ["Главная", "Образование", "Опыт", "Отзывы", "Личный кабинет"],
                        key="main_navigation")

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
        - ✉️ alexandra@email.com
        - 📱 +7 (XXX) XXX-XX-XX
        - 📍 Москва (онлайн)
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
    
    achievements_with_year = [
        {"year": "2021-2022", "event": "Универсиада «Ломоносов»", "stage": "Заключительный этап", "achievement": "🥇 Победитель"},
        {"year": "2017-2018", "event": "Всероссийская олимпиада школьников", "stage": "Региональный (Брянская обл.)", "achievement": "🥉 Призер"},
        {"year": "2017-2018", "event": "Олимпиада «Физтех» по физике", "stage": "Заключительный этап", "achievement": "🥈 Призер"}
    ]
    
    achievements_without_year = [
        {"event": "Научные достижения", "link": "https://istina.msu.ru/workers/353635785/"}
    ]
    
    for ach in sorted(achievements_with_year, key=lambda x: x["year"], reverse=True):
        with st.expander(f"📅 {ach['year']} — {ach['event']}"):
            st.write(f"**Этап:** {ach['stage']}")
            st.write(f"**Достижение:** {ach['achievement']}")
    
    for ach in achievements_without_year:
        with st.expander(f"🔬 {ach['event']}"):
            st.markdown(f"[Перейти к профилю на ИСТИНА]({ach['link']})")

# --- 6. Опыт ---
elif page == "Опыт":
    st.header("💼 Опыт работы")
    
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
    
    st.subheader("📋 Предыдущие места работы")
    
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
    
    # --- Отображение существующих отзывов ---
    if not df_reviews.empty:
        st.subheader("📖 Что говорят мои ученики")
        
        # Проверяем колонки
        cols = df_reviews.columns.tolist()
        name_col = next((c for c in cols if any(word in c.lower() for word in ['имя', 'name', 'ученик'])), None)
        review_col = next((c for c in cols if any(word in c.lower() for word in ['отзыв', 'review', 'текст'])), None)
        rating_col = next((c for c in cols if any(word in c.lower() for word in ['оценк', 'rating', 'балл'])), None)
        
        if name_col and review_col:
            # Показываем отзывы в красивом формате
            for _, row in df_reviews.iterrows():
                rating_stars = "⭐" * int(row[rating_col]) if rating_col and pd.notna(row[rating_col]) else ""
                st.markdown(f"""
                <div style="background-color: #f0f2f6; padding: 15px; border-radius: 10px; margin-bottom: 10px;">
                    <strong>{row[name_col]}</strong> {rating_stars}
                    <p style="margin-top: 5px;">{row[review_col]}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.dataframe(df_reviews)
    else:
        st.info("📭 Пока нет отзывов. Будьте первым! 😊")
    
    st.divider()
    
    # --- Форма для добавления отзыва ---
    st.subheader("✍️ Оставить отзыв")
    st.caption("Ваше мнение поможет другим ученикам сделать выбор")
    
    with st.form(key="review_form", clear_on_submit=True):
        col1, col2 = st.columns(2)
        
        with col1:
            reviewer_name = st.text_input(
                "Ваше имя",
                placeholder="Введите ваше имя",
                key="reviewer_name"
            )
        
        with col2:
            rating = st.select_slider(
                "Оценка",
                options=[1, 2, 3, 4, 5],
                value=5,
                key="review_rating"
            )
            st.caption(f"⭐ {rating} из 5")
        
        review_text = st.text_area(
            "Ваш отзыв",
            placeholder="Расскажите о вашем опыте занятий...",
            height=100,
            key="review_text"
        )
        
        # Кнопка отправки
        submitted = st.form_submit_button("📤 Отправить отзыв")
        
        if submitted:
            # Проверяем, что поля заполнены
            if not reviewer_name.strip():
                st.error("❌ Пожалуйста, введите ваше имя")
            elif not review_text.strip():
                st.error("❌ Пожалуйста, напишите текст отзыва")
            else:
                try:
                    # Подготавливаем данные для записи
                    new_review = pd.DataFrame({
                        'Имя': [reviewer_name.strip()],
                        'Отзыв': [review_text.strip()],
                        'Оценка': [rating]
                    })
                    
                    # Проверяем, есть ли уже данные в таблице
                    if df_reviews.empty:
                        # Если таблица пустая, записываем новые данные
                        conn.update(worksheet="Reviews", data=new_review)
                    else:
                        # Если данные есть, добавляем новую строку
                        # Получаем существующие данные и добавляем новую
                        existing_data = conn.read(worksheet="Reviews", ttl=0)
                        updated_data = pd.concat([existing_data, new_review], ignore_index=True)
                        conn.update(worksheet="Reviews", data=updated_data)
                    
                    # Очищаем кэш, чтобы отзыв сразу отобразился
                    st.cache_data.clear()
                    
                    # Показываем успешное сообщение
                    st.success("✅ Спасибо за ваш отзыв! Он появится на странице после обновления.")
                    
                    # Перезагружаем данные
                    st.rerun()
                    
                except Exception as e:
                    st.error(f"❌ Ошибка при сохранении отзыва: {str(e)}")
                    st.info("💡 Убедитесь, что в Google Таблице есть лист 'Reviews' с колонками: Имя, Отзыв, Оценка")

# --- 8. Личный кабинет ---
elif page == "Личный кабинет":
    st.header("🔐 Личный кабинет")
    
    student_name = st.text_input("Введи свое имя для входа (демо-режим)", key="student_name_input")
    
    if student_name:
        st.subheader(f"Здравствуй, {student_name}! 👋")
        
        if df_schedule.empty:
            st.warning("Нет данных о расписании. Добавьте занятия в Google Таблицу.")
        else:
            if 'Ученик' in df_schedule.columns:
                user_schedule = df_schedule[df_schedule['Ученик'].astype(str).str.strip() == student_name]
                
                if not user_schedule.empty:
                    st.write("### 📅 Твои занятия")
                    
                    for idx, lesson in user_schedule.iterrows():
                        date_val = lesson.get('Дата', 'дата не указана')
                        time_val = lesson.get('Время', '')
                        status_val = lesson.get('Состоялось', '')
                        
                        if pd.notna(status_val) and str(status_val).strip():
                            status_str = "✅ Состоялось" if str(status_val).lower() in ['да', 'yes', 'true', '1'] else "⏳ Запланировано"
                        else:
                            status_str = "📅 Запланировано"
                        
                        payment_status = lesson.get('Оплачено', '')
                        if pd.notna(payment_status) and str(payment_status).strip().lower() in ['да', 'yes', 'true', '1', '✅']:
                            payment_icon = "✅"
                            payment_text = "Оплачено"
                        else:
                            payment_icon = "❌"
                            payment_text = "Не оплачено"
                        
                        st.write(f"**{date_val} {time_val}** - {status_str} &nbsp;&nbsp; {payment_icon} {payment_text}")
                        
                        with st.expander(f"📎 Подробнее - {date_val}"):
                            has_content = False
                            
                            if 'Ссылка' in lesson:
                                link_val = lesson['Ссылка']
                                if pd.notna(link_val) and str(link_val).strip():
                                    st.write(f"🔗 **Ссылка на встречу:** {link_val}")
                                    has_content = True
                            
                            if 'ДЗ' in lesson:
                                dz_val = lesson['ДЗ']
                                if pd.notna(dz_val) and str(dz_val).strip():
                                    st.write(f"📄 **Домашнее задание:** {dz_val}")
                                    has_content = True
                            
                            if 'Конспект' in lesson:
                                konspekt_val = lesson['Конспект']
                                if pd.notna(konspekt_val) and str(konspekt_val).strip():
                                    st.write(f"📝 **Конспект урока:** {konspekt_val}")
                                    has_content = True
                            
                            if not has_content:
                                st.info("📭 Материалы к занятию пока не добавлены")
                else:
                    st.info(f"У ученика {student_name} нет запланированных занятий.")
            else:
                st.error("В таблице нет колонки 'Ученик'!")
        
        st.divider()
        
        st.write("### 💳 Оплатить занятия")
        st.markdown("""
        **Для оплаты занятий перейдите по ссылке ниже:**
        
        [🔗 Перейти к оплате](https://pro.selfwork.ru/kassa/fizmater)
        
        > *В сумму оплаты включены налог и комиссия платежной системы.*
        """)
