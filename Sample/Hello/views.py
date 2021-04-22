from django.http import HttpResponse
from django.shortcuts import render

# Create Your Views 
def show(request):
    return HttpResponse("<h1>Hello My Name Is Achal Gohade <br>My PRN Is 1841018</h1>")
