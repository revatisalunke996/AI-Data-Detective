import streamlit as st
import pandas as pd

from modules.voice_assistant import speak
from modules.report import show_report
from modules.ai_suggestions import show_ai_suggestions
from modules.quality_score import show_quality_score
from modules.ai_insights import show_ai_insights
from modules.pdf_report import generate_pdf_report
from modules.dashboard import show_dashboard
from modules.ml_model import train_model
from modules.visualization import show_visualizations


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Data Detective",
    page_icon="🕵️",
    layout="wide"
)


# =========================================================
# SESSION STATE
# =========================================================

if "df" not in st.session_state:
    st.session_state.df = None

if "cleaned_df" not in st.session_state:
    st.session_state.cleaned_df = None

if "uploaded_name" not in st.session_state:
    st.session_state.uploaded_name = None

if "welcome_spoken" not in st.session_state:
    st.session_state.welcome_spoken = False


# =========================================================
# SIDEBAR NAVIGATION
# =========================================================

st.sidebar.title("🕵️ AI Data Detective")

menu = st.sidebar.radio(
    "📋 Navigation",
    [
        "🏠 Home",
        "📂 Upload Dataset",
        "📊 Dashboard",
        "🤖 AI Analysis",
        "📈 Visualization",
        "📄 Reports",
        "🤖 Machine Learning",
        "ℹ️ About"
    ]
)


# =========================================================
# APPLICATION TITLE
# =========================================================

st.title("🕵️ AI Data Detective")

st.subheader(
    "AI Powered Data Cleaning & Analysis Assistant"
)


# =========================================================
# HOME PAGE
# =========================================================

if menu == "🏠 Home":

    st.markdown(
        """
        ## 👋 Welcome to AI Data Detective!

        AI Data Detective is a data cleaning and analysis
        application that helps users understand and prepare
        their datasets.

        ### 🚀 What you can do

        - 📂 Upload CSV datasets
        - 👀 Preview your dataset
        - 🔍 Detect missing values
        - 📋 Detect duplicate rows
        - 🧹 Clean missing values
        - 🗑️ Remove duplicate rows
        - 📊 Analyze data quality
        - 📈 Generate visualizations
        - 🧠 Get AI-based insights
        - 🤖 Get data cleaning suggestions
        - 🤖 Train a Machine Learning model
        - 📄 Generate downloadable PDF reports

        ### 🔄 Workflow

        **Upload → Analyze → Clean → Visualize → ML → Report**
        """
    )

    if not st.session_state.welcome_spoken:

        try:
            speak(
                "Welcome to AI Data Detective. "
                "Your AI powered data cleaning assistant."
            )
        except Exception:
            pass

        st.session_state.welcome_spoken = True


# =========================================================
# UPLOAD DATASET PAGE
# =========================================================

