
'''

Trabalho Sistemas Operacionais
NOME : Clayton R. Farias
Matrícula : 70879

'''
import time
import threading
from threading import Lock


mutex = Lock()    # Usando mutex binário

R_1 = 0           # Recursos globais R_1 == Recurso R1
R_2 = 0           # Recursos globais R_2 == Recurso R2



class Processos:   ##Classe Processo armazena cada processo com seus respectivos atributos ( Processo , Recurso , Tempo )

    def __init__(self, processo_x , recurso_x ,tempo_x):
        self.processo_x = processo_x
        self.recurso_x = recurso_x
        self.tempo_x = tempo_x

    def Print_Processo(self):

        print("-------------------------------------------------")
        print("Processo : "+str(self.processo_x)+"\nRecurso : "+str(self.recurso_x)+"\nTempo_de_execução : "+str(self.tempo_x))
        print("-------------------------------------------------")

class Fila():  # classe fila responsavel por organizar os processos(processo , recurso , tempo de execução)

    def __init__(self):
        self.fila = []
        self.fila_Executada = []


    def Append_Fila(self,processo):   #Métodos responsaveis pela Fila
        self.fila.append(processo)

    def Print_Fila(self):
        print("--------------------- Fila de Processos -----------------------")
        for i in range(len(self.fila)):
            aux = self.fila[i]
            print(aux.processo_x)
        print("---------------------------------------------------------------")

    def Print_Fila_Detalhada(self):
        print("--------------------- Fila de Processos Detalhada-----------------------")
        for i in range(len(self.fila)):
            aux = self.fila[i]
            print(str(aux.processo_x)+" , "+str(aux.recurso_x)+" , "+str(aux.tempo_x))
        print("---------------------------------------------------------------")

    def Print_Fila_Executados(self):
        print("--------------------- Processos Prontos (EXECUTADOS) -----------------------")
        for i in range(len(self.fila_Executada)):
            aux = self.fila_Executada[i]
            print(aux.processo_x)

        print("---------------------------------------------------------------------------")

    def Pop_Fila(self):
        self.fila.pop()

    def Tamanho_Fila(self):
        tam = len(self.fila)
        return(tam)

    def Append_Processos_Executados(self,processo):
        self.fila_Executada.append(processo)






def Print_arquivo(arquivo):
     print("___________________  Imprimindo processos.txt  _______________________")
     for i in range(len((arquivo))):
         print(str(i) +" "+arquivo[i])
     print("___________________  Imprimindo processos.txt ________________________")


def Processa_comando_PROCESSO(arquivo,posicao_atual):

    fita = arquivo[posicao_atual]

    tam = len(fita)

    pos = fita.index (',')

    return(pos)


def Processa_comando_RECURSO(arquivo,posicao_atual,pos_virgula):

    fita = arquivo[posicao_atual]

    tam = len(fita)

    pos_virgula = pos_virgula + 1

    while pos_virgula < tam:
            if(fita[pos_virgula] == ","):
                pos = pos_virgula
                return(pos)

            pos_virgula = pos_virgula + 1


def abertura_de_arquivo():

    descritor = open("processos.txt","r")

    arquivo = []

    arquivo = descritor.readlines()

    print("Lendo arquivo de entrada ....")
    print(arquivo)
    print("Leitura completa ....")

    descritor.close()

    return(arquivo)


def R1(processo,tempo):

    print("Processo : "+str(processo)+" Executando Recurso R1 tempo de execução : "+str(tempo)+" u.t\n")
    global R_1
    aux = int(tempo)
    R_1 = R_1 + aux


def R2(processo,tempo):

    print("Processo : "+str(processo)+" Executando Recurso R2 tempo de execução : "+str(tempo)+" u.t\n")
    global R_2
    aux = int(tempo)
    R_2 = R_2 + aux


def FIFO(fileira):             #PRONTO

    print("--------------SOLUÇÂO FIFO (FCFS)-------------------")
    media = 0.0
    contador = 0
    media_r1= 0
    media_r2 = 0
    soma_r1 = 0
    somatempr1 = 0
    soma_r2 = 0
    cont_r1 = 0
    cont_r2 = 0
    tam = fileira.Tamanho_Fila()
    print("------ Nr de processos : "+str(tam))


    aux_fileira = fileira.fila
    #print(str(aux_fileira))
    i = 0
    soma = 0

    while (i < (tam)):

        aux = aux_fileira[i]
        #print("aux : " + str(aux.tempo_x))
       #contador = contador + 1

        if(aux.recurso_x == "R1" and (i < (tam))):
           mutex.acquire()
           if(i < tam-1):
               soma_r1 = soma_r1 + int(aux.tempo_x)
               t = threading.Thread(target=R1(aux.processo_x,soma_r1))
               print(str(somatempr1))
           cont_r1 = cont_r1 + 1
           mutex.release()


        if(aux.recurso_x == "R2" and (i < (tam))):
           mutex.acquire()
           if(i < tam-1):
              soma_r2 = soma_r2 + int(aux.tempo_x)
              t = threading.Thread(target=R2(aux.processo_x,soma_r2))
              print(str(soma_r2))
           cont_r2 = cont_r2 + 1
           mutex.release()

        i=i+1

        fileira.Append_Processos_Executados(aux)
        #+fileira.Pop_Fila()


    print("Recursos ------ R1:"+str(R_1) +" R2 :"+str(R_2))

    print("\n\n\n++++++++++++++++++++++++ Processo FIFO ++++++++++++++++++++++++++++=")
    #fileira.Print_Fila()
    fileira.Print_Fila_Executados()

    print("-------------Média R1(R_1 "+str(R_1)+")/"+str(cont_r1) +" : "+str(R_1/cont_r1) +" u.t \n\n\n")
    print("-------------Média R2(R_2 "+str(R_2)+")/"+str(cont_r2) +" : "+str(R_2/cont_r2) +" u.t \n\n\n")
    print("\n\n ---------------------------------------------------------------------___")


