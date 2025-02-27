import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar los datos
pokemon = pd.read_csv("/Users/joseg/Desktop/pokemon.csv")# cambia por la ruta por la de tu archivo csv

# Verificar nombres de columnas
print(pokemon.columns)

# Explorar la estructura de los datos
print(pokemon.info())

# Ver las primeras filas
print(pokemon.head())

# Resumen estadístico
print(pokemon.describe())

# Asegurar que la columna 'is_legendary' es booleana
pokemon['is_legendary'] = pokemon['is_legendary'].astype(bool)

# Análisis de tipos primarios
tipo_primario_count = pokemon['type1'].value_counts()
print("Cantidad de Pokémon por tipo primario:")
print(tipo_primario_count)

# Gráfico de barras para tipos primarios
plt.figure(figsize=(12, 6))
tipo_primario_count.plot(kind='bar', color='skyblue')
plt.title("Distribución de Tipos Primarios")
plt.xlabel("Tipo")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.show()

# Análisis de Pokémon legendarios
legendarios = pokemon[pokemon['is_legendary']]
print("Cantidad de Pokémon legendarios:", len(legendarios))

# Resumen de estadísticas base de Pokémon legendarios
print("Resumen de estadísticas base de Pokémon legendarios:")
print(legendarios[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']].describe())

# Gráfico de caja para comparar estadísticas base
plt.figure(figsize=(10, 6))
sns.boxplot(data=legendarios[['hp', 'attack', 'defense', 'sp_attack', 'sp_defense', 'speed']], palette="Greens")
plt.title("Estadísticas Base de Pokémon Legendarios")
plt.show()

# Análisis de la relación entre altura y peso
plt.figure(figsize=(8, 6))
plt.scatter(pokemon['height_m'], pokemon['weight_kg'], color='orange', alpha=0.6)
plt.title("Relación entre Altura y Peso")
plt.xlabel("Altura (m)")
plt.ylabel("Peso (kg)")
plt.show()

# Correlación entre altura y peso
correlacion = pokemon[['height_m', 'weight_kg']].dropna().corr().iloc[0, 1]
print(f"Correlación entre altura y peso: {correlacion:.2f}")

