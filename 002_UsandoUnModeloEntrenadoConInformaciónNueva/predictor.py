def cargandoUnModeloYPrediciendo(tamanoArnes):
    import joblib
    modeloCargado=joblib.load('modeloDataset.pkl')
    print(f'Ahora nosotros hemos cargado un modelo con los siguientes parametros:\n{modeloCargado.params}')
    inputs = {'harness_size':[tamanoArnes]}
    prediccionTamanoArnes = modeloCargado.predict(inputs)[0]
    return prediccionTamanoArnes
    
tamanoAPredecir = cargandoUnModeloYPrediciendo(45)
print(f'El tamaño de bota predicho es: {tamanoAPredecir}')