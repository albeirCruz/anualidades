from day import contador

if __name__=="__main__":
    
    ciclo=int(input("ingrese el ciclo del cliente: \n"))
    ret_call=input("ingrese fecha de retencion de la siguiente manera: -> 00/00 (dia/mes) \n")
    
    cont=contador(ciclo,ret_call)

