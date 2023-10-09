import glob
import os
import math
import Turbinas

pathTurbinas='C:\\Users\\lench\\OneDrive - Estudiantes ITCR\TEC\\2022\\2do Semestre\\Liene\\Turbinas'
#pathTurbinas='C:\\Users\\lleival\\OneDrive - Estudiantes ITCR\\TEC\\2022\\2do Semestre\\Liene\\Turbinas'
#Potencia de las turbinas en Watts


class Estacion:
    def __init__(self,z1):
        
        self.lst2018=[]
        self.lst2019=[]
        self.lst2020=[]
        self.lst2021=[]
        self.lst2022=[]

        self.AEP18=[]                                           #Listas de AEP totales por año en cada estación
        self.AEP19=[]
        self.AEP20=[]
        self.AEP21=[]
        self.AEP22=[]
        
        self.monthsbyyear=[[],[],[],[],[]]                      #[0]=2018 [1]=2019 [2]=2020 [3]=2021 [4]=2022
        self.anualcheck=[False,False,False,False]
        self.z1=z1
        self.z0=2
        

Estaciones=[]

CIF=Estacion(14)
CEANA=Estacion(21)
Electromec=Estacion(10)
Planta=Estacion(12)
AEPlist=[]


def savelist(estacion,txt,file):

    if estacion == CIF:
        year1=4
        year2=6
    
    elif estacion == CEANA:
        year1=6
        year2=8

    elif estacion == Electromec:
        year1=11
        year2=13
    
    elif estacion == Planta:
        year1=7
        year2=9
        
    mnth1=year1+3
    mnth2=year2+3


    if txt[year1:year2]=='18':
                
        if not int(txt[year1:year2]) in estacion.monthsbyyear[0]:
            estacion.monthsbyyear[0].append(int(txt[mnth1:mnth2]))
        estacion.lst2018.append(file)
                

    elif txt[year1:year2]=='19':
        if not int(txt[mnth1:mnth2]) in estacion.monthsbyyear[1]:
            estacion.monthsbyyear[1].append(int(txt[mnth1:mnth2]))
        estacion.lst2019.append(file)


    elif txt[year1:year2]=='20':
        if not int(txt[mnth1:mnth2]) in estacion.monthsbyyear[2]:
            estacion.monthsbyyear[2].append(int(txt[mnth1:mnth2]))
        estacion.lst2020.append(file)


    elif txt[year1:year2]=='21':
        if not int(txt[mnth1:mnth2]) in estacion.monthsbyyear[3]:
            estacion.monthsbyyear[3].append(int(txt[mnth1:mnth2]))
        estacion.lst2021.append(file)


    elif txt[year1:year2]=='22':
        if not int(txt[mnth1:mnth2]) in estacion.monthsbyyear[4]:
            estacion.monthsbyyear[4].append(int(txt[mnth1:mnth2]))
        estacion.lst2022.append(file)



def importtxt (path):
    os.chdir(path)
    my_files = glob.glob('*.txt')
    return my_files



def genclass (path,filelist):
    for txt in filelist:
        
        if txt[0:3]=='CIF':
            file=readtxt(path+'\\'+txt,1)

            if not "CIF" in Estaciones:
                Estaciones.append("CIF")

            savelist(CIF,txt,file)


        elif txt[0:5]=="CEANA":
            file=readtxt(path+'\\'+txt,2)
            
            if not "CEANA" in Estaciones:
                Estaciones.append("CEANA")
            
            savelist(CEANA,txt,file)
            

        elif txt[0:10]=="Electromec":
            file=readtxt(path+'\\'+txt,3)

            if not "Electromec" in Estaciones:
                Estaciones.append("Electromec")

            savelist(Electromec,txt,file)

        elif txt[0:6]=="Planta":
            file=readtxt(path+'\\'+txt,4)

            if not "Planta" in Estaciones:
                Estaciones.append("Planta")

            savelist(Planta,txt,file)



