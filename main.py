from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv('topics.csv')

for index, rows in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', size=24, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=rows['Topic'], align='L', ln=1)

    for i in range(21, 282, 10):
        pdf.line(10, i, 200, i)

    pdf.ln(265)
    pdf.set_font(family='Times', size=8, style='I')
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=rows['Topic'], align='R')

    for j in range(rows['Pages'] - 1):
        pdf.add_page()

        for r in range(21, 282, 10):
            pdf.line(10, r, 200, r)

        pdf.ln(277)
        pdf.set_font(family='Times', size=8, style='I')
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=rows['Topic'], align='R')

pdf.output('output.pdf')

