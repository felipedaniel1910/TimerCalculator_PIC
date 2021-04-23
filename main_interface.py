#importando bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#=======criar nossa janela========

jan= Tk()
jan.title("Calculo - Timer")
jan.geometry("600x300")
jan.configure(background= "white")
jan.resizable(width=False, height=False)

#========Wifgets================
MainFrame = Frame(jan, width=600, height=300, bg="#49A", relief="raise")
MainFrame.pack(side=LEFT)

#=======Escrita para usuário-TIME========
TimeLabel = Label(MainFrame, text= "Tempo a ser contado:", font=("Century Gothic",20), bg="#49A",fg="White") #fg é a cor de fonte
TimeLabel.place(x=30, y=20)

#=========Entrada de dados-TIME==========
TimeEntry = ttk.Entry(MainFrame,justify=CENTER, width=20)
TimeEntry.place(x=435, y=33)

#=======Escrita para usuário-BITS========
BitsLabel = Label(MainFrame, text= "Num. de bits do contador:", font=("Century Gothic",20), bg="#49A",fg="White") #fg é a cor de fonte
BitsLabel.place(x=30, y=60)

#=========Entrada de dados-BITS==========
BitsEntry = ttk.Entry(MainFrame,justify=CENTER, width=20)
BitsEntry.place(x=435, y=73)

#=======Escrita para usuário-PRESCALER========
PrescLabel = Label(MainFrame, text= "Prescaler utilizado:", font=("Century Gothic",20), bg="#49A",fg="White") #fg é a cor de fonte
PrescLabel.place(x=30, y=100)

#=========Entrada de dados-PRESCALER==========
PrescEntry = ttk.Entry(MainFrame,justify=CENTER, width=20)
PrescEntry.place(x=435, y=113)

#=======Escrita para usuário-FREQUENCIA========
FreqLabel = Label(MainFrame, text= "Frequência utilizada:", font=("Century Gothic",20), bg="#49A",fg="White") #fg é a cor de fonte
FreqLabel.place(x=30, y=140)

#=========Entrada de dados-FREQUENCIA==========
FreqEntry = ttk.Entry(MainFrame,justify=CENTER, width=20)
FreqEntry.place(x=435, y=153)

#=====Função que realiza o calculo===========
def Calculate():

    timer = float(TimeEntry.get())
    bits = int(BitsEntry.get())
    prescaler = int(PrescEntry.get())
    freq = float(FreqEntry.get())

    carga = (timer-4*(1/freq)*prescaler*(2**bits))/-(4*(1/freq)*prescaler)

    carga = round(carga)
    carga = hex(carga)

    #=======Escrita para usuário-TMR0========
    TMRLabel = Label(MainFrame, text= "TMR:", font=("Century Gothic",20), bg="#49A",fg="White") #fg é a cor de fonte
    TMRLabel.place(x=30, y=200)

    #=======Escrita para usuário-TMR0========
    CLabel = Label(MainFrame, text= carga[2:6].upper(), font=("Century Gothic",20), bg="#49A",fg="White") #fg é a cor de fonte
    CLabel.place(x=100, y=200)

#=========Botão OK================
OkButton = ttk.Button(MainFrame, text ="OK", width = 20, command= Calculate)
OkButton.place(x=435, y=220)

jan.mainloop()
