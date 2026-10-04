import streamlit as st

def show_ai_insights(df, cleaned_df):

    st.subheader("🧠 AI Insights")

    numeric_columns = df.select_dtypes(include=["number"]).columns
    categorical_columns = df.select_dtypes(include=["object"]).columns

    missing_column = df.isnull().sum().idxmax()
    missing_count = df.isnull().sum().max()

    st.info(f"📊 Total Numeric Columns : {len(numeric_columns)}")
    st.info(f"📝 Total Categorical Columns : {len(categorical_columns)}")

    if missing_count > 0:
        st.warning(f"⚠ Most missing values are in '{missing_column}' ({missing_count} values).")
    else:
        st.success("✅ No missing values found in the dataset.")

    if len(numeric_columns) >= 2:
        st.success("🤖 This dataset is suitable for Machine Learning.")

    if len(categorical_columns) > len(numeric_columns):
        st.info("💡 This dataset contains many categorical features. Encoding may be required.")

    st.success("🎉 Dataset analysis completed successfully.")