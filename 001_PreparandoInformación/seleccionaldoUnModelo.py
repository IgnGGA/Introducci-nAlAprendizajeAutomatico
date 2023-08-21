import pandas
import statsmodels.formula.api as smf #libreria que hara el trabajo pesado por nosotros

url_1='https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py'
url_2='https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv'

#crear un diccionario (lista) con la informacion de los tamaños de botas y arnes

informacion={
    'boot_size' : [ 39, 38, 37, 39, 38, 35, 37, 36, 35, 40, 
                    40, 36, 38, 39, 42, 42, 36, 36, 35, 41, 
                    42, 38, 37, 35, 40, 36, 35, 39, 41, 37, 
                    35, 41, 39, 41, 42, 42, 36, 37, 37, 39,
                    42, 35, 36, 41, 41, 41, 39, 39, 35, 39
 ],
    'harness_size': [ 58, 58, 52, 58, 57, 52, 55, 53, 49, 54,
                59, 56, 53, 58, 57, 58, 56, 51, 50, 59,
                59, 59, 55, 50, 55, 52, 53, 54, 61, 56,
                55, 60, 57, 56, 61, 58, 53, 57, 57, 55,
                60, 51, 52, 56, 55, 57, 58, 57, 51, 59
                ]
}

#Ahora Convetimos la informacion en tabla haciendo uso de pandas

set_info=pandas.DataFrame(informacion)

#print(set_info)

#Primero definiremos la formula usando una sintaxis especial
#esta dira que el tamaño de las bota se relaciona con el arnes
formula='boot_size ~ harness_size'

#Creamos el modelo, pero no lo entrenaremos
model = smf.ols(formula = formula, data=set_info)

#Observamos que hemos creado el modelo pero no tiene parametros internos

if not hasattr(model, 'parametros'):
    print('Modelo seleccionado pero este no tiene parametros.\nNecesitamos entrenamiento.')