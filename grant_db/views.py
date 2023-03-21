from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from .models import Book
from .serializers import BookSerializer

# import io
# from django.http import FileResponse
# from reportlab.pdfgen import canvas

# Create your views here.


# @staff_member_required
# def generatePDF(request, id):
#     buffer = io.BytesIO()
#     x = canvas.Canvas(buffer)
#     x.drawString(100, 100, "Let's generate this pdf file.")
#     x.showPage()
#     x.save()
#     buffer.seek(0)
#     return FileResponse(buffer, as_attachment=True, filename='attempt1.pdf')

def firstFunction(request):
    return render(request, 'first_app_temp.html', {'data': 'Something'})


class DjangoSolution(View):
    books_obj = Book.objects.all()
    output = ''

    for i, book in enumerate(books_obj):
        output += f"{i + 1}. {book.title}\n"

    def get(self, request):
        return render(request, 'first_app_temp.html', {'data': f"We have the following books in our Grant DB:\n" + self.output})


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    authentication_classes = (TokenAuthentication,)