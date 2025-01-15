#Read reports from the JSON file and generate a PDF file from them

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors


#Generate pdf based on a given filename, title, body text, and table data
def generatePDF(filename, title, body_text, table_data):
    report = SimpleDocTemplate(filename)
    #get styles from style sheet
    styles = getSampleStyleSheet()
    #Create a title with h1 header style
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(body_text, styles["BodyText"])

    #This table style was provided by Google for purposes of this exercise
    table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
    report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
    empty_line = Spacer(1,20)
    report.build([report_title, empty_line, report_info, empty_line, report_table])