def readtxt (txt,estacion):
    lista=[]
    with open(txt,'r') as f:
        lines = f.readlines()
    f.close()
    try:
        if estacion == 1 or estacion == 4:
            for linea in lines:
                if linea[21:len(linea)-1] != '':
                    lista.append([linea[1:20],float(linea[21:len(linea)-1])])
                else:
                    lista.append([linea[1:20],0.00])

        elif estacion == 2:
            for linea in lines:
                if linea[15:len(linea)-1] != '' and linea[15:len(linea)-1] != '--':
                    lista.append(['20'+linea[6:8]+'-'+linea[3:5]+'-'+linea[0:2]+' '+linea[9:14]+':00',float(linea[15:len(linea)-1])])
                else:
                    lista.append(['20'+linea[6:8]+'-'+linea[3:5]+'-'+linea[0:2]+' '+linea[9:14]+':00',0.00])

        elif estacion == 3:
            for linea in lines:
                if linea[20:len(linea)-1] != '':
                    lista.append([linea[0:19],float(linea[20:len(linea)-1])])
                else:
                    lista.append([linea[0:19],0.00])
                
        return lista
    except:
        print("error leyendo", txt)
   

def calculoVelocidad(z2,path):
    lnz2=math.log(z2/2)    
    for estacion in Estaciones:
        if estacion == "CIF":
            lnz1=math.log(CIF.z1/2)
            
            for mes in CIF.lst2018:
            
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CIF-"+mes[0][0][2:7]+".txt",mes)

            for mes in CIF.lst2019:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CIF-"+mes[0][0][2:7]+".txt",mes)

            for mes in CIF.lst2020:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CIF-"+mes[0][0][2:7]+".txt",mes)

            for mes in CIF.lst2021:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CIF-"+mes[0][0][2:7]+".txt",mes)

            for mes in CIF.lst2022:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CIF-"+mes[0][0][2:7]+".txt",mes)

        elif estacion == "CEANA":
            lnz1=math.log(CEANA.z1/2)

            for mes in CEANA.lst2018:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CEANA-"+mes[0][0][2:7]+".txt",mes)

            for mes in CEANA.lst2019:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CEANA-"+mes[0][0][2:7]+".txt",mes)

            for mes in CEANA.lst2020:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CEANA-"+mes[0][0][2:7]+".txt",mes)

            for mes in CEANA.lst2021:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CEANA-"+mes[0][0][2:7]+".txt",mes)

            for mes in CEANA.lst2022:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_CEANA-"+mes[0][0][2:7]+".txt",mes)


        elif estacion == "Electromec":
            lnz1=math.log(Electromec.z1/2)

            for mes in Electromec.lst2018:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Electromec-"+mes[0][0][2:7]+".txt",mes)

            for mes in Electromec.lst2019:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Electromec-"+mes[0][0][2:7]+".txt",mes)

            for mes in Electromec.lst2020:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Electromec-"+mes[0][0][2:7]+".txt",mes)

            for mes in Electromec.lst2021:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Electromec-"+mes[0][0][2:7]+".txt",mes)

            for mes in Electromec.lst2022:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Electromec-"+mes[0][0][2:7]+".txt",mes)

        elif estacion == "Planta":
            lnz1=math.log(Electromec.z1/2)

            for mes in Planta.lst2018:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Planta-"+mes[0][0][2:7]+".txt",mes)

            for mes in Planta.lst2019:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Planta-"+mes[0][0][2:7]+".txt",mes)

            for mes in Planta.lst2020:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Planta-"+mes[0][0][2:7]+".txt",mes)

            for mes in Planta.lst2021:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Planta-"+mes[0][0][2:7]+".txt",mes)

            for mes in Planta.lst2022:
                cicloVelocidad(mes,lnz1,lnz2)
                exporttxt(path+"New_Planta-"+mes[0][0][2:7]+".txt",mes)



def cicloVelocidad(listames, lnz1, lnz2):
    
    for dato in listames:
        dato[1]=dato[1]*(lnz2/lnz1)
    return listames



def exporttxt(path,list):
    with open(path, 'w') as fp:
        for elemento in list:
            fp.write(str(elemento[0])+"\t"+str(elemento[1])+"\n")
    fp.close()



def exportAEPtxt(path,list,turbinas):
    with open(path, 'w') as fp:
        for elemento in list:
            fp.write(str(elemento[0])+"\t"+str(turbinas[elemento[1]])+"\n")
    fp.close()



def exportPotencias(path,list):
    with open(path, 'w') as fp:
        for elemento in list:
            fp.write(elemento+"\n")
    fp.close()



