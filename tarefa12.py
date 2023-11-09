import threading
import time

# Definindo a classe para representar um processo no algoritmo de eleição
class Processo:
    def __init__(self, id):
        self.id = id
        self.eleicao_em_andamento = False
        self.lider_atual = None

    # Método para iniciar uma eleição
    def iniciar_eleicao(self):
        self.eleicao_em_andamento = True
        self.lider_atual = None
        print(f"Processo {self.id} iniciou uma eleição.")

        # Enviar mensagens de eleição para processos com IDs maiores
        for processo in processos:
            if processo.id > self.id:
                processo.responder_elec()

        # Simular um tempo limite para receber respostas
        time.sleep(2)

        # Se nenhum líder foi escolhido, o processo atual se torna o líder
        if self.lider_atual is None:
            self.se_tornar_lider()
        else:
            print(f"Processo {self.id} recebeu um líder: Processo {self.lider_atual.id}")
        self.eleicao_em_andamento = False

    # Método para responder a uma mensagem de eleição
    def responder_elec(self):
        if self.eleicao_em_andamento:
            print(f"Processo {self.id} respondeu à eleição com 'OK'")
            self.lider_atual = processos[self.id - 1]

    # Método para se tornar o líder
    def se_tornar_lider(self):
        self.lider_atual = self
        print(f"Processo {self.id} se tornou o líder!")

# Função executada por cada thread representando um processo
def executar_eleicao(processo_id):
    processo = processos[processo_id - 1]

    # Loop principal do processo para iniciar eleições em momentos diferentes
    while not parar_programa:
        time.sleep(5)  # Simular intervalo entre eleições
        if not processo.eleicao_em_andamento:
            processo.iniciar_eleicao()

# Criando instâncias da classe Processo para representar os processos
processos = [Processo(1), Processo(2), Processo(3), Processo(4), Processo(5)]

# Iniciando threads separadas para cada processo
threads = []
parar_programa = False

for processo in processos:
    thread = threading.Thread(target=executar_eleicao, args=(processo.id,))
    threads.append(thread)
    thread.start()

# Aguardando a entrada do usuário para encerrar o programa
input("Pressione Enter para encerrar o programa.\n")
parar_programa = True

# Aguardando todas as threads serem concluídas antes de encerrar o programa
for thread in threads:
    thread.join()
