import PyPDF2

pdfs = ["MEGHANA V_SIT_ISE.pdf","Vikram_SIT_CSE(AIML).pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfs:
    pdfFile = open(filename,'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write("merged.pdf")