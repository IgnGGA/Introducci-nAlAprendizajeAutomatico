def importandoDatos():
    import pandas as pd
    graficador='https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/graphing.py'
    archivo='https://raw.githubusercontent.com/MicrosoftDocs/mslearn-introduction-to-machine-learning/main/Data/doggy-boot-harness.csv'
    datos=pd.read_csv(archivo)
    return(datos)

def trabajandoDatos():
    import statsmodels.formula.api as smf
    import joblib 
    datos=importandoDatos()
    modelo = smf.ols(formula = 'boot_size ~ harness_size', data = datos).fit()
    print('Modelo entrenado')
    modelo_database='./modeloDataset.pkl'
    joblib.dump(modelo, modelo_database)
    print('Modelo guardado.')
    return (modelo_database)

#trabajandoDatos()

def llamandoUnModelo():
    import joblib
    cargandoModelo = joblib.load(trabajandoDatos())
    print(f'Nosotros ahora hemos cargado los siguientes parametros:\n{cargandoModelo.params}')

#llamandoUnModelo()

def cargandoUnModeloYPrediciendo(tamanoArnes):
    import joblib
    modeloCargado=joblib.load('modeloDataset.pkl')
    print(f'Ahora nosotros hemos cargado un modelo con los siguientes parametros:\n{modeloCargado.params}')
    inputs = {'harness_size':[tamanoArnes]}
    prediccionTamanoArnes = modeloCargado.predict(inputs)[0]
    return prediccionTamanoArnes
    
tamanoAPredecir = cargandoUnModeloYPrediciendo(45)
print(f'El tamaño de bota predicho es: {tamanoAPredecir}')