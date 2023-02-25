from django.shortcuts import render
from .models import Book

def booklist(request):
  # books = ["igor ferreira"]
  # books = Book.objects.all()
  # Book.title = ['Testando', 'teste'] 
  # books = Book.objects.
  books = Book.objects.all()
  return render(request, 'booklist.html', {'books': books})
