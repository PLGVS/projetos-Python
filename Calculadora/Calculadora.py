from tkinter import *

#Atribuição das variáveis
total = 0
valor_str = ""
valor1_float = 0
valor2_float = 0
operacao = ""

#Contadores dos botões de operação
cont_operacoes = 0

#Funções dos números
def um():
    global valor_str
    valor_str += "1"
    resultado["text"] = valor_str

def dois():
    global valor_str
    valor_str += "2"
    resultado["text"] = valor_str

def tres():
    global valor_str
    valor_str += "3"
    resultado["text"] = valor_str

def quatro():
    global valor_str
    valor_str += "4"
    resultado["text"] = valor_str

def cinco():
    global valor_str
    valor_str += "5"
    resultado["text"] = valor_str

def seis():
    global valor_str
    valor_str += "6"
    resultado["text"] = valor_str

def sete():
    global valor_str
    valor_str += "7"
    resultado["text"] = valor_str

def oito():
    global valor_str
    valor_str += "8"
    resultado["text"] = valor_str

def nove():
    global valor_str
    valor_str += "9"
    resultado["text"] = valor_str

def zero():
    global valor_str
    valor_str += "0"
    resultado["text"] = valor_str

def c():
    global valor_str, total, operacao, cont_operacoes
    valor_str = ""
    total = 0
    operacao = ""
    cont_operacoes = 0
    resultado["text"] = total

def ponto():
    global valor_str
    valor_str += "."
    resultado["text"] = valor_str

#Funções das operações
def soma():
    global valor1_float, valor_str, operacao, cont_operacoes
    valor1_float = float(valor_str)
    valor_str = ""
    operacao = "soma"
    cont_operacoes += 1

def subtracao():
    global valor1_float, valor_str, operacao, cont_operacoes
    valor1_float = float(valor_str)
    valor_str = ""
    operacao = "subtracao"
    cont_operacoes += 1

def multiplicacao():
    global valor1_float, valor_str, operacao, cont_operacoes
    valor1_float = float(valor_str)
    valor_str = ""
    operacao = "multiplicacao"
    cont_operacoes += 1

def divisao():
    global valor1_float, valor_str, operacao, cont_operacoes
    valor1_float = float(valor_str)
    valor_str = ""
    operacao = "divisao"
    cont_operacoes += 1

#Função do resultado da operação
def igual():
    global valor2_float, valor_str, operacao, total, cont_operacoes
    valor2_float = float(valor_str)
    if operacao == "soma":
        if cont_operacoes <= 1:
            total = valor1_float + valor2_float
        else:
            total += valor2_float
        resultado["text"] = f"{total}"

    if operacao == "subtracao":
        if cont_operacoes <= 1:
            total = valor1_float - valor2_float
        else:
            total -= valor2_float
        resultado["text"] = f"{total}"

    if operacao == "multiplicacao":
        if cont_operacoes <= 1:
            total = valor1_float * valor2_float
        else:
            total *= valor2_float
        resultado["text"] = f"{total}"
    
    if operacao == "divisao":
        if cont_operacoes <= 1:
            total = valor1_float / valor2_float
        else:
            total /= valor2_float
        if total.is_integer() is True:
            resultado["text"] = f"{total:.0f}"
        else:
            resultado["text"] = f"{total}"
        

janela = Tk()
janela.title("Calculadora")
janela.geometry("290x350")
janela.resizable(width = "False", height = "False")

#Resultado
resultado = Label(janela)
resultado["text"] = f"{total}"
resultado["bg"] = "#DCDCDC"
resultado["width"] = "25"
resultado["height"] = "4"
resultado["font"] = ("Arial", 15, "bold")
resultado.place(x = 350, y = 0)
resultado.grid(column = 0, row = 0)

#Botões
botao1 = Button(janela, command = um)
botao1["text"] = "1"
botao1["bg"] = "#D3D3D3"
botao1.grid(column = 0, row = 1)
botao1["height"] = "3"
botao1["width"] = "10"
botao1.place(x = 0, y = 75)

botao2 = Button(janela, command = dois)
botao2["text"] = "2"
botao2["bg"] = "#D3D3D3"
botao2.grid(column = 1, row = 1)
botao2["height"] = "3"
botao2["width"] = "10"
botao2.place(x = 75, y = 75)

