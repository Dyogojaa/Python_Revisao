from flask import Flask
from dash import Dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
from sqlalchemy import create_engine
import plotly.graph_objs as go

# Configurar conexão SQL
DATABASE = 'dbcit_tokio'
USERNAME = 'sa'
PASSWORD = 'S6metrias#@'
SERVER = 'localhost'
DRIVER = 'SQL+Server'
DATABASE_CONNECTION = f'mssql+pyodbc://{USERNAME}:{PASSWORD}@{SERVER}/{DATABASE}?driver={DRIVER}'

engine = create_engine(DATABASE_CONNECTION)
connection = engine.connect()

# Consultas SQL
query_embarques_por_minuto = "SELECT * FROM tb_cte_jso_atm"  # Atualize com sua consulta SQL
query_inconsistencias_por_data = "SELECT * FROM tb_cte_jso_atm"  # Atualize com sua consulta SQL
query_embarques_por_dia = "SELECT * FROM tb_cte_jso_atm"  # Atualize com sua consulta SQL

# Buscar dados
df_embarques_por_minuto = pd.read_sql_query(query_embarques_por_minuto, connection)
df_inconsistencias_por_data = pd.read_sql_query(query_inconsistencias_por_data, connection)
df_embarques_por_dia = pd.read_sql_query(query_embarques_por_dia, connection)

# Fechar conexão
connection.close()

# Iniciar a aplicação
server = Flask(__name__)
app = Dash(__name__, server=server)

# Layout da aplicação
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Embarques'),

    dcc.Graph(
        id='graph1',
        figure={
            'data': [
                go.Bar(
                    x=df_embarques_por_minuto['minute'],  # Atualize com o nome da sua coluna
                    y=df_embarques_por_minuto['total'],  # Atualize com o nome da sua coluna
                    name='Embarques por minuto'
                )
            ]
        }
    ),

    dcc.Graph(
        id='graph2',
        figure={
            'data': [
                go.Scatter(
                    x=df_inconsistencias_por_data['date'],  # Atualize com o nome da sua coluna
                    y=df_inconsistencias_por_data['total'],  # Atualize com o nome da sua coluna
                    name='Inconsistências por data'
                )
            ]
        }
    ),

    html.Table(
        id='table',
        children=[
            html.Tr([html.Th(col) for col in df_embarques_por_dia.columns])] +  # Cabeçalhos
            [html.Tr([html.Td(df_embarques_por_dia.iloc[i][col]) for col in df_embarques_por_dia.columns]) for i in range(len(df_embarques_por_dia))]
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
