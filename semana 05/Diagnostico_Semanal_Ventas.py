"""Plantilla guiada: análisis de ventas de dos tiendas, sin ciclos."""

ventas_centro = [125000, 98000, 147000, 132000, 110000]
ventas_norte = [140000, 135000, 150000, 145000, 155000]
meta_centro = 640000
meta_norte = 700000

# TODO: calcula total, cantidad, mayor y menor para Centro.
total_centro = sum(ventas_centro) #total de ventas semanal
cantidad_centro = len(ventas_centro) #días registrados centro

menor_centro = min(ventas_centro) #venta mínima centro
mayor_ventas = max (ventas_centro) #venta máxima centro
promedio_centro = total_centro / cantidad_centro
porcentaje_centro = total_centro * 100 / meta_centro
#print(porcentaje_centro)

# TODO: repite los indicadores para Norte.
total_norte = sum(ventas_norte) #total de ventas semanal
cantidad_norte = len(ventas_norte) #días registrados centro

menor_ventas = min(ventas_norte) #venta mínima norte
mayor_ventas = max (ventas_norte) #venta máxima norte
promedio_norte = total_norte / cantidad_norte
porcentaje_norte = total_norte * 100 / meta_norte
#print(porcentaje_norte)

# TODO: decide si cada tienda superó, igualó o no alcanzó su meta.
if total_centro > meta_centro:
    estado_centro = 'meta superada'
elif total_centro == meta_centro:
    estado_centro = 'meta alcanzada'
else:
    estado_centro = 'meta no alcanzada'

if total_norte > meta_norte:
    estado_norte = 'meta superada'
elif total_norte == meta_norte:
    estado_norte = 'meta alcanzada'
else:
    estado_norte = 'meta no alcanzada'

# TODO: compara los totales y los rangos.
if total_centro > total_norte:
    tienda_ganadora = 'Tienda del Centro'
elif total_norte > total_centro:
    tienda_ganadora = 'Tienda del Norte'
else:
    tienda_ganadora = 'Ambas tiendas tienen el mismo total'

# TODO: presenta un reporte con etiquetas claras y f-strings.
print('Comparación semanal de tiendas')
print('_' * 70, "\n")
print(f"Centro | total ₡{total_centro:,.2f} | meta ₡{meta_centro:,.2f} | cumplimiento {porcentaje_centro:.0f}%")
print(f"Centro logro: {estado_centro}")
print(f"Norte | total ₡{total_norte:,.2f} | meta ₡{meta_norte:,.2f} | cumplimiento {porcentaje_norte:.0f}%")
print(f"Norte logro: {estado_norte}")

print("\nTienda con mayor ventas:", tienda_ganadora)
print('_' * 70, "\n")

# TODO: escribe las tres conclusiones solicitadas en la guía.
