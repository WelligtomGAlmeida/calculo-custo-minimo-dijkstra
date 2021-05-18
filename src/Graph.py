from collections import defaultdict


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def procurar_no(self, noprocurado):
        no = 0

        for node in self.nodes:
            if node.replace(' ', '').upper() == noprocurado.replace(' ', '').upper():
                no = node

        if no == 0:
            return 0

        return 1

    def add_node(self, value):
        self.nodes.add(str(value).replace(' ', '').upper())

    def add_edge(self, from_node, to_node, distance):
        from_node = str(from_node).replace(' ', '').upper()
        to_node = str(to_node).replace(' ', '').upper()

        if self.procurar_no(from_node) == 0:
            self.add_node(from_node)
        if self.procurar_no(to_node) == 0:
            self.add_node(to_node)

        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance

    def dijsktra(self, initial, final):
        initial = str(initial).replace(' ', '').upper()
        final = str(final).replace(' ', '').upper()
        visited = {initial: 0}
        path = {}
        caminho = ''
        caminhol = list()

        nodes = set(self.nodes)

        while nodes:
            min_node = None
            for node in nodes:
                if node in visited:
                    if min_node is None:
                        min_node = node
                    elif visited[node] < visited[min_node]:
                        min_node = node

            if min_node is None:
                break

            nodes.remove(min_node)
            current_weight = visited[min_node]

            for edge in self.edges[min_node]:
                weight = float(current_weight) + float(self.distances[(edge, min_node)])
                #print(str(min_node) + ' : ' + str(edge) + ' = ' + str(self.distances[(edge, min_node)]))

                if edge not in visited or weight < visited[edge]:
                    visited[edge] = weight
                    path[edge] = min_node

        print(path)

        i = 0
        atual = ''
        while i == 0:
            if atual != initial:
                if not caminhol:
                    caminhol.append(final)
                    caminhol.append(path[str(final).replace(' ', '')])
                    atual = path[final.replace(' ', '')]
                else:
                    caminhol.append(path[atual].replace(' ', ''))
                    atual = path[atual.replace(' ', '')]
            else:
                i = 1

        for x in reversed(caminhol):
            if caminho == '':
                caminho = '\nPercurso: ' + x
            else:
                caminho = caminho + ' -> ' + x
        caminho = caminho + '\nDistância Percorrida: ' + str(visited[str(final).replace(' ', '')])

        return caminho