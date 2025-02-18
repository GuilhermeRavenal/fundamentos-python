# Dados de população e área
sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

# Cálculo da densidade populacional
sf_density = sf_population / sf_area
rio_density = rio_population / rio_area

# Arredondando os valores para 2 casas decimais
sf_density = round(sf_density, 2)
rio_density = round(rio_density, 2)

# Comparação usando operadores lógicos
if sf_density > rio_density:
    resultado = "San Francisco has a denser population than Rio!"
elif sf_density < rio_density:
    resultado = "Rio has a denser population than San Francisco!"
else:
    resultado = "Both cities have the same population density!"

# Exibindo os resultados
print(resultado)
print(f"San Francisco Density: {sf_density} people/km²")
print(f"Rio de Janeiro Density: {rio_density} people/km²")

# Verificando se a densidade de São Francisco é maior que 3000 hab/km²
if sf_density > 3000:
    print("San Francisco is a highly dense city!")
