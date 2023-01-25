class Titulo():


    def __init__(self, titulo, diretor, genero: list, avaliacao: int) -> None:
        self.__titulo = titulo
        self.__diretor = diretor
        self.__genero = genero
        self.__avaliacao = int
    

    """Getters"""
    @property
    def titulo(self):
        return self.__titulo
    

    @property
    def diretor(self):
        return self.__diretor
    

    @property
    def genero(self):
        return self.__genero
    

    @property
    def avaliacao(self):
        return self.__avaliacao


    """Setters"""
    @titulo.setter
    def titulo(self, new_title):
        self.__titulo = new_title
    

    @diretor.setter
    def diretor(self, new_director):
        self.__diretor = new_director
    

    @genero.setter
    def genero(self, new_genre):
        """Ao passar um novo gênero ele acrescenta em sua lista de gêneros"""
        self.__genero.append(new_genre)
    

    """Método str"""
    def __str__(self) -> str:
        return self.titulo


    """Métodos da Classe"""

