from day import contador
from mod import dcto

if __name__=="__main__":
    ciclo=int(input("ingrese el ciclo del cliente: \n"))
    ret_call=input("ingrese fecha de retencion de la siguiente manera: -> 00/00 (dia/mes) \n")
    year=" "
    year=input("año biciesto: y/n\n")
    out=float(input("ingrese el descuento de la siguiente manera: -> 0.0\n"))
    value_price=int(input("ingrese el valor de la voleta sin decimales:\n"))
    #traemos los periodos establecidos
    cont=contador(ciclo,ret_call,year)
    #aplicamos descuento
    prop_dcto=dcto(cont[1],out,value_price)
    print("\nvalor proporcional de la boleta:", prop_dcto)