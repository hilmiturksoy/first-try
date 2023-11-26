from pdf2docx import Converter

pdf_file = 'family-visit-checklist-mar-2022.pdf'
docx_file = 'family-visit-checklist-mar-2022.docx'

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()