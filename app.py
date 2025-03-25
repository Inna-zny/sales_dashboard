
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Интерактивный дашборд продаж', layout='wide')
st.title('📊 Дашборд по продажам за март')

data = pd.read_csv('combined_data_for_pbi.csv')

with st.sidebar:
    st.header('Фильтры')
    channels = st.multiselect('Канал', data['Канал'].unique(), default=data['Канал'].unique())
    start_date = st.date_input('Дата с', pd.to_datetime(data['Дата']).min())
    end_date = st.date_input('Дата по', pd.to_datetime(data['Дата']).max())

filtered_data = data[(data['Канал'].isin(channels)) &
                     (pd.to_datetime(data['Дата']) >= pd.to_datetime(start_date)) &
                     (pd.to_datetime(data['Дата']) <= pd.to_datetime(end_date))]

st.subheader('KPI')
st.metric('Общая сумма продаж', f"{filtered_data['Сумма'].sum():,.0f} руб")
st.metric('Конверсия', f"{filtered_data['Конверсия'].mean():.2%}")
st.metric('Средний чек', f"{filtered_data['Средний чек'].mean():,.0f} руб")


fig_sales = px.line(filtered_data, x='Дата', y='Сумма', color='Канал', title='Динамика суммы продаж')
st.plotly_chart(fig_sales, use_container_width=True)
