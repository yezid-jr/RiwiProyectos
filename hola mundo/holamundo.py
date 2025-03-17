import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg") 
archivo_leer = "/home/Coder/Documentos/Sample Data v3/Inventory_v2.csv"
df = pd.read_csv(archivo_leer)

# print(djia_data.head())
plt.figure(figsize=(12, 6))
plt.bar(df["product.partNumber"], df["quantity"], color="royalblue")
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.title("Inventario de Productos")
plt.xticks(rotation=90)  # Rotar nombres para mejor lectura
plt.ion()
plt.pause(10)
plt.show()