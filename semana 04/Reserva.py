#Solución Kit Seguro

nombre = input('Nombre: ').upper().strip()
kit = input('Tipo de kit: ').upper().strip()
autorizacion = input('Tiene autorización (si/no)?: ').lower().strip() == 'si'
try: 
    cantidad = int(input('Cantidad de kits?: '))
except ValueError:
    print('Cantidad de kits inválida, digite del 1 al 100')
    cantidad = -1  
try:   
    dias = int(input('Días de préstamo: '))
except ValueError:
    print('Cantidad de días inválidas, digite del 1 al 100')
    cantidad = -1

if not nombre or not kit or cantidad < 1 or dias < 1:
    resultado = 'Revise los datos ingresados'
elif autorizacion and cantidad <= 3 and not dias > 7:
    resultado = f'Solicitud aprobada para {nombre}: '
else:
    resultado = 'Solicitud enviada a revisión'

print(resultado)