def checkmonth(estacion,contadorEst):
    years=[]
    contador=0
    for year in estacion.monthsbyyear:
        if len(year)==12:
            contadorEst+=1
            years.append(contador)
            if contador ==0:
                print(contadorEst,"2018")
                AEPlist.append(estacion.lst2018)
            elif contador ==1:
                print(contadorEst,"2019")
                AEPlist.append(estacion.lst2019)
            elif contador ==2:
                print(contadorEst,"2020")
                AEPlist.append(estacion.lst2020)
            elif contador ==3:
                print(contadorEst,"2021")
                AEPlist.append(estacion.lst2021)
            elif contador ==4:
                print(contadorEst,"2022")
                AEPlist.append(estacion.lst2022)
        contador+=1
    
    if years == []:
        print("No hay datos suficientes para esta estación")

listaPotencias=[]

def calculoEnergia(mes):
    indice=1
    GeneracionMes=0                                     #KWh
    listaPotencias.append('Mes')
    gen=0
    for linea in mes:
        Potencia=Turbinas.interpolacion(linea[1])/1000  #kW
        listaPotencias.append(str(Potencia))
        #consumo=0
        if indice < len(mes):
            dia1=float(linea[0][8:10])
            dia2=float(mes[indice][0][8:10])
            hora1=float(linea[0][11:13])
            hora2=float(mes[indice][0][11:13])
            minuto1=float(linea[0][14:16])
            minuto2=float(mes[indice][0][14:16])
            segundo1=float(linea[0][17:19])
            segundo2=float(mes[indice][0][17:19])

            #print(hora1,hora2,minuto1,minuto2,segundo1,segundo2)
            if dia1==dia2:
                if hora1==hora2:
                    if minuto1==minuto2:
                        gen= (segundo2-segundo1) * Potencia / 3600
                        GeneracionMes+= gen
                    elif minuto2-minuto1==1:
                        gen= (segundo2+(60-segundo1)) * Potencia / 3600
                        GeneracionMes+= gen
                    else:
                        gen= (60*(minuto2-minuto1-1)+(segundo2+(60-segundo1))) * Potencia / 3600  
                        GeneracionMes+= gen
                        
                elif hora2-hora1==1:                   
                        gen= (60*(minuto2+(60-minuto1)-1)+(segundo2+(60-segundo1)))* Potencia / 3600
                        GeneracionMes+= gen        
                else:
                    gen= ((3600*(hora2-hora1-1))+60*(minuto2+(60-minuto1)-1)+(segundo2+(60-segundo1)))* Potencia / 3600
                    GeneracionMes+= gen
                    
            elif dia2-dia1==1:

                gen= ((3600*(hora2+(24-hora1-1)))+60*(minuto2+(60-minuto1)-1)+(segundo2+(60-segundo1)))* Potencia / 3600
                GeneracionMes+= gen
            else:
                gen= ((86400*(dia2-dia1-1))+(3600*(hora2+(24-hora1-1)))+60*(minuto2+(60-minuto1)-1)+(segundo2+(60-segundo1)))* Potencia / 3600
                GeneracionMes+= gen
                #print("AAAAAAAAA")

        #print(gen)
        indice+=1
        
    #print("mes",GeneracionMes)
    return GeneracionMes

                

def totalAEP (estacion,turbina):
        
    E18=0
    E19=0
    E20=0
    E21=0
    E22=0
          
    contadorEstacion=0
    if estacion.monthsbyyear[0]!=[]:                                            # Se podria limitar a los años que sólamente tengan datos en todos los 12 meses           
        for mes in estacion.lst2018:                                            # Ej: if estacion.monthsbyyear[0]==[12]:   
            contadorEstacion+=1
            E18+=calculoEnergia(mes)/len(estacion.monthsbyyear[0])*12
    estacion.AEP18.append([turbina,E18])
            
    if estacion.monthsbyyear[1]!=[]:
        for mes in estacion.lst2019:     
            contadorEstacion+=1   
            E19+=calculoEnergia(mes)/len(estacion.monthsbyyear[1])*12
    estacion.AEP19.append([turbina,E19])

    if estacion.monthsbyyear[2]!=[]:
        for mes in estacion.lst2020:        
            contadorEstacion+=1
            E20+=calculoEnergia(mes)/len(estacion.monthsbyyear[2])*12
    estacion.AEP20.append([turbina,E20])

    if estacion.monthsbyyear[3]!=[]:
        for mes in estacion.lst2021:        
            contadorEstacion+=1
            E21+=calculoEnergia(mes)/len(estacion.monthsbyyear[3])*12
    estacion.AEP21.append([turbina,E21])

    if estacion.monthsbyyear[4]!=[]:
        for mes in estacion.lst2022:        
            contadorEstacion+=1
            E22+=calculoEnergia(mes)/len(estacion.monthsbyyear[4])*12
    estacion.AEP22.append([turbina,E22])        



