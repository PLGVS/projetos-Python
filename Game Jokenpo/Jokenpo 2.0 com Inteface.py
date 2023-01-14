import random
from tkinter import *
vitorias_pc = 0
vitorias_jogador = 0

def pedra():
    #Condições caso o usuário escolha Pedra
    global vitorias_pc
    global vitorias_jogador
    escolha_pc = ['Pedra', 'Papel', 'Tesoura']
    escolhido_pc = random.choice(escolha_pc)
    escolha = 'Pedra'
    if escolhido_pc == 'Tesoura':
        resultado["text"] = f"Pedra VS {escolhido_pc}\nVITÓRIA!!!"
        vitorias_jogador += 1
    elif escolhido_pc == 'Papel':
        resultado["text"] = f"Pedra VS {escolhido_pc}\nDERROTA!!!"
        vitorias_pc += 1
    elif escolhido_pc == 'Pedra':
        resultado["text"] = f"Pedra VS {escolhido_pc}\nEMPATE!!!"

    pontuacao["text"] = f"Vitórias:\nVocê:{vitorias_jogador} \nPC:{vitorias_pc}"

def papel():
    #Condições caso o usuário escolha Papel
    global vitorias_pc
    global vitorias_jogador
    escolha_pc = ['Pedra', 'Papel', 'Tesoura']
    escolhido_pc = random.choice(escolha_pc)
    escolha = 'Papel'
    if escolhido_pc == 'Pedra':
        resultado["text"] = f"Papel VS {escolhido_pc}\nVITÓRIA!!!"
        vitorias_jogador += 1
    elif escolhido_pc == 'Tesoura':
        resultado["text"] = f"Papel VS {escolhido_pc}\nDERROTA!!!"
        vitorias_pc += 1
    elif escolhido_pc == 'Papel':
        resultado["text"] = f"Papel VS {escolhido_pc}\nEMPATE!!!"
    
    pontuacao["text"] = f"Vitórias:\nVocê:{vitorias_jogador} \nPC:{vitorias_pc}"

def tesoura():
    #Condições caso o usuário escolha Tesoura
    global vitorias_pc
    global vitorias_jogador
    escolha_pc = ['Pedra', 'Papel', 'Tesoura']
    escolhido_pc = random.choice(escolha_pc)
    escolha = 'Tesoura'
    if escolhido_pc == 'Papel':
        resultado["text"] = f"Tesoura VS {escolhido_pc}\nVITÓRIA!!!"
        vitorias_jogador += 1
    elif escolhido_pc == 'Pedra':
        resultado["text"] = f"Tesoura VS {escolhido_pc}\nDERROTA!!!"
        vitorias_pc += 1
    elif escolhido_pc == 'Tesoura':
        resultado["text"] = f"Tesoura VS {escolhido_pc}\nEMPATE!!!"
    
    pontuacao["text"] = f"Vitórias:\nVocê:{vitorias_jogador} \nPC:{vitorias_pc}"
    
janela = Tk()
janela.title("Pedra, Papel ou Tesoura")
janela.configure(bg = "black")
janela.geometry("450x600")

#Contador da pontuação
pontuacao = Label(janela)
pontuacao["text"] = pontuacao["text"] = f"Vitórias:\nVocê:{vitorias_jogador} \nPC:{vitorias_pc}"
pontuacao["font"] = ("Arial", 12)
pontuacao["background"] = "yellow"
pontuacao.grid(column = 1, row = 0, pady = 10, padx = 10)

#Logo de fundo
logo = PhotoImage(file = "images/logo.png")
logo = logo.subsample(1, 1)
figura1 = Label(image = logo, bg = "black")
figura1.grid(column = 0, row = 0, padx = (50, 0))

#Botões de opção
pedra = Button(janela, command = pedra)
pedra["text"] = "Pedra"
pedra["background"] = "yellow"
pedra["font"] = ("Arial", 12)
pedra["height"] = 2
pedra["width"] = 10
pedra.grid(column = 0, row = 1, pady = 10, padx = (50, 0))

papel = Button(janela, command = papel)
papel["text"] = "Papel"
papel["background"] = "yellow"
papel["font"] = ("Arial", 12)
papel["height"] = 2
papel["width"] = 10
papel.grid(column = 0, row = 2, pady = 10, padx = (50, 0))

tesoura = Button(janela, command = tesoura)
tesoura["text"] = "Tesoura"
tesoura["background"] = "yellow"
tesoura["font"] = ("Arial", 12)
tesoura["height"] = 2
tesoura["width"] = 10
tesoura.grid(column = 0, row = 3, pady = 10, padx = (50, 0))

#Texto que anuncia o resultado
resultado = Label(janela)
resultado["text"] = ""
resultado["font"] = ("Arial", 20)
resultado["fg"] = "yellow"
resultado["background"] = "black"
resultado.grid(column = 0, row = 4, pady = 10, padx = (50, 0))

#Assinatura
assinatura = Label(janela)
assinatura["text"] = "Desenvolvido por Pedro Luis Gaspar"
assinatura["font"] = ("Arial", 12, "italic")
assinatura["fg"] = "yellow"
assinatura["background"] = "black"
assinatura.grid(column = 0, row = 5, pady = 10, padx = (0, 100))

janela.mainloop()