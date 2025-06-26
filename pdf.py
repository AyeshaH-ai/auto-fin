import streamlit as st
import pandas as pd
from visuals import net_profit_chart
from fpdf import FPDF
from io import BytesIO

# App title
st.title(" Automated Financial Report App")

# File uploader
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])
if uploaded_file:
    data = pd.read_excel(uploaded_file)

    # Show chart
    st.subheader("Net Profit Chart")
    fig = net_profit_chart(data)
    st.pyplot(fig)

    # Recommendations (customize this logic!)
    st.subheader(" Recommendations")
    recommendations = """
    • Expenses increased in the last quarter.  
    • Revenue growth has slowed — consider sales strategies.  
    • Operational costs are above budget.
    """
    st.markdown(recommendations)

    # Save chart to memory
    img_buf = BytesIO()
    fig.savefig(img_buf, format='PNG')
    img_buf.seek(0)

    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, " Financial Report Summary", ln=True, align="C")

    with open("temp_chart.png", "wb") as f:
        f.write(img_buf.read())
    pdf.image("temp_chart.png", x=10, y=30, w=180)
    pdf.ln(105)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(0, 10, " Recommendations", ln=True)
    pdf.set_font("Arial", '', 12)
    for line in recommendations.strip().split('\n'):
        pdf.multi_cell(0, 8, line)

    # Save PDF to memory
    pdf_buf = BytesIO()
    pdf.output(pdf_buf)
    pdf_buf.seek(0)

    # Download button
    st.download_button(" Download Report (PDF)", data=pdf_buf, file_name="financial_report.pdf", mime="application/pdf")
