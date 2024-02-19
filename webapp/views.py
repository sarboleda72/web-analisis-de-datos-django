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

def calculoFactor(factorAprendiz,estadoAprendiz):
    problemasPersonales=0
    dificultadesEconomicas=0
    faltaDeInteres=0
    faltaApoyoEconomico=0
    oportunidadesLaborales=0
    
    for factor,estado in zip(factorAprendiz,estadoAprendiz):
        if estado=='Cancelado' or estado=='Retiro voluntario':
            if factor== 'Problemas personales / familiares':
                problemasPersonales+=1
            elif factor == 'Dificultades económicas' :
                dificultadesEconomicas += 1
            elif factor == 'Falta de interés en el programa de formación':
                faltaDeInteres += 1
            elif factor == 'Falta de apoyo académico':
                faltaApoyoEconomico += 1
            elif factor == 'Oportunidades laborales externas':
                oportunidadesLaborales+=1
    
    return [dificultadesEconomicas,problemasPersonales,faltaDeInteres,faltaApoyoEconomico,oportunidadesLaborales]

def calculoEdad(tipoDocumento,estadoAprendiz):
    mayorEdad=0
    menorEdad=0
    for tipoDocumento,estado in zip(tipoDocumento,estadoAprendiz):
        if estado=='Cancelado' or estado=='Retiro voluntario':
            if tipoDocumento== 'CC' or tipoDocumento== 'CE' or tipoDocumento== 'PPT' :
                mayorEdad+=1
            elif tipoDocumento == 'TI':
                menorEdad += 1
    return [mayorEdad,menorEdad]

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
        
        #Llamado de funciones que calculan las metricas
        desercion=calculoDesercion(df['ESTADO_APRENDIZ'])
        factor=calculoFactor(df['FACTORES'],df['ESTADO_APRENDIZ'])
        edad=calculoEdad(df['TIPO_DOCUMENTO'],df['ESTADO_APRENDIZ'])
        
        mensaje={
            'desercion':desercion,
            'factor':factor,
            'edad':edad
        }
        return render(request, 'index.html',mensaje)
    
    return render(request, 'index.html')
