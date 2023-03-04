def dcto (days_before,days_after,dcto,value_boleta):
    return (((value_boleta-(value_boleta*dcto))/30)*days_after)+((value_boleta/30)*days_before)

 