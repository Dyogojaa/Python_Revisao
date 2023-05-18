import PySimpleGUI as sg

# Layout da janela
layout = [
    [sg.Text('Formulário de Cadastro')],
    [sg.Text('Nome'), sg.Input(key='-NOME-')],
    [sg.Text('Email'), sg.Input(key='-EMAIL-')],
    [sg.Text('Endereço'), sg.Input(key='-ENDEREÇO-')],
    [sg.Listbox(values=[], size=(50, 6), key='-LISTA-')],
    [sg.Button('Adicionar'), sg.Button('Atualizar'), sg.Button('Excluir'), sg.Button('Limpar')]
]

# Cria a janela
window = sg.Window('Cadastro', layout)

# Lista de cadastro
cadastro = []

while True:
    event, values = window.read()
    
    # Se o usuário fechar a janela ou clicar em 'Sair'
    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Adicionar':
        cadastro.append(f"{values['-NOME-']}, {values['-EMAIL-']}, {values['-ENDEREÇO-']}")
        window['-LISTA-'].update(cadastro)
    elif event == 'Atualizar':
        selected_item = values['-LISTA-'][0]
        index = cadastro.index(selected_item)
        cadastro[index] = f"{values['-NOME-']}, {values['-EMAIL-']}, {values['-ENDEREÇO-']}"
        window['-LISTA-'].update(cadastro)
    elif event == 'Excluir':
        selected_item = values['-LISTA-'][0]
        cadastro.remove(selected_item)
        window['-LISTA-'].update(cadastro)
    elif event == 'Limpar':
        window['-NOME-'].update('')
        window['-EMAIL-'].update('')
        window['-ENDEREÇO-'].update('')

window.close()
