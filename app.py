import streamlit as st
import pandas as pd
from io import BytesIO
from generate_reports import process_data, generate_suggestions
from visuals import generate_visuals

st.set_page_config(page_title="📊 Auto-Fin Report Generator")

st.title("📊 Auto-Fin – Automated Financial Reporting")
st.write("Upload your Excel file using our template to get instant reports, visuals, and smart suggestions.")

# Excel template download button
with open("template.xlsx", "rb") as file:
    st.download_button("📥 Download Excel Template", file, file_name="template.xlsx")

# File upload section
uploaded_file = st.file_uploader("📤 Upload Your Excel File", type=["xlsx"])

if uploaded_file:
    try:
        df = pd.read_excel(uploaded_file)

        required_cols = ['Date', 'Description', 'Category', 'Sub-Category', 'Amount', 'Payment Method']
        if not all(col in df.columns for col in required_cols):
            st.error("❌ Your file must follow the provided template format.")
        else:
            # Process and summarize the data
            report_df = process_data(df)

            # Generate downloadable Excel report
            output = BytesIO()
            with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
                report_df.to_excel(writer, index=False, sheet_name="Summary")

            st.download_button("📄 Download Report", output.getvalue(), file_name="auto-fin-report.xlsx")

            # Show visuals
            st.subheader("📊 Your Data Insights")
            generate_visuals(df)

            # Show AI suggestions
            st.subheader("🤖 Auto-Fin Suggestions")
            for tip in generate_suggestions(df):
                st.info(tip)

    except Exception as e:
        st.error(f"❌ Error processing file: {e}")
