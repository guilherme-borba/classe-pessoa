# Classe Pessoa: Crie uma classe que modele uma pessoa:
# Atributos: nome, idade, peso e altura
# Métodos: Envelhercer, engordar, emagrecer, crescer.
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

import pessoa
fulano = pessoa.Pessoa("fulano", 15, 62, 162.2)
pessoa.Pessoa.crescer(fulano)
pessoa.Pessoa.envelhecer(fulano)
pessoa.Pessoa.crescer(fulano)
