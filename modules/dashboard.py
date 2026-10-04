import streamlit as st

def show_dashboard(df, cleaned_df):

    st.subheader("📊 Dashboard")

    total_rows = len(df)
    total_columns = len(df.columns)

    missing_values = df.isnull().sum().sum()
    duplicate_rows = df.duplicated().sum()

    score = 100
    score -= min(missing_values, 50)
    score -= min(duplicate_rows * 2, 20)

    if score < 0:
        score = 0

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📄 Total Rows", total_rows)

    with col2:
        st.metric("📑 Total Columns", total_columns)

    col3, col4 = st.columns(2)

    with col3:
        st.metric("❌ Missing Values", missing_values)

    with col4:
        st.metric("🔁 Duplicate Rows", duplicate_rows)

    st.metric("⭐ Quality Score", f"{score}/100")

    st.progress(score / 100)

