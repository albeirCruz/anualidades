
def dict():
    """ NOTA:   en esta clase definiremos una forma de contar periodos de tiempo basados en anualidades, especificamente de tiempo-contingente,
        las cuales tienen un inicio pero se desconoce e un fin.
        nos basaremos en los dias que contiene un año dependiendo si es bisiesto o no (365/366), y definiremos interacciones en ese periodo de tiempo 
        identificando primeramente el numero de dia correspondiente a cada interaccion. 
    """

    #se define numero de dias para año bisiesto = 366 dias
    """leap_year = {
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
        12: 31,
    }"""

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
def def_n_day (a,b,diccionario):


    day=a
    month=b-1
    temp=0
        #year=c para generar condicion de año bisiesto o normal, aun sin definir.
        
    for mes, dias in diccionario.items():
        temp+=dias
        if (mes>=month):
            return temp+day
            break
                         
def contador (c,r_c): 
        
        diccionario = dict()
        
        ciclo=c
        ret_call=r_c
        ret_day=int(ret_call[0:2])
        ret_month=int(ret_call[3:5])

        
        #cada fecha de interaccion corresponde a un numero de dia en un periodo de año de 365 dias para este caso
        #a continuacion definiremos esos numeros de dias
        #defino el inicio del ciclo correspondiente al caso atendido en el momento
        if (ret_day >= ciclo):
             
            start_ciclo=def_n_day(ciclo,ret_month,diccionario)
            print("1")
        
        else:
             start_ciclo=def_n_day(ciclo,ret_month-1,diccionario)
             print("2")

        print("dia de inicio ciclo: ",start_ciclo)


        #defino el final del ciclo correspondiente al caso atendido en el momento
        
        if (ret_day > ciclo):
             
            final_ciclo=def_n_day(ciclo,ret_month+1,diccionario)
            print("1")
        
        else:
            final_ciclo=def_n_day(ciclo,ret_month,diccionario)
            print("2")

       
        print("dia de fin ciclo: ",final_ciclo)

        #definie el numero de dia de la retencion

        ret=def_n_day(ret_day,ret_month,diccionario)
        #____________________________________________________________________________________

        days_before=ret-start_ciclo
        days_after=final_ciclo-ret

 
        print("dias transcurridos sin oferta de retencion: ", days_before,"\n")
        print("dias transcurridos con oferta de retencion: ", days_after)

        return days_before,days_after
        
