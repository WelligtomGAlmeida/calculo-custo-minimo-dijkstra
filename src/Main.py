from src.Graph import Graph


if __name__ == '__main__':
    grafo = Graph()
    no_origem = 0
    no_destino = 0

    arquivo = open('../documents/cidades.txt', 'r')
    for linha in arquivo:
        grafo.add_edge(linha.split()[0], linha.split()[1], linha.split()[2])
    arquivo.close()

    print(grafo.nodes)

    print('\n\nEscolha a rota!')
    i = 0
    while i == 0:
        no_origem = input('\nDigite a cidade de origem:')

        if grafo.procurar_no(no_origem) == 0:
            print('Cidade Inexistente')
            i = 0
        else:
            i = 1

    i = 0
    while i == 0:
        no_destino = input('\nDigite a cidade de Destino:')

        if grafo.procurar_no(no_destino) == 0:
            print('Cidade Inexistente')
            i = 0
        else:
            i = 1

    print(grafo.dijsktra(no_origem, no_destino))

