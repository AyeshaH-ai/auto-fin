import pandas as pd

def process_data(df):
    # Split categories
    pnl_df = df[df['Category'].isin(['Revenue', 'Expense'])]
    balance_df = df[df['Category'].isin(['Asset', 'Liability'])]

    # Summary calculations
    total_revenue = pnl_df[pnl_df['Category'] == 'Revenue']['Amount'].sum()
    total_expense = pnl_df[pnl_df['Category'] == 'Expense']['Amount'].sum()
    net_profit = total_revenue - total_expense

    total_assets = balance_df[balance_df['Category'] == 'Asset']['Amount'].sum()
    total_liabilities = balance_df[balance_df['Category'] == 'Liability']['Amount'].sum()
    net_assets = total_assets + total_liabilities  # Liabilities already negative

    summary_df = pd.DataFrame({
        "Metric": ["Total Revenue", "Total Expense", "Net Profit", "Total Assets", "Total Liabilities", "Net Assets"],
        "Amount": [total_revenue, total_expense, net_profit, total_assets, total_liabilities, net_assets]
    })

    return pnl_df, balance_df, summary_df