botao3 = Button(janela, command = tres)
botao3["text"] = "3"
botao3["bg"] = "#D3D3D3"
botao3.grid(column = 2, row = 1)
botao3["height"] = "3"
botao3["width"] = "10"
botao3.place(x = 150, y = 75)

botaoC = Button(janela, command = c)
botaoC["text"] = "C"
botaoC["bg"] = "#FF4500"
botaoC.grid(column = 2, row = 1)
botaoC["height"] = "3"
botaoC["width"] = "8"
botaoC.place(x = 225, y = 75)

botao4 = Button(janela, command = quatro)
botao4["text"] = "4"
botao4["bg"] = "#D3D3D3"
botao4.grid(column = 0, row = 2)
botao4["height"] = "3"
botao4["width"] = "10"
botao4.place(x = 0, y = 130)

botao5 = Button(janela, command = cinco)
botao5["text"] = "5"
botao5["bg"] = "#D3D3D3"
botao5.grid(column = 1, row = 2)
botao5["height"] = "3"
botao5["width"] = "10"
botao5.place(x = 75, y = 130)

botao6 = Button(janela, command = seis)
botao6["text"] = "6"
botao6["bg"] = "#D3D3D3"
botao6.grid(column = 2, row = 2)
botao6["height"] = "3"
botao6["width"] = "10"
botao6.place(x = 150, y = 130)

botaoDiv = Button(janela, command = divisao)
botaoDiv["text"] = "/"
botaoDiv.grid(column = 3, row = 2)
botaoDiv["height"] = "3"
botaoDiv["width"] = "8"
botaoDiv.place(x = 225, y = 130)

botao7 = Button(janela, command = sete)
botao7["text"] = "7"
botao7["bg"] = "#D3D3D3"
botao7.grid(column = 0, row = 3)
botao7["height"] = "3"
botao7["width"] = "10"
botao7.place(x = 0, y = 185)

botao8 = Button(janela, command = oito)
botao8["text"] = "8"
botao8["bg"] = "#D3D3D3"
botao8.grid(column = 1, row = 3)
botao8["height"] = "3"
botao8["width"] = "10"
botao8.place(x = 75, y = 185)

botao9 = Button(janela, command = nove)
botao9["text"] = "9"
botao9["bg"] = "#D3D3D3"
botao9.grid(column = 1, row = 3)
botao9["height"] = "3"
botao9["width"] = "10"
botao9.place(x = 150, y = 185)

botaoX = Button(janela, command = multiplicacao)
botaoX["text"] = "X"
botaoX.grid(column = 3, row = 3)
botaoX["height"] = "3"
botaoX["width"] = "8"
botaoX.place(x = 225, y = 185)

botaoPonto = Button(janela, command = ponto)
botaoPonto["text"] = "."
botaoPonto.grid(column = 0, row = 4)
botaoPonto["height"] = "3"
botaoPonto["width"] = "10"
botaoPonto.place(x = 0, y = 240)

botao0 = Button(janela, command = zero)
botao0["text"] = "0"
botao0["bg"] = "#D3D3D3"
botao0.grid(column = 1, row = 4)
botao0["height"] = "3"
botao0["width"] = "10"
botao0.place(x = 75, y = 240)

botaoMenos = Button(janela, command = subtracao)
botaoMenos["text"] = "-"
botaoMenos.grid(column = 2, row = 4)
botaoMenos["height"] = "3"
botaoMenos["width"] = "10"
botaoMenos.place(x = 150, y = 240)

botaoMais = Button(janela, command = soma)
botaoMais["text"] = "+"
botaoMais.grid(column = 3, row = 4)
botaoMais["height"] = "3"
botaoMais["width"] = "8"
botaoMais.place(x = 225, y = 240)

botaoIgual = Button(janela, command = igual)
botaoIgual["text"] = "="
botaoIgual["bg"] = "#1E90FF"
botaoIgual.grid(column = 0, row = 5)
botaoIgual["height"] = "3"
botaoIgual["width"] = "40"
botaoIgual.place(x = 0, y = 295)

janela.mainloop()


#Desenvolvido por Pedro Luis Gaspar