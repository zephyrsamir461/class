import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd
import scipy.stats as stats

st.title(" :bar_chart: Sample Electronic Store EDA")
df=pd.read_csv('online_store_data.csv')

total_sales_per_product = df.groupby('Product')['Total_Sale'].sum().reset_index()
st.title(" :bar_chart: Sample Electronic Store EDA")
px.bar(total_sales_per_product, x = 'Product', y = 'Total_Sale')
