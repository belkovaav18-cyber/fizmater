# streamlit_app.py - ДИАГНОСТИЧЕСКАЯ ВЕРСИЯ

import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

st.set_page_config(page_title="Диагностика", layout="wide")

st.title("🔧 Диагностика подключения к Google Таблицам")

# Подключаемся
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    st.success("✅ Подключение к Google Sheets установлено")
except Exception as e:
    st.error(f"❌ Ошибка подключения: {e}")
    st.stop()

# Пытаемся прочитать данные
sheet_names = ["Schedule", "Students", "Reviews"]

for sheet in sheet_names:
    st.subheader(f"📊 Лист '{sheet}'")
    try:
        df = conn.read(worksheet=sheet, ttl=60)
        if df.empty:
            st.warning(f"⚠️ Лист '{sheet}' существует, но пуст или нет доступа")
        else:
            st.success(f"✅ Загружено {len(df)} строк")
            st.write("**Колонки:**", df.columns.tolist())
            st.dataframe(df)
    except Exception as e:
        st.error(f"❌ Ошибка при чтении листа '{sheet}': {e}")

# Проверяем, какие листы вообще есть в таблице
st.subheader("📋 Все листы в таблице")
try:
    # Пробуем получить информацию о всех листах
    spreadsheet = conn.client.spreadsheet
    sheets = spreadsheet.worksheets()
    st.write("Найденные листы:")
    for s in sheets:
        st.write(f"- {s.title}")
except Exception as e:
    st.error(f"Не удалось получить список листов: {e}")

st.info("💡 Если ничего не загружается, проверьте:")
st.markdown("""
1. Добавлен ли сервисный аккаунт `fizmater@fizmater.iam.gserviceaccount.com` в таблицу с правами редактора
2. Правильно ли называются листы (регистр важен!)
3. Есть ли данные в таблице
""")
