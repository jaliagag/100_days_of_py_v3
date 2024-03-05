import os
from datetime import datetime, timedelta #, relativedelta

# const
SEVENTY = datetime(2024,2,16)
UPGRADE = datetime(2024,2,23)
MAX_DAYS = 120

days_gone_seventy = int((datetime.now() - SEVENTY).days)
days_gone_upgrade = int((datetime.now() - UPGRADE).days)

# outputs
print("pagamos el 70% del auto el 16/2/2024")
print(f"pasaron { days_gone_seventy } dias desde esa fecha - lo cual no es tan importante pero ahi esta\n")
print("pagamos la mejora del auto el 23/2/2024")
print(f"!!pasaron { days_gone_upgrade } dias desde esa fecha!! \n")
print(f"faltan { MAX_DAYS - days_gone_upgrade } dias para que se cumpla el plazo maximo para que llegue el auto\n")

if MAX_DAYS <= days_gone_upgrade:
        print("Se cumplio el plazo, hablar con abogado de lucas")
        for i in range(MAX_DAYS):
                print("#", end="")
        print(f"\t{round(( MAX_DAYS / MAX_DAYS ) * 100)}% - {MAX_DAYS}/{MAX_DAYS}")
else:
        for i in range(days_gone_upgrade):
                print("#", end="")
        print(f"\t{round(( days_gone_upgrade / MAX_DAYS ) * 100)}% - {days_gone_upgrade}/{MAX_DAYS}")

