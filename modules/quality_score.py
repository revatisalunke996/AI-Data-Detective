import streamlit as st

def show_quality_score(df, cleaned_df):

    missing_before = df.isnull().sum().sum()
    duplicate_before = df.duplicated().sum()

    score = 100

    # Deduct score for missing values
    score -= min(missing_before, 50)

    # Deduct score for duplicate rows
    score -= min(duplicate_before * 2, 20)

    if score < 0:
        score = 0

    st.subheader("⭐ AI Data Quality Score")

    st.progress(score / 100)

    st.metric("Quality Score", f"{score}/100")

    if score >= 90:
        st.success("🎉 Excellent Dataset")
    elif score >= 70:
        st.warning("🙂 Good Dataset")
    else:
        st.error("⚠ Poor Dataset")
        