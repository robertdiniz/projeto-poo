from sistema import Sistema
from usuario import Usuario


sistema = Sistema()
usuario = Usuario('teste', 'teste@gmail.com', 1234, 4)
sistema.adicionar_usuario(usuario)
print(sistema.contas_criadas)
print(sistema.contas_criadas[0].email)
sistema.login('teste@gmail.com', 1234)
print(usuario.logado)
sistema.logout(usuario)
print(usuario.logado)