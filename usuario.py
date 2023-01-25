from conta import Conta


class Usuario(Conta):


    def __init__(self, nome, email, senha, qtd_max_telas):
        super().__init__(nome, email, senha, qtd_max_telas)

    '''str'''
    def __str__(self) -> str:
        return super().nome
    
