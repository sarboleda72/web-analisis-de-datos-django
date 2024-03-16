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

def calculoCarreraTecnologica(carrerasTecnologicas,estadoAprendiz):
    adso=0
    aniDig=0
    autSisMec=0
    desProEle=0
    desSisEleind=0
    disIntAutMec=0
    gesProInd=0
    gesIntTra=0
    impInfTecInfCom=0
    impRedSerTel=0
    manEquBio=0
    proComMecMaqCNC=0
    for carrera,estado in zip(carrerasTecnologicas,estadoAprendiz):
        if estado=='Cancelado' or estado=='Retiro voluntario':
            if carrera=='ANALISIS Y DESARROLLO DE SOFTWARE.':
                adso+=1
            elif carrera=='ANIMACION DIGITAL':
                aniDig+=1
            elif carrera=='AUTOMATIZACION DE SISTEMAS MECATRONICOS':
                autSisMec+=1
            elif carrera=='DESARROLLO DE PRODUCTOS ELECTRONICOS':
                desProEle+=1
            elif carrera=='DESARROLLO DE SISTEMAS ELECTRONICOS INDUSTRIALES':
                desSisEleind+=1;  
            elif carrera=='DISEÑO E INTEGRACIÓN DE AUTOMATISMOS MECATRÓNICOS':
                disIntAutMec+=1
            elif carrera=='GESTIÓN DE LA PRODUCCIÓN INDUSTRIAL':
                gesProInd+=1
            elif carrera=='GESTION INTEGRAL DEL TRANSPORTE':
                gesIntTra+=1
            elif carrera=='IMPLEMENTACION DE INFRAESTRUCTURA DE TECNOLOGIAS DE LA INFORMACION Y LAS COMUNICACIONES.':
                impInfTecInfCom+=1
            elif carrera=='IMPLEMENTACION DE REDES Y SERVICIOS DE TELECOMUNICACIONES':
                impRedSerTel+=1
            elif carrera=='MANTENIMIENTO DE EQUIPO BIOMÉDICO':
                manEquBio+=1
            elif carrera=='PRODUCCION DE COMPONENTES MECANICOS CON MAQUINAS DE CONTROL NUMERICO COMPUTARIZADO':
                proComMecMaqCNC+=1
    
    return [adso,aniDig,autSisMec,desProEle,desSisEleind,disIntAutMec,gesProInd,gesIntTra,impInfTecInfCom,impRedSerTel,manEquBio,proComMecMaqCNC]

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
        carreraTecnologica=calculoCarreraTecnologica(df['PROGRAMA'],df['ESTADO_APRENDIZ'])
        
        mensaje={
            'desercion':desercion,
            'factor':factor,
            'edad':edad,
            'tecnologica':carreraTecnologica
        }
        return render(request, 'index.html',mensaje)
    
    return render(request, 'index.html')
