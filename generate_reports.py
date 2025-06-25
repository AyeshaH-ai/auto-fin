import pandas as pd

def process_data(df):
    # Split categories for different report types
    pnl_df = df[df['Category'].isin(['Revenue', 'Expense'])]             # Profit & Loss
    balance_df = df[df['Category'].isin(['Asset', 'Liability'])]        # Balance Sheet

    # Summary metrics
    total_revenue = pnl_df[pnl_df['Category'] == 'Revenue']['Amount'].sum()
    total_expense = pnl_df[pnl_df['Category'] == 'Expense']['Amount'].sum()
    net_profit = total_revenue - total_expense

    total_assets = balance_df[balance_df['Category'] == 'Asset']['Amount'].sum()
    total_liabilities = balance_df[balance_df['Category'] == 'Liability']['Amount'].sum()
    net_assets = total_assets + total_liabilities

    summary_df = pd.DataFrame({
        "Metric": [
            "Total Revenue", "Total Expense", "Net Profit",
            "Total Assets", "Total Liabilities", "Net Assets"
        ],
        "Amount": [
            total_revenue, total_expense, net_profit,
            total_assets, total_liabilities, net_assets
        ]
    })

    # AI Suggestions in a separate sheet
    suggestions = generate_suggestions(df)
    suggestions_df = pd.DataFrame({'Auto-Fin Suggestions': suggestions})

    return pnl_df, balance_df, summary_df, suggestions_df

def generate_suggestions(df):
    suggestions = []

    revenue = df[df['Category'] == 'Revenue']['Amount'].sum()
    expense = df[df['Category'] == 'Expense']['Amount'].sum()
    net_profit = revenue - expense

    # Net profit check
    if net_profit > 0:
        suggestions.append("✅ Your business is profitable. Great job!")
    else:
        suggestions.append("⚠️ Your expenses exceed revenue. Consider reducing costs.")

    # Salary ratio check
    salaries = df[df['Sub-Category'].str.lower().str.contains("salaries")]['Amount'].sum()
    if salaries > 0.3 * expense:
        suggestions.append(" Salaries are more than 30% of your total expenses. Consider reviewing salary structure.")

    # Rent ratio check
    rent = df[df['Sub-Category'].str.lower().str.contains("rent")]['Amount'].sum()
    if rent > 0.2 * expense:
        suggestions.append(" Rent is a large part of your expenses. Could you switch to a smaller or remote space?")

    return suggestions

   
     
