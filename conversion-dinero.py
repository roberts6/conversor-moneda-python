
tipo_de_cambio_eur_a_mex = 23.7
tipo_de_cambio_usd_a_mex = 20.75

# 1. Solicitar el tipo de moneda y convertir a mayúsculas 
tipo_de_moneda = input("Por favor, ingresá la moneda que querés convertir (Euro / Dolar): ").upper()

# 2. Solicitar el monto y reemplazar coma por punto si es necesario
monto_a_convertir = input("Por favor, ingrese el monto a convertir: ").replace(',', '.')

# Convertir el monto a flotante
monto_a_convertir = float(monto_a_convertir)

# 3. Validar el tipo de moneda y hacer la conversión correcta
if tipo_de_moneda == "EURO":
    resultado = monto_a_convertir * tipo_de_cambio_eur_a_mex
    print(f"El monto en pesos mexicanos es: {resultado:.2f}") # sin :.2f el resultado se imprimiría con todos los decimales
elif tipo_de_moneda == "DOLAR":
    resultado = monto_a_convertir * tipo_de_cambio_usd_a_mex
    print(f"El monto en pesos mexicanos es: {resultado:.2f}")
else:
    print("Moneda no reconocida. Por favor, ingresá 'Euro' o 'Dolar'.")

