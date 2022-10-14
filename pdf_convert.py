from fpdf import FPDF



def pdfConvert(path, filename):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size = 15)


    with open(path, 'r', encoding= 'utf-8') as f1:
    
        for l1 in f1:
            pdf.cell(200, 10, txt = l1, ln = 1, align = 'L') 

        pdf.output(filename + ".pdf")
   
   


