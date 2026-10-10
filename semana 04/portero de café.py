"""Microreto: el portero del café."""

nombre = input('Como te llamas?: ').upper().strip()
energia = int(input('Cuanta energía tienes de 0 a 100?: '))
trae_cafe = input('Traes café (si/no)?: ').lower().strip() == 'si'

mensaje = 'Portero confundido, revisar respuestas'

# Si menos 50% y no traigo café: Descansar
if (energia < 50 and trae_cafe == False):
    mensaje = 'Descansar'
# Si 50% o más o que tenga un café: Puede ingresar a la clase
elif(energia >= 50 or trae_cafe == 'True'):
    mensaje = 'Puede ingresar a la clase'
#Cualquier otro escenario: Portero confundido, revisar respuestas
else:
    mensaje = 'Portero confundido, revisar respuestas'

print(f'{nombre}: {mensaje}')