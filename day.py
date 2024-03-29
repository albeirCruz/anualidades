def b_year():
    """ NOTA:   en esta clase definiremos una forma de contar periodos de tiempo basados en anualidades, especificamente de tiempo-contingente,
        las cuales tienen un inicio pero se desconoce e un fin.
        nos basaremos en los dias que contiene un año  si es bisiesto (366), y definiremos interacciones en ese periodo de tiempo 
        identificando primeramente el numero de dia correspondiente a cada interaccion. 
    """
#se define numero de dias para año bisiesto = 366 dias
    leap_year = {
        1: 31,
        2: 29,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,}
    return leap_year
def n_year():
    """ NOTA:   en esta clase definiremos una forma de contar periodos de tiempo basados en anualidades, especificamente de tiempo-contingente,
        las cuales tienen un inicio pero se desconoce e un fin.
        nos basaremos en los dias que contiene un año normal(365), y definiremos interacciones en ese periodo de tiempo 
        identificando primeramente el numero de dia correspondiente a cada interaccion. 
    """
    #se define numero de dias para año no bisiesto = 365 dias
    normal_year = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    return normal_year
#recorrer mi diccionario para sumar los dias hasta un mes antes del ingresado por el usuario
def def_n_day (day_i,month_i,diccionario):
    """combierte una fecha en el numero del dia correspondiente, dentro de un año de 365 o 366 
        ejemplo:
            ingresa day_i y month_i= 04/03
            return day_i(4)+month(59)"""
    day=day_i
    month=month_i-1
    temp=0
    #year=c para generar condicion de año bisiesto o normal, aun sin definir.      
    for mes, dias in diccionario.items():
        temp+=dias
        if mes>=month:
            return temp+day                 
def contador (ciclo_i,ret_c,year): 
    """llama la funcion def_n_day y establece el numero de dia para inicio y final de ciclo, 
        tambien el numeor de dia de la alteracion en el ciclo de facturacion y los agrupa para definir 
        los periodos de tiempo dentro de un ciclo de facturacion""" 
    if year=="y":
        diccionario = b_year()
    else:
        diccionario = n_year()
    ciclo=ciclo_i
    ret_call=ret_c
    ret_day=int(ret_call[0:2])
    ret_month=int(ret_call[3:5])
    #cada fecha de interaccion corresponde a un numero de dia en un periodo de año de 365 dias para este caso
    #a continuacion definiremos esos numeros de dias
    #defino el inicio del ciclo correspondiente al caso atendido en el momento
    if ret_day >= ciclo:     
        start_ciclo=def_n_day(ciclo,ret_month,diccionario)  
    else:
        start_ciclo=def_n_day(ciclo,ret_month-1,diccionario)
    print("dia de inicio ciclo: ",start_ciclo)
    #defino el final del ciclo correspondiente al caso atendido en el momento
    if ret_day > ciclo:
        final_ciclo=def_n_day(ciclo,ret_month+1,diccionario)
    else:
        final_ciclo=def_n_day(ciclo,ret_month,diccionario)
    print("dia de fin ciclo: ",final_ciclo)
    #definie el numero de dia de la retencion
    ret=def_n_day(ret_day,ret_month,diccionario)
    #definimos los dos periodos antes y despues de la retencion
    days_before=ret-start_ciclo
    days_after=final_ciclo-ret
    print("dias transcurridos sin oferta de retencion: ", days_before,"\n")
    print("dias transcurridos con oferta de retencion: ", days_after)
    return days_before,days_after        