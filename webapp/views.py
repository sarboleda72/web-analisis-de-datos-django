from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd


# Create your views here.
    
def calculoMetricas():
    return {'decercion':'50%'}
def index(request):
    if request.method == 'POST' and request.FILES['excel']:
        excel = request.FILES['excel']
        fs =FileSystemStorage()
        filename= fs.save(excel.name, excel)  # Guarda el archivo en la carpeta de media
        uploaded_file_url=fs.url(filename)   # Genera una URL para acceder al archivo guardado
        return render(request, 'index.html', {'upload_file_url':uploaded_file_url})
    
    mensaje=calculoMetricas()
    return render(request, 'index.html', mensaje)
