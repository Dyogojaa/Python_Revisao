import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# Carregar os dados fictícios
data = pd.DataFrame({
    'Categoria': ['ProcessaAtm', 'CargaCitNet', 'IntegraAtm', 'Consumer'],
    'Valor': [100000, 30000, 1000, 500000]
})

# Inicializar o aplicativo Dash
app = dash.Dash(__name__)

# Definir o layout do aplicativo
app.layout = html.Div(children=[
    html.H1(children='Dashboard de Exemplo'),
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': data['Categoria'], 'y': data['Valor'], 'type': 'bar', 'name': 'Categoria'}
            ],
            'layout': {
                'title': 'Gráfico de Barras'
            }
        }
    )
])

# Executar o aplicativo
if __name__ == '__main__':
    app.run_server(debug=True)