import pandas as pd

def process_data(df):
    # Group by Category and Sub-Category
    summary = df.groupby(['Category', 'Sub-Category'])['Amount'].sum().reset_index()
    summary.columns = ['Category', 'Sub-Category', 'Total Amount']
    return summary

def generate_suggestions(df):
    tips = []

    if df['Amount'].sum() > 100000:
        tips.append("💰 High total activity – monitor large expense and revenue flows.")
    
    if (df['Amount'] < 0).any():
        tips.append("⚠️ Negative values found – may indicate loans, overdrafts, or returns.")

    if df['Payment Method'].nunique() > 3:
        tips.append("📌 Multiple payment methods in use – consider consolidating for better tracking.")

    if 'Expense' in df['Category'].values:
        tips.append("📉 Expenses are recorded – analyze Cost of Goods Sold and overheads separately.")

    return tips
