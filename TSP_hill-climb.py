# TSP con Hill Climbing

import math 
import random

# Obtencion de la distancia mas corta
def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2)**2 + (lon1 + lon2)**2)

# Calcular la distancia cubierta por cada ruta

def evalua_ruta(ruta):
    total = 0
    for i in range(0, len(ruta)-1):
        ciudad1 = ruta[i]
        ciudad2 = ruta[i+1]
        total = total + distancia(coord[ciudad1], coord[ciudad2])
        ciudad1 = ruta[i+1]
        ciudad2 = ruta[0]
        total = total + distancia(coord[ciudad1], coord[ciudad2])
    return total

def hill_climbing():
    # Crear la ruta inicial Aleatoria
    ruta = []
    for ciudad in coord:
        ruta.append(ciudad)
    random.shuffle(ruta)

    mejora = True
    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta) 
        # Evaluar residuos
        for i in range(0, len(ruta)):
            if mejora:
                break
            for j in range(0, len(ruta)):
                if i!= j:
                    ruta_tmp = ruta[:]
                    ciudad_tmp = ruta[i]
                    ruta_tmp[i] = ruta_tmp[j]
                    ruta_tmp[j] = ciudad_tmp
                    dist = evalua_ruta(ruta_tmp)
                    if dist < dist_actual:
                        # Se ha encontrado un vecino que mejora tu vida el resultado
                        mejora = True
                        ruta = ruta_tmp[:]
                        break
    return ruta

if __name__ == "__main__":
    coord = {
        'Jilotepec': (19.984146, -99.519127),
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

ruta = hill_climbing()
print(ruta)
print("Distancia tota: " + str(evalua_ruta(ruta)))