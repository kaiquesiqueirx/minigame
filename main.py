import tkinter
from tkinter import *
from tkinter import ttk



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
app_nome.place(x=215, y=0) # posicao do titulo



# configuraçoes do frame de baixo
l_pontos = Label(frame_corpo, text='SCORE: 0', anchor='center', font=('Ivy 16 bold'), bg=fundo, fg=co1) 
l_pontos.place(x=77, y=390) # posicao informacao "tentativas" ('l' para simbolizar Label)
l_tentativas = Label(frame_corpo, text='TRIES: 3', anchor='center', font=('Ivy 16 bold'), bg=fundo, fg=co1) 
l_tentativas.place(x=580, y=390)

l_linha = Label(frame_corpo, text='', width=135, anchor='center', font=('Ivy 6'), bg=cor3, fg=co1) 
l_linha.place(x=39, y=435)

l_regra_1 = Label(frame_corpo, text='TRY TO GUESS THE NUMBER TO GET POINTS ≧◡≦ ', anchor='center', font=('Ivy 13 bold'), bg=fundo, fg=co1) 
l_regra_1.place(x=175, y=120)




janela.mainloop()

