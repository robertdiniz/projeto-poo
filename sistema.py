class Sistema():


    class Categoria():

        def __init__(self) -> None:
            """
                Na categoria, teremos filmes e séries.
                {
                    'filmes': [],
                    'series': []
                }
            """
            self.__categoria = {}
        
        """Getters"""
        @property
        def categoria(self):
            return self.__categoria
        
        """Setters"""
        @categoria.setter
        def categoria(self, new_title):
            """ Ao passar um novo título, acrescenta no dicionário da categoria """
            self.__categoria.append(new_title)

    def __init__(self) -> None:
        self.__contas_criadas = []
        """
            Na categoria, teremos filmes e séries.
            {
                'filmes': [],
                'series': []
            }
        """
        self.__categoria = {}

    """Getters"""
    @property
    def contas_criadas(self):
        return self.__contas_criadas
    
    """Setters"""
    @contas_criadas.setter
    def contas_criadas(self, new_account):
        self.__contas_criadas.append(new_account)
    
    """Métodos da Classe"""

    def login(self, conta, senha):
        pass

    
    def assistir(self, conta, titulo):
        pass

    
    def buscar(self, titulo):
        pass


    def logout(self, conta):
        pass