elif menu == "📂 Upload Dataset":

    st.header("📂 Upload Dataset")

    uploaded_file = st.file_uploader(
        "Upload your CSV file",
        type=["csv"]
    )

    if uploaded_file is not None:

        try:

            df = pd.read_csv(uploaded_file)

            st.session_state.df = df
            st.session_state.uploaded_name = uploaded_file.name

            # -------------------------------------------------
            # CREATE CLEANED DATASET
            # -------------------------------------------------

            cleaned_df = df.copy()

            # Numeric columns
            numeric_columns = cleaned_df.select_dtypes(
                include=["number"]
            ).columns

            if len(numeric_columns) > 0:

                cleaned_df[numeric_columns] = (
                    cleaned_df[numeric_columns]
                    .fillna(
                        cleaned_df[numeric_columns].mean()
                    )
                )

            # Text columns
            text_columns = cleaned_df.select_dtypes(
                include=["object"]
            ).columns

            for column in text_columns:

                mode_value = cleaned_df[column].mode()

                if not mode_value.empty:

                    cleaned_df[column] = (
                        cleaned_df[column]
                        .fillna(mode_value.iloc[0])
                    )

            # Remove duplicates
            cleaned_df = cleaned_df.drop_duplicates()

            st.session_state.cleaned_df = cleaned_df

            st.success(
                "✅ Dataset uploaded successfully!"
            )

            try:
                speak(
                    "Dataset uploaded successfully."
                )
            except Exception:
                pass

            # -------------------------------------------------
            # DATASET PREVIEW
            # -------------------------------------------------

            st.subheader("📄 Dataset Preview")

            st.dataframe(
                df,
                use_container_width=True
            )

            # -------------------------------------------------
            # DATASET SUMMARY
            # -------------------------------------------------

            st.subheader("📊 Dataset Summary")

            col1, col2, col3 = st.columns(3)

            with col1:
                st.metric(
                    "Total Rows",
                    df.shape[0]
                )

            with col2:
                st.metric(
                    "Total Columns",
                    df.shape[1]
                )

            with col3:
                st.metric(
                    "Total Missing Values",
                    int(df.isnull().sum().sum())
                )

            # -------------------------------------------------
            # COLUMN NAMES
            # -------------------------------------------------

            st.subheader("📋 Column Names")

            st.write(
                list(df.columns)
            )

            # -------------------------------------------------
            # DATA TYPES
            # -------------------------------------------------

            st.subheader("🔤 Data Types")

            datatype_df = (
                df.dtypes
                .astype(str)
                .reset_index()
            )

            datatype_df.columns = [
                "Column Name",
                "Data Type"
            ]

            st.dataframe(
                datatype_df,
                use_container_width=True
            )

            # -------------------------------------------------
            # MISSING VALUES
            # -------------------------------------------------

            st.subheader(
                "🔍 Missing Value Detection"
            )

            missing_values = df.isnull().sum()

            missing_df = (
                missing_values
                .reset_index()
            )

            missing_df.columns = [
                "Column Name",
                "Missing Values"
            ]

            st.dataframe(
                missing_df,
                use_container_width=True
            )

            total_missing = int(
                missing_values.sum()
            )

            if total_missing == 0:

                st.success(
                    "🎉 No Missing Values Found!"
                )

            else:

                st.warning(
                    f"⚠️ Total Missing Values: "
                    f"{total_missing}"
                )

            # -------------------------------------------------
            # DUPLICATE DETECTION
            # -------------------------------------------------

            st.subheader(
                "📋 Duplicate Detection"
            )

            duplicate_count = int(
                df.duplicated().sum()
            )

            if duplicate_count == 0:

                st.success(
                    "🎉 No Duplicate Rows Found!"
                )

            else:

                st.warning(
                    f"⚠️ Duplicate Rows Found: "
                    f"{duplicate_count}"
                )

                st.dataframe(
                    df[df.duplicated()],
                    use_container_width=True
                )

            # -------------------------------------------------
            # CLEAN DATASET
            # -------------------------------------------------

            st.subheader(
                "🧹 Cleaned Dataset"
            )

            if st.button(
                "🧹 Clean Dataset",
                use_container_width=True
            ):

                st.success(
                    "✅ Dataset Cleaned Successfully!"
                )

                st.dataframe(
                    cleaned_df,
                    use_container_width=True
                )

            # -------------------------------------------------
            # DOWNLOAD CLEANED CSV
            # -------------------------------------------------

            st.subheader(
                "📥 Download Cleaned Dataset"
            )

            csv_data = (
                cleaned_df
                .to_csv(index=False)
                .encode("utf-8")
            )

            st.download_button(
                label="📥 Download Cleaned CSV",
                data=csv_data,
                file_name="cleaned_dataset.csv",
                mime="text/csv",
                use_container_width=True
            )

        except Exception as e:

            st.error(
                f"❌ Error reading dataset: {e}"
            )

    else:

        st.info(
            "📂 Please upload a CSV file to continue."
        )


# =========================================================
# CHECK DATASET
# =========================================================

