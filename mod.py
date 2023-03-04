"""readme:
    en mod.py  se definen los distintas alteraciones que se puedan presentar dentro de un ciclo de facturacion 
    ejemplo:
        descuentos, cambios de tarifa, cancelaciones, etc
"""
def dcto (days_before,days_after,descuento,value_boleta):
    """readme
        traemos los periodos ya establecidos en day.py y aplcamos descuentos"""
    return (((value_boleta-(value_boleta*descuento))/30)*days_after)+((value_boleta/30)*days_before)
 