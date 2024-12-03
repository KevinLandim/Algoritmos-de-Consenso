Algoritmo de Consenso: Proof of Work (PoW) - Implementação Simulada
Este projeto implementa uma simulação simples do algoritmo Proof of Work (PoW), utilizado em sistemas distribuídos e blockchains, como o Bitcoin. O código simula a mineração de blocos por múltiplos mineradores, com um nó coordenador para gerenciar a comunicação entre os nós participantes. Também simula falhas nos nós e a recuperação desses nós, além de registrar logs detalhados de cada fase do algoritmo.

Descrição do Projeto
Este projeto implementa o algoritmo Proof of Work (PoW) em um ambiente distribuído com a seguinte estrutura:

Nó Coordenador: Um nó central que gerencia a comunicação entre os mineradores e encerra a mineração quando um minerador encontra a solução.
Mineradores: Vários mineradores competem para resolver o problema computacional (mineração de um bloco) tentando encontrar um hash que atenda a um critério específico.
Falhas de Nó: Os mineradores podem falhar aleatoriamente com uma taxa de falha configurável. Quando um nó falha, ele é recuperado após um tempo aleatório, e o sistema tenta continuar a mineração.
Logs Detalhados: O sistema gera logs detalhados de todas as operações realizadas, incluindo tentativas de mineração, falhas e recuperações de nós.
Algoritmo Implementado
O algoritmo implementado é o Proof of Work (PoW), utilizado principalmente em blockchains. O PoW funciona de forma que mineradores competem para resolver um problema de cálculo (encontrar um hash que atenda a um critério específico, como começar com um prefixo "0000"). O minerador que encontrar a solução primeiro propaga essa solução para os outros mineradores e o processo é encerrado.

Como Funciona
Mineradores: Cada minerador tenta encontrar um hash do bloco concatenado com um número (nonce) que atenda ao critério de começar com um prefixo específico (neste caso, "0000").
Coordenador: O coordenador recebe a solução de um minerador, propaga a solução para os outros mineradores e encerra a mineração.
Falhas e Recuperação: Durante o processo de mineração, nós podem falhar aleatoriamente com uma taxa configurável. Quando um nó falha, ele é recuperado após um tempo aleatório e o processo de mineração continua.
Logs Detalhados: Logs são registrados em todas as fases do algoritmo: início da mineração, solução encontrada, falhas e recuperações.
