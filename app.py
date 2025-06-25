import streamlit as st
import pandas as pd
from io import BytesIO
from generate_reports import process_data, generate_suggestions
from visuals import generate_visuals

st.set_page_config(page_title="Auto-Fin Report Generator")

st.title("Auto-Fin – Automated Financial Reporting")
st.write("Upload your Excel file using our template to get instant reports, visuals, and smart suggestions.")

# Template download button
with open("template.xlsx", "rb") as file:
    st.download_button(" Download Excel Template", file, file_name="template.xlsx")

# File upload
uploaded_file = st.file_uploader(" Upload Your Excel File", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        required_cols = ['Date', 'Description', 'Category', 'Sub-Category', 'Amount', 'Payment Method']
        if not all(col in df.columns for col in required_cols):
            st.error(" Your file must follow the provided template format.")
        else:
            # Process data into all 4 report parts
            pnl_df, balance_df, summary_df, suggestions_df = process_data(df)

            # Create downloadable multi-sheet Excel file
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                pnl_df.to_excel(writer, index=False, sheet_name="P&L")
                balance_df.to_excel(writer, index=False, sheet_name="Balance Sheet")
                summary_df.to_excel(writer, index=False, sheet_name="Summary")
                suggestions_df.to_excel(writer, index=False, sheet_name="Auto-Fin Tips")
            output.seek(0)

            st.download_button(" Download Full Report (Excel)", output.getvalue(), file_name="auto-fin-report.xlsx")

            # Show visuals
            st.subheader(" Your Data Insights")
            generate_visuals(df)

            # Show GPT-style financial suggestions
            st.subheader(" Auto-Fin Suggestions")
