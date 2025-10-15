import matplotlib.pyplot as plt

def generarBarra(tablaOrdenada, columnaX, columnaY, titulo):

    agrupacionDatos=tablaOrdenada.groupby(columnaX)[columnaY].sum()
    plt.figure(figsize=(10,5))
    plt.bar(agrupacionDatos.index,agrupacionDatos.values)
    plt.title(titulo)
    plt.xlabel(columnaX)
    plt.ylabel(columnaY)
    plt.show()