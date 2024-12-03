import hashlib
import time
import random
import threading
import logging

# Parâmetros do algoritmo PoW
TARGET_PREFIX = "0000"  # O hash deve começar com "0000"
MAX_NONCE = 1000000     # Máximo de tentativas para encontrar a solução
FAILURE_RATE = 0.2      # Taxa de falha dos nós (20%)

# Configuração de logs
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(message)s')

class Miner(threading.Thread):
    def __init__(self, miner_id, coordinator):
        super().__init__()
        self.miner_id = miner_id
        self.nonce = 0
        self.block_data = "block_data_example"
        self.found = False
        self.coordinator = coordinator  # Referência para o nó coordenador

    def mine(self):
        while self.nonce < MAX_NONCE and not self.found:
            if random.random() < FAILURE_RATE:  # Simula falha de nó aleatória
                logging.warning(f"Miner {self.miner_id} falhou e será recuperado.")
                time.sleep(random.randint(1, 3))  # Simula tempo de recuperação
                logging.info(f"Miner {self.miner_id} foi recuperado.")
            
            nonce_str = f"{self.block_data}{self.nonce}"
            hash_result = hashlib.sha256(nonce_str.encode()).hexdigest()

            if hash_result.startswith(TARGET_PREFIX):
                self.found = True
                logging.info(f"Miner {self.miner_id} encontrou a solução: {hash_result} com nonce: {self.nonce}")
                self.coordinator.broadcast_solution(hash_result, self.miner_id)
                return hash_result

            self.nonce += 1

        if not self.found:
            logging.info(f"Miner {self.miner_id} não encontrou a solução após {MAX_NONCE} tentativas.")
        return None

    def run(self):
        """Executa o processo de mineração em segundo plano."""
        logging.info(f"Miner {self.miner_id} iniciou a mineração.")
        self.mine()

class Coordinator:
    def __init__(self):
        self.miners = []
        self.block = "block_data_example"
        self.lock = threading.Lock()

    def add_miner(self, miner):
        self.miners.append(miner)

    def broadcast_solution(self, solution, miner_id):
        """Recebe uma solução de um minerador e transmite para os outros."""
        with self.lock:
            logging.info(f"Coordenador recebeu a solução de Miner {miner_id}: {solution}")
            for miner in self.miners:
                if miner.miner_id != miner_id:
                    logging.info(f"Coordenador enviando solução para Miner {miner.miner_id}")
                    # Simulação de envio de solução para outros mineradores
                    miner.nonce = MAX_NONCE  # Encerrar mineração para outros mineradores

def simulate_mining():
    coordinator = Coordinator()

    # Criando mineradores
    miners = [Miner(i, coordinator) for i in range(4)]  # 4 mineradores competindo

    # Adiciona mineradores ao coordenador
    for miner in miners:
        coordinator.add_miner(miner)

    # Inicia os mineradores
    for miner in miners:
        miner.start()

    # Espera todos os mineradores terminarem
    for miner in miners:
        miner.join()

if __name__ == "__main__":
    start_time = time.time()
    simulate_mining()
    end_time = time.time()
    
    logging.info(f"\nTempo total de execução: {end_time - start_time:.2f} segundos")
