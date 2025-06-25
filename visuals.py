import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def generate_visuals(df):
    st.write(" Revenue vs Expense Overview")

    revenue = df[df["Category"] == "Revenue"]
    expense = df[df["Category"] == "Expense"]

    rev_total = revenue.groupby("Sub-Category")["Amount"].sum()
    exp_total = expense.groupby("Sub-Category")["Amount"].sum()

    # Revenue Pie Chart
    fig1, ax1 = plt.subplots()
    ax1.pie(rev_total, labels=rev_total.index, autopct='%1.1f%%', startangle=90)
    ax1.axis('equal')
    st.pyplot(fig1, use_container_width=True)
    st.caption(" Revenue Breakdown by Sub-Category")

    # Expense Bar Chart
    st.write("###  Top 5 Expenses")
    top_exp = exp_total.sort_values(ascending=False).head(5)
    fig2, ax2 = plt.subplots()
    ax2.bar(top_exp.index, top_exp.values, color='orange')
    plt.xticks(rotation=45)
    st.pyplot(fig2, use_container_width=True)
    st.caption(" Focus on your top spending areas.")
