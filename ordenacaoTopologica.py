from Grafo import Grafo
from lerEntrada import grafoDeEntrada

class OrdenacaoTopologica():
    def __init__(self):
        self.tempo = 0

    def ordenacaoTopologica(self,gfo: Grafo):
        visitados_c = {vert[0]: False for vert in gfo.vertices}
        tempo_t = {vert[0]: float('inf') for vert in gfo.vertices}
        tempo_f = {vert[0]: float('inf') for vert in gfo.vertices}



        ordenado = []
        for vert in gfo.vertices:
            if not visitados_c[vert[0]]:
                self.dfs_visit_ot(gfo, vert, visitados_c, tempo_t, tempo_f, ordenado)

        string_formatada = ''
        for item in ordenado:
            string_formatada += str(item)+' -> '
        string_formatada = string_formatada.strip(' -> ')
        print(string_formatada)
        return ordenado


    def dfs_visit_ot(self,gfo, vert, visitados_c, tempo_t, tempo_f, ordenado):
        visitados_c[vert[0]] = True
        self.tempo += 1
        tempo_t[vert[0]] = self.tempo
        for indice in gfo.vizinhos(vert[0]):
            vert1 = gfo.vertices[indice-1]
            if not visitados_c[vert1[0]]:
                self.dfs_visit_ot(gfo, vert1, visitados_c, tempo_t, tempo_f, ordenado)

        self.tempo += 1
        tempo_f[vert] = self.tempo
        ordenado.insert(0, vert[1])


if __name__ == "__main__":
    g1 = grafoDeEntrada("casos-de-teste/dirigido2.txt", isDirigido=True)
    ord = OrdenacaoTopologica()
    ord.ordenacaoTopologica(g1)