def SJF(fileira):

    print('\n\n\n Iniciando Escalonamento SJF  \n\n\n')

    j = 0
    i = 0

    tam = len(fileira.fila)
    lista_tempo_organizada = []


    for i in range(tam):        #salva tempos dos (processos) da Classe(Fila a lista self.fila[]) temporariamente
        aux = fileira.fila[i]
        lista_tempo_organizada.append(int(aux.tempo_x))


    lista_tempo_organizada.sort()     #Organiza em ordem crescente serve como auxilio para executar
    nova_fila = Fila()
    #b = []


    for i in range(tam):
        for j in range(tam):
            aux = fileira.fila[j]      # Pega posição da fileira e testa com a posição da lista auxiliar te tempo
            tempo = int(aux.tempo_x)

            if((lista_tempo_organizada[i] == tempo) and (tempo != 0)): #  salva uma fila auxiliar com os tempos em ordem (Shortest Job First)
               x = Processos(aux.processo_x,aux.recurso_x,aux.tempo_x)
               nova_fila.Append_Fila(x)
               aux.tempo_x = 0


    nova_fila.Print_Fila()
    nova_fila.Print_Fila_Detalhada()

    i = 0
    contador = 0
    media_r1= 0
    media_r2 = 0
    soma_r1 = 0
    soma_r2 = 0
    cont_r1 = 0
    cont_r2 = 0
    tam = nova_fila.Tamanho_Fila()

    while (i < (tam)):       #Executa a fila de prontos

        aux = nova_fila.fila[i]
        contador = contador + 1


        if(aux.recurso_x == "R1" and (i < (tam))):
           mutex.acquire()
           if(i < tam-1):
               soma_r1 = soma_r1 + int(aux.tempo_x)
               t = threading.Thread(target=R1(aux.processo_x,soma_r1))
               print("R1 :"+str(soma_r1))
               print("R_1: " +str(R_1))
           cont_r1 = cont_r1 + 1
           mutex.release()


        if(aux.recurso_x == "R2" and (i < (tam))):
           mutex.acquire()
           if(i < tam-1):
              soma_r2 = soma_r2 + int(aux.tempo_x)
              t = threading.Thread(target=R2(aux.processo_x,soma_r2))
              print("R2 :"+str(soma_r2))
           cont_r2 = cont_r2 + 1
           mutex.release()




        i = i+1

    print("-----------------SJF-------------------------------------")
    fileira.Append_Processos_Executados(aux)
    print("Recursos utilizados \nR1:"+str(R_1) +"\nR2:"+str(R_2))
    #media = media / tam
    print("-------------Média R1 "+str(R_1) +" : "+ str(R_1/cont_r1) +" u.t \n\n\n")
    print("-------------Média R2 "+str(R_2) +": "+str(R_2/cont_r2) +" u.t \n\n\n")

    print("--------------------------------- END SJF ----------------------------------------------")

def Main():

    print("----------------- Trabalho de S.O ------------------------------")

    arquivo = abertura_de_arquivo()

    Print_arquivo(arquivo)

    tamanho_arquivo = len(arquivo)

    print("Tamanho do Arquivo linhas : "+str(tamanho_arquivo))

    fila = Fila()

    for i in range(tamanho_arquivo):

        fita = arquivo[i]

        virgula_um  = Processa_comando_PROCESSO(arquivo,i)

        virgula_segunda  = Processa_comando_RECURSO(arquivo,i,virgula_um)

        x = Processos((fita[0:virgula_um]),fita[virgula_um+1:virgula_segunda] ,fita[virgula_segunda+1:len(fita)-1])

        fila.Append_Fila(x)


    digito = input("\n\n\nDigite o método de escalonamento \n1-FIFO \n2-SJF \nDigite qual opção você deseja : ")

    if(digito == "1"):
            FIFO(fila)

    if(digito == "2"):
            SJF(fila)







Main()
