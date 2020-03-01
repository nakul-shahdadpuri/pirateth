from fpdf import FPDF

pdf = FPDF()

print("Enter the name of the directory to be pdfyised - ")
name = input()
print("Enter the size of document - ")
num = int(input())

for i in range(1,num+1):
	pdf.add_page()
	pdf.image(name + "/"+ str(i) +".jpeg",5,5,200,270)

pdf.output(name + '/' + name +".pdf","F")