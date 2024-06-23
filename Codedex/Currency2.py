# currency.py
# This program converts amounts from Colombian pesos, Peruvian soles, and Brazilian reais to USD.

# Current exchange rates to USD (as of the latest available data, please verify for current rates)
exchange_rate_colombian_peso_to_usd = 0.00026
exchange_rate_peruvian_sol_to_usd = 0.27
exchange_rate_brazilian_real_to_usd = 0.20

# Asking the user for the amount they have in each currency
colombian_pesos = float(input('What do you have left in pesos? '))
peruvian_soles = float(input('What do you have left in soles? '))
brazilian_reais = float(input('What do you have left in reais? '))

# Calculating the total in USD
total_usd = (colombian_pesos * exchange_rate_colombian_peso_to_usd) + \
            (peruvian_soles * exchange_rate_peruvian_sol_to_usd) + \
            (brazilian_reais * exchange_rate_brazilian_real_to_usd)

# Displaying the result
print(total_usd)