import PyPDF2 as py
PdfFiles=["1.pdf","2.pdf"]
Merge=py.PdfMerger()
for filename in PdfFiles:
    PdfFile=open(filename,"rb")
    PdfReader=py.PdfReader(PdfFile)
    Merge.append(PdfReader)
PdfFile.close()
Merge.write("merged.pdf")

     #OR

# import PyPDF2 as py
#
# # List of PDF files to merge
# PdfFiles = ["1.pdf", "2.pdf"]s
#
# # Create a PdfMerger object
# Merge = py.PdfMerger()
#
# # Append each PDF file to the merger
# for filename in PdfFiles:
#     with open(filename, 'rb') as PdfFile:
#         PdfReader = py.PdfReader(PdfFile)
#         Merge.append(PdfReader)
#
# # Write the merged PDF to a new file
# with open("merged.pdf", 'wb') as output:
#     Merge.write(output)


