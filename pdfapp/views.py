from reportlab.pdfgen import canvas
from django.http import HttpResponse


def getpdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'
    p = canvas.Canvas(response)
    p.setFont("Times-Roman", 13)
    p.drawString(70, 780, "Hello, Shahed Mohammad Hridoy")
    p.showPage()
    p.drawString(70, 780, "Hello, Shahed Mohammad Hridoy")
    p.showPage()
    p.drawString(70, 780, "Hello, Shahed Mohammad Hridoy")
    p.showPage()
    p.save()
    return response