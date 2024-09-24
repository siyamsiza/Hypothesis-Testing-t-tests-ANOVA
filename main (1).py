import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns


#st.set_page_config(layout="wide")
st.sidebar.title("Exploratory Data Analysis")
page = st.sidebar.radio("Select a section:", ["Data Upload", "Data Summary", "Data Visualization", "Hypothesis Testing"])

#App title
st.title("Statistical Analysis: Hypothesis Testing")
st.write("Author: Siyabonga Msiza")
st.subheader("Upload Your Dataset")

#Uploading a csv file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

#Data Preview
if page == 'Data Upload':
    if uploaded_file is not None:
       df = pd.read_csv(uploaded_file)
       st.success("Dataset uploaded successfully!")

       st.header("Exploratory Data Analysis(EDA)")

       st.subheader("Data Preview")
       st.write(df.head())

       st.subheader("Data Dimension")
       st.write(f"Number of rows: {df.shape[0]}")
       st.write(f"Number of columns: {df.shape[1]}")

       st.subheader("Basic inforamtion about the dataset")
       st.write(df.info(verbose=False))

#Data Summarization
if page == 'Data Summary':
    if uploaded_file is not None:
       df = pd.read_csv(uploaded_file)
       st.subheader("Summary Statistics")
       st.write(df.describe())

       st.subheader("Filter Data")
       columns = df.columns.tolist()
       selected_column = st.selectbox("Select a column to filter by", columns)
       unique_values = df[selected_column].unique()
       selected_value = st.selectbox("Select value", unique_values)

       filtered_df = df[df[selected_column]==selected_value]
       st.write(filtered_df.head())

#Data Visualization
if page=='Data Visualization':
    if uploaded_file is not None:
       df = pd.read_csv(uploaded_file)
       st.subheader("Univariate Data Plot")
       columns = df.columns.tolist()
       column = st.selectbox("Select a column", columns)
       plt.style.use('ggplot')
       fig, ax = plt.subplots()
       ax.hist(df[column], color='lightblue', edgecolor='red')
       st.pyplot(fig)

#Hypothesis Testing
if page=='Hypothesis Testing':
    if uploaded_file is not None:
       df = pd.read_csv(uploaded_file)
       st.subheader("Perform Hypothesis Testing")
       columns = df.columns.tolist()
    

       from scipy.stats import ttest_ind, ttest_1samp, f_oneway

       tests = {'One Way Sample t-test':ttest_1samp,
             'Two Sample t-test':ttest_ind,
             'Oneway ANOVA':f_oneway}
       test = [ttest_ind, ttest_1samp, f_oneway]

       selected_test = st.selectbox("Select Type of Test", tests)

       if selected_test == 'One Way Sample t-test':
           x = st.selectbox("Select Attribute 1", columns)
           y = st.number_input("Enter the specified value: ")
           t_stat, p_value = ttest_1samp(df[x], y)
        
       elif selected_test == 'Oneway ANOVA':
             x = st.selectbox("Select Attribute 1", columns)
             y = st.selectbox("Select Attribute 2", columns)
             z = st.selectbox("Select Attribute 3", columns)
             t_stat, p_value = f_oneway(df[x], df[y], df[z])
       else:
            x = st.selectbox("Select Attribute 1", columns)
            y = st.selectbox("Select Attribute 2", columns)
            t_stat, p_value = ttest_ind(df[x], df[y])


       alpha = st.selectbox("Select Alpha", [0.05, 0.01, 0.025])


       st.subheader("Significance Interpretation")
       st.write(f"t-statistic: {t_stat}, p-value: {p_value}")


       if st.button("Generate Results"): 
          if alpha < p_value:
             st.write("Reject the null hypothesis: The means are significantly different.")
          else:
             st.write("Fail to reject the null hypothesis: The means are not significantly different. ")
       else:
            st.write("Press button to generate results...")
   