def maxAEP(estacion,turbinas,path):
    with open(path, 'w') as fp:
        
        if estacion.AEP18!=[]:
            Max18=max(estacion.AEP18)
            MaxTurbine18=estacion.AEP18.index(Max18)
            
            print("\t 2018:")
            fp.write("\t 2018:\n")
            if Max18!=0:
                print("\t Potencia máxima: ", Max18, "\t Turbina: ", turbinas[MaxTurbine18])
                fp.write("\t Potencia máxima: "+ str(Max18)+ "\t Turbina: "+ turbinas[MaxTurbine18]+"\n")
            else:
                print("\t Potencia máxima: ", Max18, "\t Turbina: ", "N/a")
                fp.write("\t Potencia máxima: "+ str(Max18)+ "\t Turbina: "+ "N/a\n")

        if estacion.AEP19!=[]:
            Max19=max(estacion.AEP19)
            print("\t 2019:")
            fp.write("\t 2019:\n")
            MaxTurbine19=estacion.AEP19.index(Max19)
            if Max19!=0:
                print("\t Potencia máxima: ", Max19, "\t Turbina: ", turbinas[MaxTurbine19])
                fp.write("\t Potencia máxima: "+ str(Max19)+ "\t Turbina: "+ turbinas[MaxTurbine19]+"\n")
            else:
                print("\t Potencia máxima: ", Max19, "\t Turbina: ", "N/a")
                fp.write("\t Potencia máxima: "+ str(Max19)+ "\t Turbina: "+ "N/a\n")

        if estacion.AEP20!=[]:
            Max20=max(estacion.AEP20)
            MaxTurbine20=estacion.AEP20.index(Max20)
            print("\t 2020:")
            fp.write("\t 2020:\n")
            if Max20!=0:
                print("\t Potencia máxima: ", Max20, "\t Turbina: ", turbinas[MaxTurbine20])
                fp.write("\t Potencia máxima: "+ str(Max20)+ "\t Turbina: "+ turbinas[MaxTurbine20]+"\n")
            else:
                print("\t Potencia máxima: ", Max20, "\t Turbina: ", "N/a")
                fp.write("\t Potencia máxima: "+ str(Max20)+ "\t Turbina: "+ "N/a\n")


        if estacion.AEP21!=[]:
            Max21=max(estacion.AEP21)
            MaxTurbine21=estacion.AEP21.index(Max21)
            print("\t 2021:")
            fp.write("\t 2021:\n")
            if Max21!=0:
                print("\t Potencia máxima: ", Max21, "\t Turbina: ", turbinas[MaxTurbine21])
                fp.write("\t Potencia máxima: "+ str(Max21)+ "\t Turbina: "+ turbinas[MaxTurbine21]+"\n")
            else:
                print("\t Potencia máxima: ", Max21, "\t Turbina: ", "N/a")
                fp.write("\t Potencia máxima: "+ str(Max21)+ "\t Turbina: "+ "N/a\n")


        if estacion.AEP22!=[]:
            Max22=max(estacion.AEP22)
            MaxTurbine22=estacion.AEP22.index(Max22)
            print("\t 2022:")
            fp.write("\t 2022:\n")
            if Max22!=0:
                print("\t Potencia máxima: ", Max22, "\t Turbina: ", turbinas[MaxTurbine22])
                fp.write("\t Potencia máxima: "+ str(Max22)+ "\t Turbina: "+ turbinas[MaxTurbine22]+"\n")
            else:
                print("\t Potencia máxima: ", Max22, "\t Turbina: ", "N/a")
                fp.write("\t Potencia máxima: "+ str(Max22)+ "\t Turbina: "+ "N/a\n")

    fp.close()



