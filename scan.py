import os
import sys
import platform
from datetime import datetime
from types import DynamicClassAttribute

ip = input("ingresa ip:")
ipDividida = ip.split('.')


#validamos entrada del valor de red
#y de host!

try:
    red = ipDividida[0]+'.'+ipDividida[1]+'.'+ipDividida[2]+'.'
    comienzo=int(input("ingresa el comienzo de la subred: "))
    fin= int(input("ingresa el numero que deseas acabar el barrido: "))
except:
    print('Error!!!')
    sys.exit(1)


if(platform.system()=='Windows'):
    ping = "ping -n 1"
else:
    ping = "ping -c 1"    

tiempoinicio=datetime.now()
#print("[*] El scan se esta realizando desde",red+str(comienzo," hasta ",red+str(fin)))
print("[*] El escaneo se está realizando desde",red+str(comienzo),"hasta",red+str(fin))

for subred in range(comienzo,fin+1):
    direccion=red+str(subred)
    response = os.popen(ping+" "+direccion)
    for line in response.readlines():
        if("ttl" in line.lower()):
            print(direccion," Activo")
            break

tiempofinal=datetime.now()
tiempo = tiempofinal-tiempoinicio
print("[*] El escaneo ha durado %s"%tiempo)