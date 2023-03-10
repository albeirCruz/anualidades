from day import contador
from mod import dcto

if __name__=="__main__":
    ciclo=int(input("ingrese el ciclo del cliente: \n"))
    ret_call=input("ingrese fecha de retencion de la siguiente manera: -> 00/00 (dia/mes) \n")
    #traemos los periodos establecidos
    cont=contador(ciclo,ret_call)
    #aplicamos descuento
    prop_dcto=dcto(cont[1],0.3,49900)
    print("\nvalor proporcional de la boleta:", prop_dcto)