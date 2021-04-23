

timer = float(input("Digite o tempo a ser contado: "))
bits = int(input("Digite o numero de bits do contador: "))
prescaler = int(input("Digite o prescaler usado: "))
freq = float(input("Digite a frequencia do oscilador: "))
           
           
carga = (timer-4*(1/freq)*prescaler*(2**bits))/-(4*(1/freq)*prescaler)

carga = round(carga)
carga = hex(carga)

print("\nTMR0H = ",carga[2:4].upper()," e TMR0L = ",carga[4:6].upper())

input("\nPressione qualquer tecla para sair...")
