from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import pandas as pd
import os

# Create your views here.
def calculoNivelformacion(nivelFormacion,estadoAprendiz):
    tecnicosDesertados=0
    tecnologosDesertados=0
    totalTecnicos=0
    totalTecnologos=0

    for formacion,estado in zip(nivelFormacion,estadoAprendiz):
        totalTecnicos += 1 if formacion=='TÉCNICO' else 0
        totalTecnologos += 1 if formacion=='TECNÓLOGO' else 0

        if estado=='Cancelado' or estado=='Retiro voluntario':
            tecnicosDesertados+= 1 if formacion=='TÉCNICO' else 0
            tecnologosDesertados+= 1 if formacion=='TECNÓLOGO' else 0

    totalDesertados=tecnicosDesertados+tecnologosDesertados
    porcentajeTecnicos=round(tecnicosDesertados*100/totalDesertados,2)
    porcentajeTecnologos=round(tecnologosDesertados*100/totalDesertados,2)
        
    
    return {'totalDesertados':totalDesertados,'totalTecnicos':totalTecnicos,'tecnicosDesertados':tecnicosDesertados,'totalTecnologos':totalTecnologos,'tecnologosDesertados':tecnologosDesertados,'porcentajes':[porcentajeTecnicos,porcentajeTecnologos]}

def calculoHombresvsMujeres(hombresDesertados,mujeresDesertadas):
    totalDesertados=hombresDesertados+mujeresDesertadas
    porcentajeHombres=round(hombresDesertados*100/totalDesertados,2)
    porcentajeMujeres=round(mujeresDesertadas*100/totalDesertados,2)

    return [porcentajeHombres,porcentajeMujeres]

def calculoMujeres(generos,estadoAprendiz):
    mujeresDesertados=0
    totalMujeres=0

    for genero,estado in zip(generos,estadoAprendiz):
        
        totalMujeres += 1 if genero=='F' else 0
        if estado=='Cancelado' or estado=='Retiro voluntario':
            mujeresDesertados+= 1 if genero=='F' else 0
    
    return {'totalMujeres':totalMujeres,'mujeresDesertados':mujeresDesertados}
def calculoHombres(generos,estadoAprendiz):
    hombresDesertados=0
    totalHombres=0

    for genero,estado in zip(generos,estadoAprendiz):
        
        totalHombres += 1 if genero=='M' else 0
        if estado=='Cancelado' or estado=='Retiro voluntario':
            hombresDesertados+= 1 if genero=='M' else 0
    
    return {'totalHombres':totalHombres,'hombresDesertados':hombresDesertados}

def calculoFrecuenciaMeses(fechaRetiro, estadoAprendiz):
    meses=[0,0,0,0,0,0,0,0,0,0,0,0]
    
    for fecha,estado in zip(fechaRetiro,estadoAprendiz):
        
        if estado=='Cancelado' or estado=='Retiro voluntario':
            fecha=fecha.split("-")
            mes = fecha[1]
            if mes=="01":
                meses[0]+=1
            elif mes=="02":
                meses[1]+=1
            elif mes=="03":
                meses[2]+=1
            elif mes=="04":
                meses[3]+=1
            elif mes=="05":
                meses[4]+=1
            elif mes=="06":
                meses[5]+=1
            elif mes=="07":
                meses[6]+=1
            elif mes=="08":
                meses[7]+=1
            elif mes=="09":
                meses[8]+=1
            elif mes=="10":
                meses[9]+=1
            elif mes=="11":
                meses[10]+=1
            elif mes=="12":
                meses[11]+=1
    return  meses

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

def calculoEdad(tipoDocumento,estadoAprendiz,edaAprendiz):
    adulto = 0
    joven = 0
    adolescente = 0
    for tipoDocumento,estado,edad in zip(tipoDocumento,estadoAprendiz,edaAprendiz):
        if estado=='Cancelado' or estado=='Retiro voluntario':
            adulto += 1 if edad>=29 and edad<=59 else 0
            joven += 1 if edad>=19 and edad<=28 else 0
            if tipoDocumento=='TI':
                adolescente += 1 if edad<=18 else 0

    return [adulto,joven,adolescente]

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
        edad=calculoEdad(df['TIPO_DOCUMENTO'],df['ESTADO_APRENDIZ'],df['EDAD'])
        carreraTecnologica=calculoCarreraTecnologica(df['PROGRAMA'],df['ESTADO_APRENDIZ'])
        frecuenciaMeses=calculoFrecuenciaMeses(df['FECHA_RETIRO'],df['ESTADO_APRENDIZ'])
        hombres=calculoHombres(df['GENERO'],df['ESTADO_APRENDIZ'])
        mujeres=calculoMujeres(df['GENERO'],df['ESTADO_APRENDIZ'])
        hombresvsMujeres=calculoHombresvsMujeres(hombres['totalHombres'],mujeres['totalMujeres'])
        nivelFormacion=calculoNivelformacion(df['NIVEL_DE_FORMACION'],df['ESTADO_APRENDIZ'])

        mensaje={
            'desercion':desercion,
            'factor':factor,
            'edad':edad,
            'tecnologica':carreraTecnologica,
            'frecuencia':frecuenciaMeses,
            'hombres':hombres,
            'mujeres':mujeres,
            'hvM':hombresvsMujeres,
            'nivelFormacion':nivelFormacion,
            'porcentajeFormacion':nivelFormacion['porcentajes']
        }
        return render(request, 'index.html',mensaje)
    
    return render(request, 'index.html')
