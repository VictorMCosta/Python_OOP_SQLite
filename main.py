#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa

#Exemplo de uso
victor = Pessoa(1, "Victor Mendes")
print(victor)

#Quero mostrar só o nome
print(victor.nome)
