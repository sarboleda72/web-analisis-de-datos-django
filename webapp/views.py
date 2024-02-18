from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os


# Create your views here.
    
def calculoDesercion(estadoAprendiz):
    cancelado=0
    retiroVoluntario=0
    for estado in estadoAprendiz:
        if estado=='Cancelado':
            cancelado+=1
        if estado=='Retiro voluntario':
            retiroVoluntario+=1
    porcentajeDesercion= ((cancelado+retiroVoluntario)/len(estadoAprendiz))*100
    porcentajeDesercion= str(round(porcentajeDesercion,2))+'%'
    return {'desertados':porcentajeDesercion,'total':len(estadoAprendiz),'cancelado':cancelado,'retirado':retiroVoluntario}

def index(request):
    if request.method == 'POST' and request.FILES['excel']:
        excel = request.FILES['excel']
        fs =FileSystemStorage()
        if fs.exists('db.xlsx'):
            fs.delete('db.xlsx')
        filename= fs.save('db.xlsx', excel)  # Guarda el archivo en la carpeta de media
        uploaded_file_url=fs.url(filename)   # Genera una URL para acceder al archivo guardado
        ruta_archivo = os.path.join(settings.MEDIA_ROOT, filename)#captura ruta interna
        #captura pandas
        df = pd.read_excel(ruta_archivo)
        desercion=calculoDesercion(df['ESTADO_APRENDIZ'])
        
        mensaje={
            'desercion':desercion
        }
        return render(request, 'index.html',mensaje)
    
    return render(request, 'index.html')
