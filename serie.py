from titulo import Titulo


class Serie(Titulo):

    def __init__(self, titulo, diretor, genero: list, avaliacao: int) -> None:
        super().__init__(titulo, diretor, genero, avaliacao)
        """
            Temporadas é um dicionário:
            {
                'temporada1': [episodio(obj), episodio(obj)]
                'temporada2': {
                    'ep1': {
                        'titulo': 'episodio um',
                        'duracao': duracao
                    },
                    'ep2': {
                        'titulo': 'episodio um',
                        'duracao': duracao
                    },
                }
            }
        """
        self.__temporadas = {}

