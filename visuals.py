import streamlit as st
import plotly.express as px

def generate_visuals(df):
    # Total by Category
    cat_chart = px.bar(df.groupby('Category')['Amount'].sum().reset_index(),
                       x='Category', y='Amount', title='Total by Category')
    st.plotly_chart(cat_chart)

    # Pie chart by Payment Method
    payment_chart = px.pie(df, names='Payment Method', values='Amount', title='Payments Breakdown')
    st.plotly_chart(payment_chart)
