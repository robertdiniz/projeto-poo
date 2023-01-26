class Conta:
    def __init__(self, nome, email, senha, qtd_max_telas):
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        self.__qtd_max_telas = qtd_max_telas
        self.__telas = []
        self.__telas_logadas = 0
        self.__logado = False
        self.__favoritos = []
        self.__plano = ''

    """GET and SET"""
    @property
    def nome(self):
        return  self.__nome

    @nome.setter
    def nome(self, value):
        self.__nome = value

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value

    @property
    def senha(self):
        return self.__senha

    @senha.setter
    def senha(self, value):
        self.__senha = value

    @property
    def qtd_max_telas(self):
        return self.__qtd_max_telas

    @qtd_max_telas.setter
    def qtd_max_telas(self, value):
        self.__qtd_max_telas = value

    @property
    def plano(self):
        return self.__plano

    @plano.setter
    def plano(self, value):
        self.__plano = value

    @property
    def telas(self):
        return self.__telas

    @telas.setter
    def telas(self, value):
        self.__telas.append(value)

    @property
    def telas_logadas(self):
        return self.__telas_logadas

    @telas_logadas.setter
    def telas_logadas(self, value):
        self.__telas_logadas = value
    
    @property
    def logado(self):
        return self.__logado

    @logado.setter
    def logado(self, value):
        self.__logado = value
    
    @property
    def favoritos(self):
        return self.__favoritos

    @favoritos.setter
    def favoritos(self, value):
        self.__favoritos.append(value)
    
    
    """ METHODS THIS CLASS"""
    def escolher_plano(self, new_plan):
        self.plano = new_plan
    
    def alterar_plano(self, new_plan):
        self.plano = new_plan

    def criar_tela(self, nome_da_tela):
        """verifica se a quantidade de telas ja logadas nao é maior q o suportado"""
        if self.telas_logadas <= len(self.telas) and self.telas_logadas < self.qtd_max_telas:
            self.telas.append(nome_da_tela)
            self.telas_logadas += 1
        
        elif self.telas_logadas == self.qtd_max_telas:
            """se a quantidade de telas logadas for igual ao limite nao vai mais adicionar"""
            return '\033[0;30;41mERROR!! muitas telas logadas;(\033[m'
        
        else:
            """e se nada acima for atendido retorna um erro"""
            raise ValueError('\033[0;30;41mERROR!! ;(\033[m')

    def apagar_tela(self, id_tela):
        """levando em consideração q o usuario nao entende de incide, vou criar uma validação para o valor q ele colocar"""
        id_tela -= 1
        del self.telas[id_tela]

    
    def modificar_tela(self, id_tela):
        pass

    def favoritar_titulo(self, titulo):
        self.favoritos.append(titulo)