import glob
import pandas as pd
import os 
#función que encuentra PATH de varios csv
def direccion(path):
    dfVacio = pd.DataFrame()
    all_data = glob.glob(path)
    #dfall_data = pd.read_csv(all_data, enconding = 'utf-8')
    for i in all_data:
        df_temp = pd.read_csv(i, encoding = "ISO-8859-1" )
        dfVacio = pd.concat([dfVacio, df_temp], ignore_index= True)
    #dfVacio


    dfVacio.to_csv('C:/Users/juanm/OneDrive/Escritorio/TrabajoSam/FINAL/concatenado.csv', encoding = "utf-8" )
    eliminarInput = str(input('Si quiere eliminar columnas ingrese ''1'', si no tiene columnas por eliminar, pero si por mezclar, presione 2 '))
    DfOrganizar = pd.read_csv('C:/Users/juanm/OneDrive/Escritorio/TrabajoSam/FINAL/concatenado.csv', encoding = "utf-8")
    if eliminarInput == '1':
        eliminarPath = str(input('Ingrese la dirección del archivo hoja de prueba, recuerde cambiar \ por / y poner el nombre del archivo con la extensión .csv: '))
        eliminar(eliminarPath, DfOrganizar)

    elif eliminarInput == '2':
        mezclarInput = str(input('Ingrese la dirección del archivo index3, recuerde cambiar \ por / y poner el nombre del archivo con la extensión .csv: '))
        DfNoNaFill = DfOrganizar.fillna(' ').copy(deep=True)
        merge(mezclarInput, DfNoNaFill)
    else:
        print('Ingrese un número, 1 ó 2 según su necesidad')

#Función que encuentra PATH de un solo csv
def UnaDire(path):
    DfLeer = pd.read_csv(path, encoding="ISO-8859-1")
    #DfLeerGuardado = pd.to_csv('C:/Users/juanm/OneDrive/Escritorio/TrabajoSam/FINAL/concatenado.csv', encoding = "utf-8")
    #DfNoNa = pd.read_csv('C:/Users/juanm/OneDrive/Escritorio/TrabajoSam/FINAL/concatenado.csv', encoding = "utf-8")
    #return DfLeer
    eliminarInput = str(input('Si quiere eliminar columnas ingrese ''1'', si no tiene columnas por eliminar, pero si por mezclar, presione 2 '))
    
    if eliminarInput == '1':
        eliminarPath = str(input('Ingrese la dirección del archivo hoja de prueba, recuerde cambiar \ por / y poner el nombre del archivo con la extensión .csv: '))
        eliminar(eliminarPath, DfLeer)

    elif eliminarInput == '2':
        mezclarInput = str(input('Ingrese la dirección del archivo index3, recuerde cambiar \ por / y poner el nombre del archivo con la extensión .csv: '))
        DfNoNaFill = DfLeer.fillna(' ').copy(deep=True)
        merge(mezclarInput, DfNoNaFill)
    else:
        print('Ingrese un número, 1 ó 2 según su necesidad')

#Función que me elimina celdas
def eliminar(columnsdrop, dfsucio):
    columnasEliminar = pd.read_csv(columnsdrop, encoding="ISO-8859-1") 
    DfSucio = dfsucio
    #DfSucio = pd.read_csv(dfsucio, encoding='ISO-8859-1')
    ColumnsDrop = columnasEliminar['Borrar'].tolist()

    DfLimpio = DfSucio.drop(ColumnsDrop, axis = 1).copy(deep=True)
    DfLimpioNoNa = DfLimpio.fillna(' ').copy(deep=True)
    DfLimpioNoNa.to_csv('C:/Users/juanm/OneDrive/Escritorio/TrabajoSam/FINAL/limpio.csv', encoding = "ISO-8859-1")
    CombinarInput = str(input('Si tiene celdas por combinar, ingrese ""1"", sino presione ""2"": '))
    DfLimpioTotalmente = pd.read_csv('C:/Users/juanm/OneDrive/Escritorio/TrabajoSam/FINAL/limpio.csv', encoding = "ISO-8859-1")
    if CombinarInput == '1':
        DireccionIndex = str(input('Ingrese la dirección del archivo index3, recuerde cambiar \ por / y poner el nombre del archivo con la extensión .csv: '))
        merge(DireccionIndex, DfLimpioTotalmente)
    elif CombinarInput == '2':
        DfLimpioTotalmente
    else:
        print('Ingrese 1 ó 2 según su necesidad')
#Funcion que me junta columnas

def merge(index, dflimpio):
    DfIndexar = pd.read_csv(index, encoding='utf-8')

    NombreDescript = {}
    for i in range(DfIndexar.shape[0]):
        a = DfIndexar.iloc[i, 0]
        b = DfIndexar.iloc[i, 1]
        NombreDescript[b] = NombreDescript.get(b, list())
        NombreDescript[b].append(a)

    dflimpioNoNaColumns = pd.DataFrame()

    for k in NombreDescript.keys():
        dflimpioNoNaColumns[k] = dflimpio[NombreDescript[k]].astype(str).T.agg(''.join)

    dflimpioNoNaColumns.to_csv('C:/Users/juanm/OneDrive/Escritorio/TrabajoSam/FINAL/Final.csv', encoding = "utf-8", index=False) 

    
    
def run():


    opcion = str(input('Ingrese 1 si va a trabajar con un archivo o 2 si son varios archivos: '))

    if opcion == '1':
        path = str(input('Ingrese la dirección de la carpeta recuerde cambiar \ por / y poner el nombre del archivo con la extensión .csv: '))
        UnaDire(path)
    elif opcion == '2': 
        path = str(input('Ingrese la dirección de la carpeta recuerde cambiar \ por / y poner el nombre del archivo con la extensión .csv: '))
        direccion(path)        

if __name__ == "__main__":
    run()
