class PC:
    def __init__(self, marca:str, processador:str, memoria_ram:int, placa_grafica:str):
        self.__marca = marca
        self.__processador = processador
        self.__memoria_ram = memoria_ram
        self.__placa_grafica = placa_grafica
        self.__ligado = False

    @property
    def marca(self):
        return self.__marca

    @property
    def processador(self):
        return self.__processador

    @processador.setter
    def processador(self, novo_processador):
        self.__processador = novo_processador

    @property
    def memoria_ram(self):
        return self.__memoria_ram

    @memoria_ram.setter
    def memoria_ram(self, nova_memoria):
        self.__memoria_ram = nova_memoria

    @property
    def placa_grafica(self):
        return self.__placa_grafica

    @placa_grafica.setter
    def placa_grafica(self, nova_placa):
        self.__placa_grafica = nova_placa

    @property
    def ligado(self):
        return self.__ligado

    def ligar(self):
        if(self.__ligado == False):
            self.__ligado = True
            return print("O pc está ligando...")
        else:
            print("O pc já está ligado.")

    def desligar(self):
        if(self.__ligado == True):
            self.__ligado = False
            return print("O pc está desligando...")
        else:
            print("O computador já está desligado.")

    def upgrade(self):
        print("-"*20,"(1)Processador", "(2)Memória RAM", "(3)Placa de Vídeo", "-"*20, sep="\n")
        upgrade = int(input("Digite o componente que deseja trocar: "))

        if(upgrade == 1):
            novo_componente = input("Digite o novo processador: ")
            self.processador = novo_componente
        elif(upgrade == 2):
            novo_componente = int(input("Digite a nova memória RAM: "))
            self.memoria_ram = novo_componente
        elif(upgrade == 3):
            novo_componente = input("Digite a nova placa de vídeo: ")
            self.placa_grafica = novo_componente
        else:
            return print("Valor inválido.")
        
    