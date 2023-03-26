import pandas as pd
import plotly.express as px
import streamlit as st

with st.sidebar:
      X = st.selectbox(
      'X',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'))
      Y = st.selectbox(
      'Y',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'))
      Size = st.selectbox(
      'Size',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'))
      Color = st.selectbox(
      'Color',
      ('  GDP per capita ', ' Life expectancy at birth', '  Population ',' Birth rate'))
      Circle_area = st.slider('Circle Area', 0, 100, 60)

      st.write('X:', X)
      st.write('Y:', Y)
      st.write('Size:', Size)
      st.write('Color:', Color)
      st.write("Circle Area:", Circle_area)

Data = pd.read_csv("factbook.csv")

fig = px.scatter(data_frame=Data,x=X, y=Y,size =Size,color=Color,log_x=True,log_y=True,size_max=Circle_area)

st.plotly_chart(fig, theme="streamlit", use_container_width=True)
