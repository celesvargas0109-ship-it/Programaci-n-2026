producto = ["Cafe", 5000, 20]

porcentaje_aumento = 20

descuento = producto[1] * 15 / 100
#print (descuento)

ingreso_actual = producto[1] * producto[2]
#print(ingreso_actual)

precio_promocional = producto[1] - descuento

aumento = producto[2] * porcentaje_aumento / 100
#print(aumento)

aumento_unidad = aumento + 20
#print(aumento_unidad)

unidades_totales = aumento_unidad + producto [2]

ingreso_proyectado = precio_promocional * aumento_unidad 
#print(ingreso_proyectado)

diferencia = ingreso_proyectado - ingreso_actual
#print(diferencia)

if diferencia > 0:
    RECOMENDACION = 'Lanzar'
else:
    RECOMENDACION = 'No lanzar'
#print(RECOMENDACION)

print('Promociones de Café')
print('_' * 70, "\n")
print(f"\nProducto: Café")
print(f"Precio actual: ₡{producto[1]:.0f}")
print(f"Unidades actuales:{producto[2]}")
print(f"Ingreso: ₡{ingreso_actual:.0f}")
print(f"\nDescuento: ₡{descuento:.0f}")
print(f"Precio promocional: ₡{precio_promocional:.0f}")
print(f"\nAumento esperado en ventas: {porcentaje_aumento}%")
print(f"Unidades proyectadas: {unidades_totales}")
print(f"Ingreso con promocion: ₡{ingreso_proyectado:.0f}")
print(f"Diferencia: ₡{diferencia:.0f}")
print("\n" + "_" * 70)
print(f"RECOMENDACION: {RECOMENDACION}.")
print("=" * 70)
