import pandas as pd

def process_data(df):
    df['Net Amount'] = df['Amount'] * 0.9
    summary = df.groupby('Description')['Net Amount'].sum().reset_index()
    summary.columns = ['Category', 'Total']
    return summary

def generate_suggestions(df):
    tips = []
    total = df['Amount'].sum()
    avg = df['Amount'].mean()

    if total > 100000:
        tips.append("💡 High total spending – consider reviewing big transactions.")
    if 'Loan' in df['Description'].values:
        tips.append("📌 You have loan entries – track your repayment plan.")
    if avg > 5000:
        tips.append("📊 Average transaction is high – batch or categorize expenses better.")
    if df['Amount'].min() < 0:
        tips.append("⚠️ Negative values found – verify if these are refunds or errors.")
    return tips
