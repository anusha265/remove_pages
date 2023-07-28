from django.shortcuts import render
from PyPDF2 import PdfWriter, PdfReader
import io
from .forms import PDFUploadForm
from django.http import HttpResponse
def remove_pages(request):
    if request.method == 'POST':
        form = PDFUploadForm(request.POST, request.FILES)
        if form.is_valid():
            pdf_file = request.FILES['pdf_file']
            page_numbers = form.cleaned_data['page_numbers'].split(',')
            # Read the uploaded PDF file
            pdf_reader = PdfReader(pdf_file)
            pdf_writer = PdfWriter()
            # Copy pages from the input PDF to the output PDF except for the specified page numbers
            for page_number in range(len(pdf_reader.pages)):
                if str(page_number + 1) not in page_numbers:
                    pdf_writer.add_page(pdf_reader.pages[page_number])
            # Create an in-memory PDF file to store the modified PDF
            output_pdf = io.BytesIO()
            pdf_writer.write(output_pdf)
            output_pdf.seek(0)
            # Set the appropriate response headers
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="modified_pdf.pdf"'
            # Send the modified PDF file as the response
            response.write(output_pdf.getvalue())
            return response
    else:
        form = PDFUploadForm()
    return render(request, 'remove/remove_pages.html', {'form': form})