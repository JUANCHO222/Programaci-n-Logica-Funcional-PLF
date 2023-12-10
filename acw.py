# VRP
import math
from operator import itemgetter

def distancia(coord1, coord2):
    lat1 = coord1[0]
    lon1 = coord1[1]
    lat2 = coord2[0]
    lon2 = coord2[1]
    return math.sqrt((lat1 - lat2) ** 2 + (lon1 - lon2) ** 2)

def en_ruta(rutas, c):
    ruta = None
    for r in rutas:
        if c in r:
            ruta = r
    return ruta

def peso_ruta(ruta):
    total = 0
    for c in ruta:
        total = total + pedidos[c]
    return total

def vrp_voraz():
    # calcular los ahorros
    s = {}
    for c1 in coord:
        for c2 in coord:
            if c1 != c2:
                if not (c2, c1) in s:
                    d_c1_c2 = distancia(coord[c1], coord[c2])
                    d_c1_almacen = distancia(coord[c1], almacen)
                    d_c2_almacen = distancia(coord[c2], almacen)
                    s[c1, c2] = d_c1_almacen + d_c2_almacen - d_c1_c2
    # ordenar ahorros
    s = sorted(s.items(), key=itemgetter(1), reverse=True)
    # construir rutas
    rutas = []
    for k, v in s:
        rc1 = en_ruta(rutas, k[0])
        rc2 = en_ruta(rutas, k[1])
        if rc1 == None and rc2 == None:
            # no están en ninguna ruta. La creamos.
            if peso_ruta([k[0], k[1]]) <= max_carga:
                rutas.append([k[0], k[1]])
        elif rc1 != None and rc2 == None:
            # ciudad 1 ya en una ruta. Agregamos la ciudad 2
            if rc1[0] == k[0]:
                if peso_ruta(rc1) + peso_ruta([k[1]]) <= max_carga:
                    rutas[rutas.index(rc1)].insert(0, k[1])
            elif rc1[len(rc1) - 1] == k[0]:
                if peso_ruta(rc1) + peso_ruta([k[1]]) <= max_carga:
                    rutas[rutas.index(rc1)].append(k[1])
        elif rc1 == None and rc2 != None:
            # ciudad 2 ya en una ruta. Agregamos la ciudad 1
            if rc2[0] == k[1]:
                if peso_ruta(rc2) + peso_ruta([k[0]]) <= max_carga:
                    rutas[rutas.index(rc2)].insert(0, k[0])
            elif rc2[len(rc2) - 1] == k[1]:
                if peso_ruta(rc2) + peso_ruta([k[0]]) <= max_carga:
                    rutas[rutas.index(rc2)].append(k[0])
        elif rc1 != None and rc2 != None and rc1 != rc2:
            # ciudad 1 y 2 ya en una ruta. Tratamos de unirlas
            if rc1[0] == k[0] and rc2[len(rc2) - 1] == k[1]:
                if peso_ruta(rc1) + peso_ruta(rc2) <= max_carga:
                    rutas[rutas.index(rc2)].extend(rc1)
                    rutas.remove(rc1)
            elif rc1[len(rc1) - 1] == k[0] and rc2[0] == k[1]:
                if peso_ruta(rc1) + peso_ruta(rc2) <= max_carga:
                    rutas[rutas.index(rc1)].extend(rc2)
                    rutas.remove(rc2)
    return rutas

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
    pedidos = {
        'Jilotepec':10,
        'Toluca':15,
        'Atlacomulco':0,
        'Guadalajara':0,
        'Monterrey':40,
        'Cancun':50,
        'Morelia':25,
        'Aguascalientes':45,
        'CDMX':60,
        'Querétaro':100,
    }

    almacen = (40.23, -3.40)
    max_carga = 40
    rutas = vrp_voraz()
    for ruta in rutas:
        print(ruta)