def importandoDatos():
    import pandas as pd
    graficador='https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py'
    archivo='https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv'
    datos=pd.read_csv(archivo)
    return(datos)

def trabajandoDatos():
    import statsmodels.formula.api as smf
    datos=importandoDatos()
    print(datos.head())
    modelo = smf.ols(formula = 'boot_size ~ harness_size', data = datos).fit()
    print('Modelo entrenado')
trabajandoDatos()
