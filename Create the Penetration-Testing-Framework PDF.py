from fpdf import FPDF

# Function to create a basic PDF
def create_pdf(title, content, filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.set_font("Arial", '', 12)
    pdf.ln(10)
    pdf.multi_cell(0, 10, txt=content)
    pdf.output(filename)

# Create the Penetration-Testing-Framework PDF
ptf_title = "Penetration Testing Framework"
ptf_content = """
This document outlines the structure and methodology of the custom Penetration Testing Framework.

Components:
- Reconnaissance Modules
- Scanning & Enumeration Tools
- Exploitation Scripts
- Reporting System

Usage:
Each module can be run independently or chained together for automated workflows.
"""
create_pdf(ptf_title, ptf_content, "Penetration-Testing-Framework.pdf")

# Create the Vulnerability Assessment Tool PDF
vat_title = "Vulnerability Assessment Tool Documentation"
vat_content = """
This document provides details on how to use the custom Vulnerability Assessment Tool.

Features:
- Port Scanning
- Vulnerability Enumeration
- Risk Scoring System

Usage Instructions:
1. Configure the scan targets.
2. Execute the tool using the CLI.
3. Review the generated reports in the /sample_scans directory.
"""
create_pdf(vat_title, vat_content, "Vulnerability-Assessment-Tool.pdf")

# Create sample scan result PDF
sample_scan_title = "Sample Vulnerability Assessment Report"
sample_scan_content = """
Target: 192.168.1.100
Scan Type: Full TCP Scan

Findings:
- Port 22 open (SSH) - no issues found
- Port 80 open (HTTP) - outdated Apache version (2.2.15)
- Port 139/445 open - SMBv1 enabled (vulnerable)

Recommendations:
- Disable SMBv1
- Update Apache to latest version
"""
create_pdf(sample_scan_title, sample_scan_content, "Vulnerability-Assessment-Tool-Sample.pdf")
