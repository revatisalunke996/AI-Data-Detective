# AI Data Detective

AI Data Detective is a Streamlit-based data cleaning and analysis application that helps users understand, clean, analyze, and visualize CSV datasets.

The application provides an easy-to-use interface for detecting data quality problems and generating useful insights from uploaded datasets.

## Features

- Upload CSV datasets
- Preview uploaded data
- Display number of rows and columns
- Display column names and data types
- Detect missing values
- Detect duplicate records
- Clean missing values automatically
- Remove duplicate records
- Calculate data quality score
- Generate data quality suggestions
- Generate AI-based dataset insights
- Create data visualizations
- Detect outliers
- Train a Linear Regression model on suitable numeric datasets
- Compare actual and predicted values
- Generate a PDF data report
- Download the cleaned dataset
- Voice assistant support

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- ReportLab
- Pyttsx3

## How It Works

### 1. Upload Dataset

The user uploads a CSV file through the Streamlit interface.

### 2. Dataset Analysis

The application analyzes the uploaded dataset and displays:

- Number of rows
- Number of columns
- Column names
- Data types
- Missing values
- Duplicate records

### 3. Data Cleaning

The application cleans the dataset by:

- Filling missing numeric values using the mean
- Filling missing text values using the mode
- Removing duplicate records

### 4. Data Quality Analysis

The application calculates a quality score and provides suggestions based on detected data problems.

### 5. Visualization

Users can visualize numerical and categorical data using charts such as:

- Bar charts
- Pie charts
- Histograms
- Box plots

### 6. Machine Learning

The application provides a Linear Regression module for suitable numeric datasets.

The user selects a numeric target column, and the application uses the remaining numeric columns as features.

The model displays:

- Model accuracy using R² score
- Model coefficients
- Actual values
- Predicted values

### 7. Reports

The application can generate a PDF report containing information about the uploaded and cleaned dataset.

The cleaned dataset can also be downloaded as a CSV file.

## Project Structure

```text
AI Data Detective/
│
├── data/
│   └── student_data.csv
│
├── images/
│
├── models/
│
├── modules/
│   ├── ai_insights.py
│   ├── ai_suggestions.py
│   ├── dashboard.py
│   ├── ml_model.py
│   ├── pdf_report.py
│   ├── quality_score.py
│   ├── report.py
│   ├── visualization.py
│   └── voice_assistant.py
│
├── notebooks/
│
├── reports/
│
├── .gitignore
├── app.py
├── README.md
└── requirements.txt