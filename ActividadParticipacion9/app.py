from modelo.datos_meteorologicos import DatosMeteorologicos



datos_meteorologicos = DatosMeteorologicos("datos.txt")
print(datos_meteorologicos.procesar_datos())