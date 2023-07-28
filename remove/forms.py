from django import forms

class PDFUploadForm(forms.Form):
    pdf_file = forms.FileField()
    page_numbers = forms.CharField(help_text="Enter page numbers to remove (comma-separated)")
