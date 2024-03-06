import os
from datetime import datetime, timedelta #, relativedelta

def days_count():
    # const
    SEVENTY = datetime(2024,2,16)
    UPGRADE = datetime(2024,2,23)
    MAX_DAYS = 120
    
    days_gone_seventy = int((datetime.now() - SEVENTY).days)
    days_gone_upgrade = int((datetime.now() - UPGRADE).days)
    
    # outputs
    output = []
    output.append("pagamos el 70% del auto el 16/2/2024\n")
    output.append(f"pasaron { days_gone_seventy } dias desde esa fecha - lo cual no es tan importante pero ahi esta\n\n")
    output.append("pagamos la mejora del auto el 23/2/2024\n")
    output.append(f"\t!!pasaron { days_gone_upgrade } dias desde esa fecha!! \n\n")
    output.append(f"faltan { MAX_DAYS - days_gone_upgrade } dias para que se cumpla el plazo maximo para que llegue el auto\n")
    #output.append()
    
    
    if MAX_DAYS <= days_gone_upgrade:
        output.append("Se cumplio el plazo, hablar con abogado de lucas\n")
        hashs = []
        for i in range(MAX_DAYS):
            hashs.append("#")
        output.append(f"{''.join(hashs)}\t{round(( MAX_DAYS / MAX_DAYS ) * 100)}% - {MAX_DAYS}/{MAX_DAYS})\n")
    else:
        hashs = []
        for i in range(days_gone_upgrade):
            hashs.append("#")
        output.append(f"{''.join(hashs)}\t{round(( days_gone_upgrade / MAX_DAYS ) * 100)}% - {days_gone_upgrade}/{MAX_DAYS}\n")
    
    return output
    
    
