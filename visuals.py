import streamlit as st
import plotly.express as px

def generate_visuals(df):
    fig = px.bar(df.groupby('Description')['Amount'].sum().reset_index(),
                 x='Description', y='Amount', title='Spending by Category')
    st.plotly_chart(fig)

    fig2 = px.pie(df, names='Description', values='Amount', title='Category Distribution')
    st.plotly_chart(fig2)
