
class Algoritmo:
    
    def __init__(self, nome, tempo, lista) :
        self._nome = nome
        self._tempo = tempo
        self._lista = lista
        
    def __str__(self):
        return f'Nome: {self._nome}, Tempo: {self._tempo}'    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, novoNome):
        self._nome = novoNome
        
    @property
    def tempo(self):
        return self._tempo
    
    @tempo.setter
    def tempo(self, novoTempo):
        self._tempo = novoTempo
                
    @property
    def lista(self):
        return self._lista
    
    @lista.setter
    def lista(self, novaLista):
        self._lista = novaLista 
        
  