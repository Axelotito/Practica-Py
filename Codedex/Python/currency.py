""" Esto es para la cambiar la divisar de un pais a dolares estadounidenses"""

SoPeru = float(input("Cuanto tiene en soles peruanos:"))
PeColom = float(input("Cuanto tiene en pesos colombianos:"))
ReBraz = float(input("Cuanto tiene en monedas brazileña:"))

""" Tasas de cambio actuales a USD (según los datos más recientes disponibles, verifique las tasas actuales) """
peso_colombiano_a_usd = 0.00024
sol_peruano_a_usd = 0.26
real_brasileño_a_usd = 0.18

""" inicializar USD """
USD = 0

""" Calculando el total en USD """
USD += PeColom * peso_colombiano_a_usd
USD += SoPeru * sol_peruano_a_usd
USD += ReBraz * real_brasileño_a_usd

print(f"Tiene {USD} dólares estadounidenses.")