def AEPbyTurbineExport(Estacion,file):
    

    with open(path+file, 'w') as fp:
        if Estacion.AEP18 != []:
            fp.write("Datos de AEP para la estación: \n")

            fp.write("2018:\n")
            if Estacion.AEP18 != []:
                fp.write("\tTurbina\t\tAEP(kWH/año)\n")
                for turbina in Estacion.AEP18:
                    fp.write("\t"+turbina[0][0:len(turbina[0])-4]+"\t\t"+str(turbina[1])+"\n")
            else:
                fp.write("\tN/A\n")
            fp.write("\n")

            fp.write("2019:\n")
            if Estacion.AEP19 != []:
                fp.write("\tTurbina\t\tAEP(kWH/año)\n")
                for turbina in Estacion.AEP19:
                    fp.write("\t"+turbina[0][0:len(turbina[0])-4]+"\t\t"+str(turbina[1])+"\n")
            else:
                fp.write("\tN/A\n")
            fp.write("\n")

            fp.write("2020:\n")
            if Estacion.AEP20 != []:
                fp.write("\tTurbina\t\tAEP(kWH/año)\n")
                for turbina in Estacion.AEP20:
                    fp.write("\t"+turbina[0][0:len(turbina[0])-4]+"\t\t"+str(turbina[1])+"\n")
            else:
                fp.write("\tN/A\n")
            fp.write("\n")

            fp.write("2021:\n")
            if Estacion.AEP21 != []:
                fp.write("\tTurbina\t\tAEP(kWH/año)\n")
                for turbina in Estacion.AEP21:
                    fp.write("\t"+turbina[0][0:len(turbina[0])-4]+"\t\t"+str(turbina[1])+"\n")
            else:
                fp.write("\tN/A\n")
            fp.write("\n")

            fp.write("2022:\n")
            if Estacion.AEP22 != []:
                fp.write("\tTurbina\t\tAEP(kWH/año)\n")
                for turbina in Estacion.AEP22:
                    fp.write("\t"+turbina[0][0:len(turbina[0])-4]+"\t\t"+str(turbina[1])+"\n")
            else:
                fp.write("\tN/A\n")
            fp.write("\n")
        
    fp.close()



def genAEPfile(estacion,turbinas,path,index):
    if index==0:
        exportAEPtxt(path+'CIF-AEP-2018.txt',estacion.AEP18,turbinas)
        exportAEPtxt(path+'CIF-AEP-2019.txt',estacion.AEP19,turbinas)
        exportAEPtxt(path+'CIF-AEP-2020.txt',estacion.AEP20,turbinas)
        exportAEPtxt(path+'CIF-AEP-2021.txt',estacion.AEP21,turbinas)
        exportAEPtxt(path+'CIF-AEP-2022.txt',estacion.AEP22,turbinas)

    elif index==1:
        exportAEPtxt(path+'CEANA-AEP-2018.txt',estacion.AEP18,turbinas)
        exportAEPtxt(path+'CEANA-AEP-2019.txt',estacion.AEP19,turbinas)
        exportAEPtxt(path+'CEANA-AEP-2020.txt',estacion.AEP20,turbinas)
        exportAEPtxt(path+'CEANA-AEP-2021.txt',estacion.AEP21,turbinas)
        exportAEPtxt(path+'CEANA-AEP-2022.txt',estacion.AEP22,turbinas)

    elif index==2:
        exportAEPtxt(path+'Electromec-AEP-2018.txt',estacion.AEP18,turbinas)
        exportAEPtxt(path+'Electromec-AEP-2019.txt',estacion.AEP19,turbinas)
        exportAEPtxt(path+'Electromec-AEP-2020.txt',estacion.AEP20,turbinas)
        exportAEPtxt(path+'Electromec-AEP-2021.txt',estacion.AEP21,turbinas)
        exportAEPtxt(path+'Electromec-AEP-2022.txt',estacion.AEP22,turbinas)

    else:
        exportAEPtxt(path+'Planta-AEP-2018.txt',estacion.AEP18,turbinas)
        exportAEPtxt(path+'Planta-AEP-2019.txt',estacion.AEP19,turbinas)
        exportAEPtxt(path+'Planta-AEP-2020.txt',estacion.AEP20,turbinas)
        exportAEPtxt(path+'Planta-AEP-2021.txt',estacion.AEP21,turbinas)
        exportAEPtxt(path+'Planta-AEP-2022.txt',estacion.AEP22,turbinas)



path = input("Ingrese el directorio de carpeta con los txt a importar: ")
filelist=importtxt(path)
genclass(path,filelist)

print(CIF.monthsbyyear)
print(CEANA.monthsbyyear)
print(Electromec.monthsbyyear)
print(Planta.monthsbyyear)

