# Statistical Analysis and Hypothesis Testing App

This is a **Streamlit** web application that allows users to upload their own dataset and perform **Exploratory Data Analysis (EDA)**, **Data Visualization**, and **Hypothesis Testing**. The app provides a user-friendly interface for conducting statistical analysis and gaining insights from the data.

## Features

1. **Data Upload**: 
   - Upload a CSV file and preview the first few rows of the dataset.
   - View the dataset dimensions and basic information.

2. **Data Summary**:
   - Generate summary statistics of the uploaded data (mean, median, standard deviation, etc.).
   - Filter the data based on selected columns and values.

3. **Data Visualization**:
   - Create univariate histograms of selected columns for visual analysis.

4. **Hypothesis Testing**:
   - Perform statistical tests including:
     - One-way sample t-test
     - Two-sample t-test
     - Oneway ANOVA
   - Interpret test results and determine if the null hypothesis can be rejected based on the selected significance level (alpha).

## How to Run Locally

To run the app on your local machine, follow these steps:

1. Clone this repository:
    ```bash
    git clone https://github.com/siyamsiza/Hypothesis-Testing-t-tests-ANOVA.git
    ```

2. Navigate to the project directory:
    ```bash
    cd siyamsiza
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

5. Open your browser and go to `http://localhost:8501` to view and interact with the app.

## Deploying the App

This app can be deployed easily on **Streamlit Cloud**. To deploy:
1. Push this project to a GitHub repository.
2. Go to [Streamlit Cloud](https://share.streamlit.io/).
3. Connect your GitHub repository and deploy the app following the prompts.

## Technologies Used

- **Streamlit**: A framework for building interactive web apps in Python.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical operations.
- **Matplotlib**: For plotting data visualizations.
- **Seaborn**: For enhancing data visualization.
- **SciPy**: For performing hypothesis testing.

## Author

**Siyabonga Msiza** – Student at UCT, aspiring Data Scientist specializing in Finance and Machine Learning.

LinkedIn: (https://www.linkedin.com/in/siyabonga-msiza-07506616a/)[Siyabonga]

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
