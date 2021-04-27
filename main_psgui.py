import PySimpleGUI as sg

class Telapython:
    
    def __init__(self):

        sg.change_look_and_feel('GreenMono') #muda o stilo da janela
        #layout
        layout = [
        [sg.Text('Tempo em ms:',size=(5,0)),sg.Input(size=(30,0), key='timer')], 
        [sg.Text('Qual o numero de bits do contador?')],
        [sg.Radio('8bits','contador',key='c8'),sg.Radio('16bits','contador',key='c16')],
        [sg.Text('Qual o prescaler utilizado?')],
        [sg.Radio('32','pscaler',key='p32'),sg.Radio('64','pscaler',key='p64'),sg.Radio('128','pscaler',key='p128'),sg.Radio('256','pscaler',key='p256')],
        [sg.Text('Qual a frequência utilizada?')],
        [sg.Radio('8MHz','freq',key='f8'),sg.Radio('10MHz','freq',key='f10'),sg.Radio('16Mhz','freq',key='f16'),sg.Radio('20MHz','freq',key='f20')],
        [sg.Button("Calcular")],     
        #logs - mostram as informações que estão sendo extraídas
        [sg.Output(size=(40,10))] 
        ]

        #criação da janela
        self.janela = sg.Window("Cálculo pré-carregamento").layout(layout)

    def iniciar(self):
        while True:
            self.button, self.values = self.janela.Read() #faz rodar apenas 1 vez no loop e aguardar novos dados
            timer = float(self.values['timer'])
            timer = timer/1000
            
            
            if self.values['c8'] == True:
                bits = 8
            elif self.values['c16'] == True:
                    bits = 16   
            
            if self.values['p32'] == True:
                prescaler = 32
            elif self.values['p64'] == True:
                prescaler = 64  
            elif self.values['p128'] == True:
                prescaler = 128  
            elif self.values['p256'] == True:
                prescaler = 256  
           
            if self.values['f8'] == True:
                freq = 8e6
            elif self.values['f10'] == True:
                freq = 10e6 
            elif self.values['f16'] == True:
                freq = 16e6
            elif self.values['f20'] == True:
                freq = 20e6 

            carga = (timer-4*(1/freq)*prescaler*(2**bits))/-(4*(1/freq)*prescaler)

            carga = round(carga)
            carga = hex(carga)

            print("\n TMR0H = ",carga[2:4].upper()," e TMR0L = ",carga[4:6].upper())

tela = Telapython()
tela.iniciar()
