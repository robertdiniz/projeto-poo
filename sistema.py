class Sistema():


    def __init__(self) -> None:
        """
            Contas criadas vai ser uma lista com objetos Conta:
            contas_criadas = [Conta, Conta, ...]
        """
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

    @property
    def categoria(self):
        return self.__categoria

    """Setters"""
    @contas_criadas.setter
    def contas_criadas(self, new_account):
        self.__contas_criadas.append(new_account)

    @categoria.setter
    def categoria(self, new_title):
        """ Ao passar um novo título, acrescenta no dicionário da categoria """
        self.__categoria.append(new_title)
    

    """Métodos da Classe"""

    def adicionar_usuario(self, new_user):
        self.__contas_criadas.append(new_user)


    def login(self, email: str, senha):

        for conta in range(len(self.contas_criadas)):
            """ 
            Percorrendo contas no 'banco de dados' 
            obs: login apenas com e-mail e senha 
            """

            if self.contas_criadas[conta].email == email:
                """
                Se o EMAIL da conta no elemento atual da LISTA for igual ao informado -> próxima etapa
                """

                if senha == self.contas_criadas[conta].senha:
                    """ 
                    Se a SENHA da conta no elemento atual da LISTA for igual ao informado -> mude seu status para logado 
                    """
                    self.contas_criadas[conta].logado = True
            else:
                return f'Nenhuma conta encontrada com esses dados.'



    def assistir(self, conta, titulo):
        if self.conta.logado != True:
            return f'Tente fazer o login novamente!'
        elif self.conta.telas_logadas >= self.conta.qtd_max_telas:
            return f'Máximo de telas permitidas atingida!'
        

    
    def buscar(self, titulo):
        pass


    def logout(self, usuario):
        """ Usuário atual recebe status falso e é dado um logout """
        usuario.logado = False




