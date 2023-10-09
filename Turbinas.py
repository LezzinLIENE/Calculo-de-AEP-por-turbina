import os
import glob

#Turbinas=["2-aerogenesis-5000.txt" "Aerogenesis Turbine" "5 kW";"3-high-900.txt" "High" "900 W";"3-low-900.txt" "Low" "900 W"; "4-Airx-400.txt" "Commercial Ar-X" "400 W"; "5-ATT-400.txt" "Air-x modified with ATT" "400 W"; "6--5500.txt" "-" "5.5 W"; "7--75.txt" "-" "7.5 W"; "8-SWT5-5000.txt" "SWT wind turbine" "5 KW";"9-SWT3-3000.txt" "SWT wind turbine" "3 KW";"10-SW1-1000.txt" "SW wind turbine" "1 KW";"11-SW2-2000.txt" "SW wind turbine" "2 KW";"12-SW3-3000.txt" "SW wind turbine" "3 KW";"13-SW5-5000.txt" "SW wind turbine" "5 kW";"14-pitch-2000.txt" "Pitch wind turbine" "2 kW";"15-evance-5000.txt" "Evancewind R9000" "5 kW";"16-eol-5000.txt" "Eolulion Wind Turbine" "5 kW";"17-fortis5-5000.txt" "Fortis Wind Energy Montana" "5 kW";"18-fortis14-1400.txt" "Fortis Wind Energy Passaat" "1.4 kW";"19-raum-1500.txt" "Raum Energy" "1.5 kW";"20-kestrel-2500.txt" "Kestrel-e400nb" "2.5 kW";"21-skystream-2100.txt" "Skstream 3.7" "2.1 KW";"22-T701-1500.txt" "T701" "1.5 kW";"23-giraffe-2746.txt" "Giraffe 2.0/Windspot 3.5" "2.746 kW";"24-windspot-3500.txt" "Windspot 3.5" "3.5 kW";"25-DS-3000.txt" "Ds3000" "3 kW";"26-H3-1000.txt" "H3.1" "1 kW";"27-gerar-1000.txt" "GERAR 246" "1 kW";"28-ELV-500.txt" "ELV-H2.7" "500 W";"29-ELV-2000.txt" "ELV-H3.8" "2 kW";"30-ELV-3000.txt", "ELV-H4.6 3 kW"],["31-fd4-3000.txt", "Fd4.0 3 kW"],["32-fanturbine-5000.txt","Fanturbine 5 kW"]]
Turbinas=[]
Tabla=[]

def importTurbinas (path):
    os.chdir(path)
    my_files = glob.glob('*.txt')
    return my_files

def openfile (path,seleccion):
    Tabla=[]
    if seleccion <= len(Turbinas):
        #Turbinas[seleccion-1]
        with open(path+'\\'+Turbinas[seleccion-1]) as f:
            lines = f.readlines()
        f.close()
        for linea in lines:
            posicion=0
            num=''
            while posicion < len(linea):
                if linea[posicion]!='\t':
                    num+=linea[posicion]
                else:
                    Tabla.append([float(num),float(linea[posicion+1:len(linea)-1])])
                    posicion=len(linea)
                posicion+=1
    return Tabla


def interpolacion (velocidad):
    contador=0
    contador2=1
    y=0
    while contador2<len(Tabla):
        if velocidad>Tabla[contador][0] and velocidad<Tabla[contador2][0]:
            b=(Tabla[contador2][1]-Tabla[contador][1])/(Tabla[contador2][0]-Tabla[contador][0])
            a=Tabla[contador][1]-b*Tabla[contador][0]
            y=a+b*velocidad
                                        
        elif velocidad == Tabla[contador][0]:
            y=Tabla[contador][1]

        elif velocidad == Tabla[contador2][0]:
            y=Tabla[contador2][1]
                   

        contador=contador+1
        contador2=contador2+1
    return y


'''
path=input("Inserte el path: ")
Turbinas=importTurbinas(path)

contador=1
for turbina in Turbinas:
    print(contador,turbina)
    contador+=1

print('')
seleccion=int(input("Ingrese el número de turbina a utilizar: "))
Tabla=openfile(path,seleccion)
print(Tabla)
velocidad=float(input("Ingrese la velocidad a calcular: "))
a=interpolacion(velocidad)
print(a)

'''
