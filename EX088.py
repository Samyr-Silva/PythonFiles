from tkinter import *

def checar():
       n1 = int(resp.get())
       n2 = int(resp2.get())
       resultado = n1 + n2
       soma["text"] = f"A soma é {resultado} "

janela = Tk()
janela.title("Joguinho do botão")
janela.configure(background="green")
texto = Label(janela, text="Número 1:", width=20)
texto.grid(column=0, row=0)

texto2 = Label(janela, text="Número 2:", width=20)
texto2.grid(column=0, row=1)

resp = Entry(janela, background="grey", width=15)
resp.grid(column=1, row=0)

resp2 = Entry(janela, background="grey", width=15)
resp2.grid(column=1, row=1)

soma = Label(janela, text="", width=30)
soma.grid(column=0, row=3)

botao = Button(janela, width=25, background="blue", text="Somar", command=checar)
botao.grid(column=1, row=2)
janela.mainloop()