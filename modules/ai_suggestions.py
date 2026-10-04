import streamlit as st

def show_ai_suggestions(df, cleaned_df):

    st.subheader("🤖 AI Suggestions")

    missing_before = df.isnull().sum().sum()
    missing_after = cleaned_df.isnull().sum().sum()

    duplicate_before = df.duplicated().sum()
    duplicate_after = cleaned_df.duplicated().sum()

    suggestions = []

    if missing_before > 0:
        suggestions.append("✅ Missing values were detected and cleaned.")

    if duplicate_before > 0:
        suggestions.append("✅ Duplicate rows were detected and removed.")

    if missing_after == 0:
        suggestions.append("✅ No missing values remain in the cleaned dataset.")

    if duplicate_after == 0:
        suggestions.append("✅ No duplicate rows remain in the cleaned dataset.")

    suggestions.append("🤖 Dataset is ready for Data Analysis.")
    suggestions.append("🤖 Dataset can now be used for Machine Learning.")

    for suggestion in suggestions:
        st.success(suggestion)