elif menu != "🏠 Home":

    df = st.session_state.df
    cleaned_df = st.session_state.cleaned_df

    if df is None or cleaned_df is None:

        st.warning(
            "⚠️ Please upload a CSV dataset first."
        )

        st.info(
            "Go to **📂 Upload Dataset** from the sidebar."
        )

    else:

        # =================================================
        # DASHBOARD
        # =================================================

        if menu == "📊 Dashboard":

            st.header("📊 Data Dashboard")

            show_dashboard(
                df,
                cleaned_df
            )

            st.divider()

            st.subheader(
                "🔍 Missing Values by Column"
            )

            missing_data = (
                df.isnull()
                .sum()
                .sort_values(
                    ascending=False
                )
            )

            if missing_data.sum() > 0:

                st.bar_chart(
                    missing_data
                )

            else:

                st.success(
                    "🎉 Your dataset has no missing values."
                )


        # =================================================
        # AI ANALYSIS
        # =================================================

        elif menu == "🤖 AI Analysis":

            st.header(
                "🤖 AI Data Analysis"
            )

            show_ai_insights(
                df,
                cleaned_df
            )

            st.divider()

            show_ai_suggestions(
                df,
                cleaned_df
            )

            st.divider()

            show_quality_score(
                df,
                cleaned_df
            )


        # =================================================
        # VISUALIZATION
        # =================================================

        elif menu == "📈 Visualization":

            st.header(
                "📈 Data Visualization"
            )

            show_visualizations(
                df
            )


        # =================================================
        # REPORTS
        # =================================================

        elif menu == "📄 Reports":

            st.header(
                "📄 Data Reports"
            )

            show_report(
                df,
                cleaned_df
            )

            st.divider()

            st.subheader(
                "📄 Generate PDF Report"
            )

            if st.button(
                "📄 Generate AI PDF Report",
                use_container_width=True
            ):

                try:

                    pdf_path = generate_pdf_report(
                        df,
                        cleaned_df
                    )

                    st.success(
                        "✅ PDF Report Generated Successfully!"
                    )

                    with open(
                        pdf_path,
                        "rb"
                    ) as pdf_file:

                        st.download_button(
                            label="📥 Download PDF Report",
                            data=pdf_file,
                            file_name=(
                                "AI_Data_Detective_Report.pdf"
                            ),
                            mime="application/pdf",
                            use_container_width=True
                        )

                except Exception as e:

                    st.error(
                        f"❌ Could not generate PDF: {e}"
                    )


        # =================================================
        # MACHINE LEARNING
        # =================================================

        elif menu == "🤖 Machine Learning":

            st.header(
                "🤖 Machine Learning Analysis"
            )

            st.write(
                "Use Linear Regression to predict "
                "a selected numeric target column."
            )

            # -------------------------------------------------
            # NUMERIC COLUMNS
            # -------------------------------------------------

            numeric_columns = (
                cleaned_df
                .select_dtypes(
                    include=["number"]
                )
                .columns
                .tolist()
            )

            if len(numeric_columns) < 2:

                st.warning(
                    "⚠️ Machine Learning requires "
                    "at least two numeric columns."
                )

            else:

                # -------------------------------------------------
                # TARGET COLUMN
                # -------------------------------------------------

                target_column = st.selectbox(
                    "🎯 Select Target Column",
                    numeric_columns
                )

                st.info(
                    f"🎯 Target Column: "
                    f"**{target_column}**"
                )

                # -------------------------------------------------
                # TRAIN MODEL
                # -------------------------------------------------

                if st.button(
                    "🚀 Train Machine Learning Model",
                    use_container_width=True
                ):

                    try:

                        model, result, prediction_results = (
                            train_model(
                                cleaned_df,
                                target_column
                            )
                        )

                        if model is None:

                            st.error(
                                f"❌ {result}"
                            )

                        else:

                            st.success(
                                "✅ Machine Learning "
                                "Model Trained Successfully!"
                            )

                            st.subheader(
                                "📊 Model Details"
                            )

                            st.write(
                                "**Algorithm:** "
                                "Linear Regression"
                            )

                            st.write(
                                f"**Target Column:** "
                                f"{target_column}"
                            )

                            st.metric(
                                "Model Accuracy (R²)",
                                f"{result:.2f}%"
                            )

                            st.subheader(
                                "🔮 Actual vs Predicted"
                            )

                            st.dataframe(
                                prediction_results,
                                use_container_width=True
                            )

                            # -------------------------------------------------
                            # MODEL COEFFICIENTS
                            # -------------------------------------------------

                            st.subheader(
                                "📌 Model Coefficients"
                            )

                            coefficient_df = pd.DataFrame(
                                {
                                    "Feature": (
                                        model.feature_names_in_
                                    ),
                                    "Coefficient": (
                                        model.coef_
                                    )
                                }
                            )

                            st.dataframe(
                                coefficient_df,
                                use_container_width=True
                            )

                            st.write(
                                "**Intercept:**",
                                model.intercept_
                            )

                    except Exception as e:

                        st.error(
                            f"❌ Machine Learning Error: {e}"
                        )


        # =================================================
        # ABOUT
        # =================================================

        elif menu == "ℹ️ About":

            st.header(
                "ℹ️ About AI Data Detective"
            )

            st.markdown(
                """
                ## 🕵️ AI Data Detective

                AI Data Detective is an intelligent data
                cleaning and analysis application.

                ### ✨ Features

                - 📂 CSV Dataset Upload
                - 📄 Dataset Preview
                - 🔍 Missing Value Detection
                - 📋 Duplicate Detection
                - 🧹 Automatic Data Cleaning
                - ⭐ Data Quality Score
                - 🧠 AI Insights
                - 🤖 AI Suggestions
                - 📈 Data Visualization
                - 🤖 Machine Learning
                - 📄 PDF Report Generation

                ### 🛠️ Technologies Used

                - Python
                - Streamlit
                - Pandas
                - Matplotlib
                - Scikit-learn
                - ReportLab

                ### 🔄 Data Processing Workflow

                **Upload Dataset**

                ↓

                **Analyze Dataset**

                ↓

                **Detect Data Problems**

                ↓

                **Clean Dataset**

                ↓

                **Visualize Data**

                ↓

                **Machine Learning**

                ↓

                **Generate Report**
                """
            )