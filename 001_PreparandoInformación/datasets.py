def datosImportados():
    import pandas
    datos = 'https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv'
    dataset = pandas.read_csv(datos)
    return (dataset)

def cosasParaMostrar():
    import plotly.express as plexp
    graficador = 'https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py'
    datos=datosImportados()
    print('Tamaño de arnés:\n',datos.harness_size)

    #Eliminaremos las columnas sexo y edad en años
    del datos['sex']
    del datos['age_years']

    #visualizaremos la informacion despues de eliminar las columnas sexo y edad.
    print('\nColumnas disponibles despues de eliminar las columnas sexo y edad:\n',datos.columns.values)

    #Imprimir cantidad X de los valores de la tabla
    print('Parte superior de la Tabla:\n', datos.head())#El comando .head(x) muestra los primeros x datos, si es vacio muestra por defecto los primeros 5 datos
    print('Parte inferior de la Tabla:\n', datos.tail())#El comando .tail(y) muestra los ultimos y datos, si es vacio muestra por defecto los ultimos 5 datos

    #imprimir el tamaño de nuestra tabla:
    print(f'Nosotros tenemos {len(datos)} de filas de información')

    esMenorQue = datos.harness_size < 55
    print(f'\nCuantos arnés de perro son menores de 55:\n{esMenorQue}\n')
    infoPerrosPequenos = datos[esMenorQue]#Esto es equivalente a datos[datos.harness_size]<55 implica una aplicacion de un filtro en la tabla
    print(f'\nInformación para perros con tamaños de arnés menores a 55:\n{infoPerrosPequenos}\n')
    print(f'\nNumero de perros con arnés de tamaño menor a 55:\n{len(infoPerrosPequenos )}')

    patasPequenas=datos[datos.boot_size<40].copy()#Realizaremos una copia de la inforacion que contenga valores menores a 40 en la columna tamaño de bota
    print(f'Ahora tenemos {len(patasPequenas)} filas de información\nDonde las ultimas filas son{patasPequenas.tail()}')

    plexp.scatter(patasPequenas, x='harness_size', y='boot_size')

cosasParaMostrar()