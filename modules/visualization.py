import streamlit as st
import matplotlib.pyplot as plt


def show_visualizations(df):

    st.subheader("📈 Data Visualizations")

    st.write(
        "Explore your dataset using different charts and "
        "statistical visualizations."
    )

    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    categorical_columns = df.select_dtypes(
        include=["object"]
    ).columns.tolist()

    # ---------------- BAR CHART ----------------

    if len(categorical_columns) > 0:

        st.divider()
        st.write("### 📊 Bar Chart")
        st.caption("Shows the frequency of categories in a column.")

        bar_column = st.selectbox(
            "Select column for Bar Chart",
            categorical_columns,
            key="bar"
        )

        fig, ax = plt.subplots(figsize=(8, 4))

        df[bar_column].value_counts().head(15).plot(
            kind="bar",
            ax=ax
        )

        ax.set_title(f"Bar Chart of {bar_column}")
        ax.set_xlabel(bar_column)
        ax.set_ylabel("Count")

        plt.xticks(rotation=45)
        plt.tight_layout()

        st.pyplot(fig)

    # ---------------- PIE CHART ----------------

    if len(categorical_columns) > 0:

        st.divider()
        st.write("### 🥧 Pie Chart")
        st.caption("Shows the percentage distribution of categories.")

        pie_column = st.selectbox(
            "Select column for Pie Chart",
            categorical_columns,
            key="pie"
        )

        values = df[pie_column].value_counts().head(8)

        fig, ax = plt.subplots(figsize=(6, 6))

        ax.pie(
            values,
            labels=values.index,
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title(f"Pie Chart of {pie_column}")

        st.pyplot(fig)

    # ---------------- HISTOGRAM ----------------

    if len(numeric_columns) > 0:

        st.divider()
        st.write("### 📈 Histogram")
        st.caption("Shows the distribution of numerical values.")

        hist_column = st.selectbox(
            "Select column for Histogram",
            numeric_columns,
            key="hist"
        )

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.hist(
            df[hist_column].dropna(),
            bins=10
        )

        ax.set_title(f"Histogram of {hist_column}")
        ax.set_xlabel(hist_column)
        ax.set_ylabel("Frequency")

        plt.tight_layout()

        st.pyplot(fig)

    # ---------------- BOX PLOT ----------------

    if len(numeric_columns) > 0:

        st.divider()
        st.write("### 📦 Box Plot")
        st.caption(
            "Helps identify the spread and possible outliers "
            "in numerical data."
        )

        box_column = st.selectbox(
            "Select column for Box Plot",
            numeric_columns,
            key="box"
        )

        fig, ax = plt.subplots(figsize=(8, 4))

        ax.boxplot(
            df[box_column].dropna()
        )

        ax.set_title(f"Box Plot of {box_column}")
        ax.set_ylabel(box_column)

        plt.tight_layout()

        st.pyplot(fig)

    # ---------------- CORRELATION HEATMAP ----------------

    if len(numeric_columns) >= 2:

        st.divider()
        st.write("### 🔥 Correlation Heatmap")

        st.caption(
            "Shows the relationship between numerical variables. "
            "Values closer to 1 or -1 indicate stronger relationships."
        )

        correlation = df[numeric_columns].corr()

        fig, ax = plt.subplots(
            figsize=(10, 6)
        )

        heatmap = ax.imshow(
            correlation,
            cmap="coolwarm",
            interpolation="nearest"
        )

        ax.set_xticks(
            range(len(numeric_columns))
        )

        ax.set_yticks(
            range(len(numeric_columns))
        )

        ax.set_xticklabels(
            numeric_columns,
            rotation=45,
            ha="right"
        )

        ax.set_yticklabels(
            numeric_columns
        )

        ax.set_title(
            "Correlation Between Numeric Variables"
        )

        fig.colorbar(
            heatmap,
            ax=ax
        )

        # Display correlation values

        for i in range(len(numeric_columns)):

            for j in range(len(numeric_columns)):

                ax.text(
                    j,
                    i,
                    f"{correlation.iloc[i, j]:.2f}",
                    ha="center",
                    va="center"
                )

        plt.tight_layout()

        st.pyplot(fig)

    elif len(numeric_columns) == 1:

        st.divider()

        st.info(
            "ℹ️ At least two numeric columns are required "
            "to generate a correlation heatmap."
        )