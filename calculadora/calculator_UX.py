from tkinter import Tk, Entry, Button

# Função para calcular o resultado
def calcular():
    try:
        expressao = entrada.get()
        resultado = eval(expressao)
        entrada.delete(0, "end")
        entrada.insert("end", str(resultado))
    except Exception:
        entrada.delete(0, "end")
        entrada.insert("end", "Erro")

# Função para limpar a entrada
def limpar():
    entrada.delete(0, "end")

# Configuração da janela principal
janela = Tk()
janela.title("Calculadora")

# Configuração da entrada de texto
entrada = Entry(janela, width=25, justify="right")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Configuração dos botões
botoes = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("C", 4, 2), ("+", 4, 3)
]

for texto, linha, coluna in botoes:
    if texto == "C":
        botao = Button(janela, text=texto, width=5, height=2, command=limpar)
    else:
        botao = Button(janela, text=texto, width=5, height=2, command=lambda texto=texto: entrada.insert("end", texto))
    botao.grid(row=linha, column=coluna)

botao_calcular = Button(janela, text="=", width=25, height=2, command=calcular)
botao_calcular.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

# Iniciar o loop principal da aplicação
janela.mainloop()
