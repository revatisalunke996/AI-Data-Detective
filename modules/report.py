import streamlit as st

def show_report(df, cleaned_df):
    st.subheader("📋 AI Data Cleaning Report")

    total_rows = len(df)
    total_columns = len(df.columns)

    missing_before = df.isnull().sum().sum()
    missing_after = cleaned_df.isnull().sum().sum()

    duplicate_before = df.duplicated().sum()
    duplicate_after = cleaned_df.duplicated().sum()

    score = 100

    score -= min(missing_before, 50)
    score -= min(duplicate_before * 2, 20)

    if score < 0:
        score = 0

    st.metric("📄 Total Rows", total_rows)
    st.metric("📄 Total Columns", total_columns)

    st.metric("❌ Missing Values Found", missing_before)
    st.metric("✅ Missing Values Remaining", missing_after)

    st.metric("❌ Duplicate Rows Found", duplicate_before)
    st.metric("✅ Duplicate Rows Remaining", duplicate_after)

    st.metric("⭐ Data Quality Score", f"{score}/100")

    if score >= 90:
        st.success("🎉 Excellent Data Quality")
    elif score >= 70:
        st.warning("🙂 Good Data Quality")
    else:
        st.error("⚠ Poor Data Quality")