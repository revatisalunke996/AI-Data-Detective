import streamlit as st


def detect_outliers(df):

    st.subheader("🔎 Outlier Detection")

    numeric_columns = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    if len(numeric_columns) == 0:
        st.info("No numeric columns available for outlier detection.")
        return

    results = []

    for column in numeric_columns:

        data = df[column].dropna()

        if len(data) < 4:
            continue

        q1 = data.quantile(0.25)
        q3 = data.quantile(0.75)

        iqr = q3 - q1

        lower_limit = q1 - (1.5 * iqr)
        upper_limit = q3 + (1.5 * iqr)

        outliers = data[
            (data < lower_limit) |
            (data > upper_limit)
        ]

        results.append({
            "Column": column,
            "Outliers": len(outliers),
            "Lower Limit": round(lower_limit, 2),
            "Upper Limit": round(upper_limit, 2)
        })

    if len(results) == 0:

        st.info("Not enough data to detect outliers.")

    else:

        st.dataframe(
            results,
            use_container_width=True
        )