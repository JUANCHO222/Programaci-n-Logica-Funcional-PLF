# TSP con búsqueda tabú 
import math 
import random
def distancia(coord1, coord2): 
    lat1 = coord1[0] 
    lon1 = coord1[1] 
    lat2 = coord2[0] 
    lon2 = coord2[1] 
    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2) 
# calcula la distancia cubierta por una ruta 
def evalua_ruta(ruta): 
    total=0 
    for i in range(0,len(ruta)-1): 
        ciudad1=ruta[i] 
        ciudad2=ruta[i+1] 
        total=total+distancia(coord[ciudad1], coord[ciudad2]) 
    ciudad1=ruta[i+1] 
    ciudad2=ruta[0] 
    total=total+distancia(coord[ciudad1], coord[ciudad2]) 
    return total 

def busqueda_tabu(ruta): 
    mejor_ruta=ruta 
    memoria_tabu={} 
    persistencia=5 
    mejora=False 
    iteraciones=100 
    
    while iteraciones>0: 
        iteraciones = iteraciones-1 
        dist_actual = evalua_ruta(ruta) 
        # Evaluar vecinos 
        mejora = False 
        for i in range(0,len(ruta)): 
            if mejora: 
                break 
            for j in range(0,len(ruta)): 
                if i!=j: 
                    ruta_tmp=ruta[:] 
                    ciudad_tmp=ruta_tmp[i] 
                    ruta_tmp[i]=ruta_tmp[j] 
                    ruta_tmp[j]=ciudad_tmp 
                    dist=evalua_ruta(ruta_tmp) 
                    # Comprobar si el movimiento es tabú 
                    tabu=False 
                    if ruta_tmp[i]+"_"+ruta_tmp[j] in memoria_tabu: 
                        if memoria_tabu[ruta_tmp[i]+"_"+ruta_tmp[j]]>0: 
                            tabu=True 
                    if ruta_tmp[j]+"_"+ruta_tmp[i] in memoria_tabu: 
                        if memoria_tabu[ruta_tmp[j]+"_"+ruta_tmp[i]]>0: 
                            tabu=True 

                    if dist<dist_actual and not tabu:
                    # Encontrado vecino que mejora el resultado         
                        ruta=ruta_tmp[:] 
                        if evalua_ruta(ruta)<evalua_ruta(mejor_ruta): 
                            mejor_ruta=ruta[:] 
                    # Almacenamos en memoria tabú 
                        memoria_tabu[ruta_tmp[i]+"_"+ruta_tmp[j]]=persistencia 
                        mejora=True 
                        break 
                    elif dist<dist_actual and tabu: 
                        # Comprobamos criterio de aspiración 
                        # Aunque sea movimiento tabú 
                        if evalua_ruta(ruta_tmp)<evalua_ruta(mejor_ruta): 
                            mejor_ruta=ruta_tmp[:] 
                            ruta=ruta_tmp[:] 
                            # almacenamos en memoria tabú 
                            memoria_tabu[ruta_tmp[i]+"_"+ruta_tmp[j]]=persistencia 
                            mejora=True 
                            break 
                # Rebajar persistencia de los movimientos tabú 
                if len(memoria_tabu)>0: 
                    for k in memoria_tabu: 
                        if memoria_tabu[k]>0: 
                            memoria_tabu[k]=memoria_tabu[k]-1 
    return mejor_ruta 

if __name__ == "__main__": 
    coord = { 
        'Jiloyork': (19.984146, -99.519127),
        'Toluca': (19.283389, -99.651294),
        'Atlacomulco': (19.797032, -99.875878),
        'Guadalajara': (20.666006, -103.343649),
        'Monterrey': (25.687299, -100.315655),
        'Cancun': (21.080865, -86.773482),
        'Morelia': (19.706167, -101.191413),
        'Aguascalientes': (21.861534, -102.321629),
        'Querétaro': (20.614858, -100.392965),
        'CDMX': (19.432361, -99.133111),  
    } 
# Crear ruta inicial aleatoria 
ruta=[] 
for ciudad in coord: 
    ruta.append(ciudad) 
random.shuffle(ruta) 

ruta = busqueda_tabu(ruta) 
print(ruta)
print("Distancia total: " + str(evalua_ruta(ruta)))