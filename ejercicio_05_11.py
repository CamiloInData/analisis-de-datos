import pandas as pd


data = {
    'Producto': ['Manzanas', 'Peras', 'Bananas', 'Naranjas'],
    'Precio': [2.5, 3.0, 1.8, 2.2],
    'Cantidad Vendida': [100, 150, 200, 80],
    'Mes': ['Enero', 'Enero', 'Febrero', 'Febrero']
}

df = pd.DataFrame(data)
print("DataFrame original:")
print(df)

# solo las filas donde el mes sea "Enero"
df_enero = df[df['Mes'] == 'Enero']
print("\nFilas donde el mes es Enero:")
print(df_enero)

# las columnas "Producto" y "Cantidad Vendida"
df_productos_cantidad = df[['Producto', 'Cantidad Vendida']]
print("\nColumnas Producto y Cantidad Vendida:")
print(df_productos_cantidad)

# la columna "Precio" incrementando un 10%
df['Precio'] = df['Precio'] * 1.10
print("\nPrecio incrementado un 10%:")
print(df)

#nueva columna "Ingresos" 
df['Ingresos'] = df['Precio'] * df['Cantidad Vendida']
print("\nDataFrame con columna Ingresos:")
print(df)