from operator import index
import mysql.connector
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
conexion = mysql.connector.connect(

    host="localhost",
    user="root",
    password="",
    database="techmarket"
)

query = "SELECT * FROM ventas;"
df_mysql = pd.read_sql(query,conexion)
conexion.close()

print(df_mysql.head())

print("Excel data")
# cargar datos del excel


df_excel = pd.read_excel("productos.xlsx", sheet_name="productos")
print(df_excel.head())

# limpiar datos

df_mysql["ciudad"] = df_mysql["ciudad"].str.strip().str.title()
df_excel["categoría"] = df_excel["categoría"].str.strip().str.title()

#revisar valores nulos o duplicados
print("Valores Nullos")
print(df_mysql.isnull().sum())
df_mysql.drop_duplicates(inplace=True)

#unir conjuntos de datos

df_merged = pd.merge(df_mysql,df_excel, on="producto_id",how="left")

print("Merged")
print(df_merged.head())

#Crear campos derivados


df_merged["mes"] = pd.to_datetime(df_merged["fecha"]).dt.month_name()
df_merged["año"] = pd.to_datetime(df_merged["fecha"]).dt.year
df_merged["ingreso_total"] = df_merged["cantidad"] * df_merged["valor_total"]


#Carga y modelado

df_merged.to_csv("ventas_limpias.csv", index=False)


# dashboard

app = Dash(__name__)

# Gráfico 1: Ventas por categoría
fig_categoria = px.bar(df_merged.groupby('categoría')['ingreso_total'].sum().reset_index(),
                       x='categoría', y='ingreso_total', title='Ventas por Categoría')

# Gráfico 2: Tendencia mensual
fig_mes = px.line(df_merged.groupby('mes')['ingreso_total'].sum().reset_index(),
                  x='mes', y='ingreso_total', title='Tendencia de Ventas Mensuales')

# Gráfico 3: Ventas por ciudad
fig_ciudad = px.pie(df_merged, values='ingreso_total', names='ciudad', title='Distribución por Ciudad')

# Layout del Dashboard
app.layout = html.Div([
    html.H1("Dashboard de Ventas - TechMarket"),
    dcc.Graph(figure=fig_categoria),
    dcc.Graph(figure=fig_mes),
    dcc.Graph(figure=fig_ciudad)
])

if __name__ == "__main__":
    app.run(debug=True)

