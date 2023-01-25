from titulo import Titulo


class Filme(Titulo):


    def __init__(self, titulo, diretor, duracao, genero: list, avaliacao: int) -> None:
        super().__init__(titulo, diretor, genero, avaliacao)
        self.__duracao = duracao
    
    """Getters"""
    @property
    def duracao(self):
        return self.__duracao
    
    """Setters"""
    @duracao.setter
    def duracao(self, nova_duracao):
        self.__duracao = nova_duracao
    
