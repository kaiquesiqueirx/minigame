import tkinter
from tkinter import *
from tkinter import ttk

import random

# cores 
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca
co2 = "#478CC4"  # azul claro
co3 = "#38576b"  # valor
co4 = "#403d3d"   # letra
co5 = "#e06636"   # - profit
co6 = "#6dd695"   # + profit
co7 = "#ef5350"   # vermelha
co8 = "#00bfa5"   # + verde
co9 = '#FF9897'  # rosa claro
fundo = "#3b3b3b"
co10 ="#fcfbf7"

cor1='#478CC4'
cor2='#ff333a'
cor3='#A6D6C6'
cor4="#ab8918"


janela = Tk()
janela.title('GUESS')
janela.geometry('750x560')
janela.configure(bg=fundo)



# FRAME / JANELA
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=280)

frame_top = Frame(janela, width='750', height='60', bg=co9, pady=0, padx=0, relief='flat')
frame_top.grid(row=1, column=0, sticky=NW)
frame_corpo = Frame(janela, width='750', height='560', bg=fundo, pady=0, padx=0, relief='flat')
frame_corpo.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use('clam')



# configuraçoes do frame de cima
app_nome = Label(frame_top, text='GUESS THE NUMBER', anchor='center', font=('tahoma 25 bold'), bg=co9, fg=co2) # FG (foreground) define cor do texto
app_nome.place(x=215, y=7) # posicao do titulo

global tentativas
global pontuacao  



# funcao iniciar o jogo

tentativas = 5 
pontuacao = 0

def iniciar_jogo():
    l_regra_1['text'] = ''
    l_regra_2['text'] = ''
    l_regra_3['text'] = ''

    numeros = random.sample(range(1,10), 8)
    resposta = random.choice(numeros)

    def estado_do_valor(v):

        numeros = random.sample(range(1,10), 8)
        resposta = [random.choice(numeros)]

        global tentativas
        global pontuacao  
        
        ### global é usada para declarar que uma variável dentro de uma função é global, ou seja, ela se refere a uma variável definida no escopo global (fora de qualquer função). 
        ### Sem essa declaração, a variável seria tratada como local dentro da função, e qualquer tentativa de modificá-la resultaria em erro

        for i in resposta:
            print(i)
            if v == i:
                tentativas += 2
                pontuacao += 10
                l_tentativas['text']=str(tentativas) + 'TRIES'
                l_pontos='SCORE'+ str(pontuacao) 

            else:
                tentativas -= 1
                l_tentativas['text']=str(tentativas) + 'TRIES'

                print(tentativas)
                print(numeros)

                # desabilitanto butoes apos errar tudo
                if tentativas <= 0:
                    b_1['state'] = 'disable'
                    b_2['state'] = 'disable'
                    b_3['state'] = 'disable'
                    b_4['state'] = 'disable'
                    b_5['state'] = 'disable'
                    b_6['state'] = 'disable'
                    b_7['state'] = 'disable'
                    b_8['state'] = 'disable'


                    b_1['text'] = ''
                    b_2['text'] = ''
                    b_4['text'] = ''
                    b_5['text'] = ''
                    b_6['text'] = ''
                    b_7['text'] = ''
                    b_8['text'] = ''

                    # chamar a funcao gameover

                else:
                    pass




    b_1 = Button(frame_corpo,command=lambda:estado_do_valor(numeros[0]), text= numeros[0], width=5, height=2, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
    b_1.place(x=276, y=45) 
    b_2 = Button(frame_corpo,command=lambda:estado_do_valor(numeros[1]), text= numeros[1], width=5, height=2, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
    b_2.place(x=344, y=45)
    b_3 = Button(frame_corpo,command=lambda:estado_do_valor(numeros[2]), text= numeros[2], width=5, height=2, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
    b_3.place(x=412, y=45)
    b_4 = Button(frame_corpo,command=lambda:estado_do_valor(numeros[3]), text= numeros[3], width=5, height=2, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
    b_4.place(x=480, y=45)
    b_5 = Button(frame_corpo,command=lambda:estado_do_valor(numeros[4]), text= numeros[4], width=5, height=2, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
    b_5.place(x=276, y=100)
    b_6 = Button(frame_corpo,command=lambda:estado_do_valor(numeros[5]), text= numeros[5], width=5, height=2, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
    b_6.place(x=344, y=100)
    b_7 = Button(frame_corpo,command=lambda:estado_do_valor(numeros[6]), text= numeros[6], width=5, height=2, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
    b_7.place(x=412, y=100)
    b_8 = Button(frame_corpo,command=lambda:estado_do_valor(numeros[7]), text= numeros[7], width=5, height=2, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE)
    b_8.place(x=480, y=100)




# configuraçoes do frame de baixo
l_pontos = Label(frame_corpo, text='SCORE: 0', anchor='center', font=('Ivy 16 bold'), bg=fundo, fg=co1) 
l_pontos.place(x=77, y=390) # posicao informacao "tentativas" ('l' para simbolizar Label)
l_tentativas = Label(frame_corpo, text='TRIES: 3', anchor='center', font=('Ivy 16 bold'), bg=fundo, fg=co1) 
l_tentativas.place(x=580, y=390)

l_linha = Label(frame_corpo, text='', width=135, anchor='center', font=('Ivy 6'), bg=co2, fg=co1) 
l_linha.place(x=39, y=435)

l_regra_1 = Label(frame_corpo, text='TRY TO GUESS THE NUMBER TO GET POINTS ≧◡≦ ', anchor='center', font=('Ivy 13 bold'), bg=fundo, fg=co1) 
l_regra_1.place(x=175, y=120)

l_regra_2 = Label(frame_corpo, text='IF YOU GET IT RIGHT YOU WIL GET 2 CHANCES', anchor='center', font=('Ivy 13 bold'), bg=fundo, fg=co1) 
l_regra_2.place(x=191, y=150)

l_regra_3 = Label(frame_corpo, text=' IF YOU MAKE A MISTAKE THE CHANCES DECREASE ', anchor='center', font=('Ivy 13 bold'), bg=fundo, fg=co1) 
l_regra_3.place(x=170, y=180)


b_jogar = Button(frame_corpo, command=iniciar_jogo, text= 'PLAY', width=50, font=('Ivy 13 bold'), bg=co2, fg=co0, relief=RAISED, overrelief=RIDGE) 

### RELIEF Controla o estilo da borda do widget no estado normal.
### Os valores possíveis são constantes definidas no Tkinter, como:
### FLAT: Sem borda.
### RAISED: Borda com aparência elevada.
### SUNKEN: Borda com aparência rebaixada.
### GROOVE: Borda com aparência de um sulco.
### RIDGE: Borda com aparência de um relevo
### OVERRELIEF Controla o estilo da borda do widget quando o mouse passa sobre ele (estado "hover").
### Também aceita os mesmos valores que relief.

b_jogar.place(x=140, y=210) 



janela.mainloop()