import pandas as pd
import numpy as np

# Crear los datos del archivo productos.csv
datos = {
    'Producto': ['Pan', 'Leche', 'Huevos', 'Arroz', 'Café', 'Jugo', 'Yogurt', 'Azúcar', 'Galleta'],
    'Categoria': ['Abarrotes', 'Lácteos', 'Abarrotes', 'Abarrotes', 'Bebidas', 'Bebidas', 'Lácteos', 'Abarrotes', 'Abarrotes'],
    'Cantidad': [10, 20, 30, 15, 8, 7, 10, 12, 5],
    'Precio': [2000, 3500, 500, 2500, 8000, None, 2000, 1500, 1200]
}

# Crear el DataFrame
df = pd.DataFrame(datos)

# Guardar el archivo CSV
df.to_csv('productos.csv', index=False)

print("✅ Archivo 'productos.csv' creado correctamente.")

ruta = "productos.csv"




df = pd.read_csv(ruta)


print(df.head())


(df.head(3))

(df.info())

(df.describe())