'''
#____________________________________________________________________________________________________________________
#Corroborando que se guarden todos los datos

print("\n\nCIF")
print(CIF.lst2018)
print(CIF.lst2019)
print(CIF.lst2020)
print(CIF.lst2021)
print(CIF.lst2022)

print("\n\nCEANA")
print(CEANA.lst2018)
print(CEANA.lst2019)
print(CEANA.lst2020)
print(CEANA.lst2021)
print(CEANA.lst2022)

print("\n\nELECTROMEC")
print(Electromec.lst2018)
print(Electromec.lst2019)
print(Electromec.lst2020)
print(Electromec.lst2021)
print(Electromec.lst2022)

print("\n\nPLANTA")
print(Planta.lst2018)
print(Planta.lst2019)
print(Planta.lst2020)
print(Planta.lst2021)
print(Planta.lst2022)

#____________________________________________________________________________________________________________________
'''


z2 = float(input("Ingrese la nueva altura: "))
calculoVelocidad(z2,path)

print("Datos nuevos calculados y exportados con éxito.")
print("_______________________________________________\n")





print('')







Turbinas.Turbinas=Turbinas.importTurbinas(pathTurbinas)


print('Calculando AEP para cada turbina.')
#print(Turbinas.Turbinas)

contador=1
for turbina in Turbinas.Turbinas:
    Turbinas.Tabla=Turbinas.openfile(pathTurbinas,contador) 
    print('\nTurbina:',turbina)
    #print(Turbinas.Tabla)
    listaPotencias.append('')
    listaPotencias.append(turbina)
    #   Para CIF
    totalAEP(CIF,turbina)

    #   Para CEANA
    totalAEP(CEANA,turbina)

    #   Para Electromec 
    totalAEP(Electromec,turbina)

    #   Para Planta 
    totalAEP(Planta,turbina)

    print(contador,turbina)
    contador+=1

exportPotencias(path+'/Potencias.txt',listaPotencias)



print("\n Generando archivos con AEP por turbina para cada estación...")

AEPbyTurbineExport(CIF,'/Lista AEP por turbina CIF.txt')
AEPbyTurbineExport(CEANA,'/Lista AEP por turbina CEANA.txt')
AEPbyTurbineExport(Electromec,'/Lista AEP por turbina Eelctromec.txt')
AEPbyTurbineExport(Planta,'/Lista AEP por turbina Planta.txt')

'''

print("\n Generando archivos con AEP máximos para cada estación...")
## Se imprimen las potencias máximas con sus turbinas correspondientes para cada estación


print("\nCIF")
print(CIF.AEP18)
print(CIF.AEP19)
print(CIF.AEP20)
print(CIF.AEP21)
print(CIF.AEP22)

print("\nCEANA")
print(CEANA.AEP18)
print(CEANA.AEP19)
print(CEANA.AEP20)
print(CEANA.AEP21)
print(CEANA.AEP22)

print("\nElectromec")
print(Electromec.AEP18)
print(Electromec.AEP19)
print(Electromec.AEP20)
print(Electromec.AEP21)
print(Electromec.AEP22)

print("\nPlanta")
print(Planta.AEP18)
print(Planta.AEP19)
print(Planta.AEP20)
print(Planta.AEP21)
print(Planta.AEP22)

#   Para CIF
print('\n AEP máximo para CIF:')
maxAEP(CIF,Turbinas.Turbinas,path+'CIF-AEP.txt')

#   Para CEANA
print('\n AEP máximo para CEANA:')
maxAEP(CEANA,Turbinas.Turbinas,path+'CEANA-AEP.txt')

#   Para Electromec 
print('\n AEP máximo para Electromec:')
maxAEP(Electromec,Turbinas.Turbinas,path+'Electromec-AEP.txt')

#   Para Planta 
print('\n AEP máximo para Planta:')
maxAEP(Planta,Turbinas.Turbinas,path+'Planta-AEP.txt')


print("\n Archivos de AEP máximos generados.")

print("________________________________________________________")


#genAEPfile(CIF,Turbinas.Turbinas,path,0)
#genAEPfile(CEANA,Turbinas.Turbinas,path,1)
#genAEPfile(Electromec,Turbinas.Turbinas,path,2)
#genAEPfile(Planta,Turbinas.Turbinas,path,3)



##seleccion=int(input("Ingrese el número de turbina a utilizar: "))
##Turbinas.Tabla=Turbinas.openfile(path,seleccion)

##print(Turbinas.Tabla)

##velocidad=float(input("Ingrese la velocidad a calcular: "))
##a=Turbinas.interpolacion(velocidad)



##print(a)
'''
