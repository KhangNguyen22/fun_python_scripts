from docx import Document
from docx.shared import Inches, Pt
import re

def set_col_widths(table):
    widths = (Inches(1), Inches(20))
    for row in table.rows:
        for idx, width in enumerate(widths):
            row.cells[idx].width = width

document = Document()

style = document.styles['Normal']
font = style.font
font.name = 'Calibri'
font.size = Pt(16)

table = document.add_table(rows=2, cols=2)
table.style = 'Table Grid'
set_col_widths(table)

hdr_cells = table.rows[0].cells[0]
hdr_cells.text = 'L1: Consolidation and the concept of control'
table.rows[0].cells[0].paragraphs[0].runs[0].font.bold = True


file = open('/Users/khang248123/Desktop/l.txt',mode='r')
text = file.read() 
mo = re.compile(r'Page (\d|\d\d)\n\n\s([\w\W]+?)\n([\w\W]+?)(?=The University of Sydney)')
array = mo.findall(text)
for idx,i in enumerate(array):
    print(idx)
    print(i)

# print(repr(text))
# bold the left column
# table.rows[1].cells[0].paragraphs[0].runs[0].font.bold = True

# if document.save('demo.docx'):
#     print("saved")