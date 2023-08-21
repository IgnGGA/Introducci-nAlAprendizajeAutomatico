def cargandoUnModeloYPrediciendo(tamanoArnes):
    import joblib
    modeloCargado=joblib.load('modeloDataset.pkl')
    print(f'Ahora nosotros hemos cargado un modelo con los siguientes parametros:\n{modeloCargado.params}')
    inputs = {'harness_size':[tamanoArnes]}
    prediccionTamanoArnes = modeloCargado.predict(inputs)[0]
    return prediccionTamanoArnes
    
def chequeandoTamanoDeBotas(tamanoArnes, tamanoBotas):
    estimadoTamanoBotas=cargandoUnModeloYPrediciendo(tamanoArnes)
    estimadoTamanoBotas=int(round(estimadoTamanoBotas))
    if tamanoBotas == estimadoTamanoBotas:
        return print(f'Gran eleccion, nosotros pensamos que estas botas estan bien para tu perro')
    elif tamanoBotas<estimadoTamanoBotas:
        return print('Las botas que has seleccionado son muy pequeñas para un\n'\
            'perro tan grande como el tuyo,\n'\
                f'nosotros recomendamos el siguiente tamaño de botas: {estimadoTamanoBotas}')
    elif tamanoBotas>estimadoTamanoBotas:
        return print('las botas que has seleccionado son muy grandes para un\n'\
            'perro tan pequeño como el tuyo,\n'\
                f'nosotros recomendamos el siguiente tamaño de botas: {estimadoTamanoBotas}')

chequeandoTamanoDeBotas(55,39)