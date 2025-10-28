
# numero = 50 
# numero = 50 
# print(numero + numero)




# variaves 

# idade = "dez" 
# print(idade)

# - se for umar e so tirar (#)

# 3 regras 

# 1 - nao pode cinter simbolos 
# 2 - nao pode inciar com numero
# 3 - uma variavel nao pode ter espacos - use o (_)
# para separar as palavras 


# nomeDoUsuario = "pedro"


# frase = ' Ola ' + ' tudo bem?'
 
#frase1 = 'como voce estar?\n'
#frase2 = 'Eu estou bem!\n'
#frase3 = 'como vai sua familia?\n'
#frase4 = 'vai bem!'
#print(frase1 + frase2 + frase3 + frase4)

#palavra = familia 





#email = 'pedro@gmail.com'
#posicao = email.find('@')
#posicao_final = email.find ('.')
#print(email[posicao + 1:posicao_final])

# input 

#nome = input('digite seu nome\n')
#print(' ola, '+ nome +'!') 



# nome = input('qual e o seu nome? \n')
# print('nome legal, e comum.')


# len 
# frase = 'qual e o seu nome?'
# print(len(frase))

# # cont - conta quanta vezes algo  aparece na string
# # len() - retorna o comprimento de uma string

# print(frase.count ('-'))


# ----------------------------------------------------------------------------------

# resumo da aula 5 - ( Estruturas de repedição ) 


# lista_de_numeros = [ 1, 2, 3, 6,]
# print(lista_de_numeros[0])
# print(lista_de_numeros[1])
# print(lista_de_numeros[3])

# for item in lista_de_numeros:
#     print(lista_de_numeros)

# v = 0 
# while v < 10: 
#     print(v)
#     v += 1

# Break - Continue - Pass


# jogos = ['FIFA', 'minecraft', 'gta 5']


# Tuplas 

# numeros = (1, 2, 3, 4,)

# meses = ('janeiro', 'fevereiro', 'abril')

# len - Retorna o tamanho de uma string.
# count - conta quantaves vezes um detrerminado elemento que aparece na lista. 
# index - Retorna um a posição de um determinado elemento

# conjuntos(Sets)

# set() - lista de elementos únicos. 


# ---------------------------

# aula  6 


# numeros = set()


# numeros.add(3)
# numeros.add(4)
# numeros.add(5)
# numeros.add(3)

# print(numeros)


# listas [] - tuplas () - sets {}


# Booleanos - Tipo logico que so aceita dois valores: verdadeiro ou falso.

# dicionarios - (conhecido em objeto em outras linguagens)
# estrutura que armazena uma chave e um velor. 

# pessoas = {
#     'nome': 'otavio',
#     'idade': '14', 
#     'altura': '1.62'
# }

# print(pessoas['altura'])
# print(pessoas['idade'])
# print(pessoas['nome'])


# carro = { 
#     'cor': 'azul', 
#     'motor': "V-8",
#     "marca": 'bugatti',
#     "valor": '400.000'
# }

# nova_chave = input('O que você gostasria de adiciomal no carro? /n--->' )
# nova_valor = input('Qual o valor referente a chave '+ nova_chave +'? /n -->')  

# exercio 

# numeros_aleatorios = [ 1, 2, 3, 4, 4, 5, 6, 6, 7, 8] 

# numeros_certos = set()

# for numeros in 



# keys - apresenta todas as chaves do dicionarios. 
# values - apresenta todos os valores armazanados. 
# itens - apresenta ambos. 

# livro = {
#  'titulo': 'pequeno pricipe',
#  ' autor': 'tananana',
#  'ano': 1996
# }

# print(livro.keys())
# print(livro.values())
# print(livro.items())


# Exercio 2 - 



# ddd_e_estados = {
#     '61': ' Brasilia',
#     '21': 'Rio de Janeiro',
#     '11': 'São Paulo', 
#     '32': 'Juiz de Fora', 
#     '19': 'Campinas'
# }


# ------------------------------------------------------------------------------------------------------

# Aula 7 - Funções 


#  Criando funções - 
# Para declarar uma função utilizarmos a palavra reservada: def 


# def nome_da_função():
#     # codigo a se executado 
#     pass 

# # chamando a função 
# nome_da_função() 



# função de boas-vindas 


# def boas_vindas():
#     print('Seja bem vindo!')

#     boas_vindas()


# # Função com parametros 

# def boas_vindas_usuario(nome): 
#      print('Seja bem-vindo ' + nome)

# boas_vindas_usuario('Paulo')
# boas_vindas_usuario('Maria')

# Parametros são valores passado de fora para dentro de uma função. 

 # Exercios - 

# def bem_vindo_ao_new_cronos(nome)
#      print('bem vindo ao new cronos ' + nome)

# bem_vindo_ao_new_cronos('Gabriel') 

# X = input('Digite um valor ?n --->')
# Z = input('Digite o outro valor /n -->')

# def velociade(distância, tempo):

#    print( distância + tempo  ) 


# velociade( X , Z )



#  * Argument

# def prepara_açai(*itens , tamanho): 
#     print('/n preparando um açai de' ,  tamanho, 'com os seguintes ingrediente:')

#     for ingrediente in itens:
#         print('-' , ingrediente )

# prepara_açai('Amendoim', 'leite em pó', 'jujuba', 'morango', tamanho = '700ml') 
# prepara_açai('granulado', 'limão', temanho = '1l' ) 
 

# Função queretorna valores
# Para retornar um valor usamos a plavras reservadas: return 

# def diminuir(a , b):
#     return a - b 

# resultado = diminuir(5 , 2)

# print(' O resultado da subtração e ' , resultado) 


#  Função recursivas - 
# A função que chama ela mesma ate que um problema seja resolvido. 
# def dobrar_lencol(lencol , gaveta): 
#     if lencol < gaveta: 
#         return 0 
#     else: 
#         return 1 + dobrar_lencol(lencol /2 ,  gaveta )
    
# print(dobrar_lencol(200, 25)) 

# Tipo de dado -- none --> nada 

# ---------------------------------------------------------------------------------------------------

# Aula 8 - arquivos 

# Abrindo arquivos 

# open - Abre o arquivo. Recebe o caminho como parâmetro 





# # Lendo arqiuvo 
# # read() - Lê o arquivo ( Não mostra no terminal )

# print(arquivo.read()) 

# # seek(0) - Volta o ponteiro para o inicio do arquivo 
# arquivo.seek(0)


# print(arquivo.read())



# # readline ()-  Le as linhas do arquivo.

# print(arquivo.readline())
# print(arquivo.readline())
# print(arquivo.readline()) 

# Lendo arquivos com o loop for 

# for i , linha in (arquivo):
#     print(f'Linha {i} - {linha}')


# Escrevendo em um arquivo 

# write() - Função uasada para escrever em um arquivo

# arquivo.write('Testando arquivo')
# # close() - fecha o arquivo 
# arquivo.close()

# exercio 1 

# def guardar_nome(nome): 
#     with open('./pritica.txt' , 'a') as arquivo: 
#         arquivo.write(nome + '/n')
#     print(' O nome foi adicionado com sucesso') 

# nome = input(' Digite o nome do usuario /n --->')  
 

# ------------------------------------------------------------------------------------------------------------------
# Aula 9 - Modulos 

# oque sao modulos? 



 # import - comando ultilizado para importar um modulo   

# 1 importando o modulo Math 

# import math  

# # função pow - potenciação 

# print(math.pow(2 , 3))

# # Arredondando valores - 
# # Ceil - Arrendondando pra cima.
# print(math.ceil(2.7))
# # trunc - Arredondando pra baixo 
# print(math.trunc(2.3))

# # round - função nativa do pyton - Arredonda pra o inteiro mais proximo. 
# print(round(2.6))
# print(round(2.5))

# ------------------------------------------------------------------------------------------

# aula 10 - competição 


# exercios 3 - 


# ------------------------------------------------------------------------------------------------------



# ---------------------------------------------------------------------------------------------------------

# Aula 12 - Classes e objetos 

# Liguagem de auto nivel. 
# - Mais próximas da linguagem do usuario. 

# Linguagem de baixo nivel  
# Mais proximo da linguagem do computador. 


# class Cachorro:
#     raca = 'Bulldog'
#     cor = 'caramelo'
#     tamanho = 'pequeno'
#     cor = 'caramelo'

#     def latir(self): 
#         print("Au")

#     def correr(self):
#         print(' correndo...')            

# Atibutos  --> Variáves que guardam informações de uma classe.
# Métodos -->Funções dentro de uma classe.

# class Carro: 
#     rodas = '4'
#     cor = 'roxo'
#     marca = 'fiat'
#     modelo = 'uno'

#     def ligar(self):
#         print('carro ligado')

#     def desligar():
#         print('correndo')


# class Celular: 
    # capinha =  'azul' 
    # marca = 'Motorola'
    # camera = '34px'
#     tamanho = '20x10'
#     modelo = 'G24' 

#     def ligar(self):
#         print('celular ligado') 

#     def desligar(self):
#         print('Celular desligado') 

#     def som_do_alarme(self):
#         print('fruunnn')



# meu_celular = Celular()

# meu_celular.ligar()

# meu_celular.desligar()

# meu_celular.som_do_alarme()



# Metodo constutor / Metodo inicializador 


# class Pessoa: 

#     def __init__(self, nome, altura, idade):
#         self.nome = nome 
#         self.idade = idade 
#         self.altura = altura  
#         pass


#     def andar(self):
#         print('andando') 

#     def getinformacoes(self):
#         info = f'Nome: {self.nome}, idade: {self.idade}, altura {self.altura}'
#         return info
    
#     def setDataDeNascimento(self, data): 
#         self.setDataDeNascimento = data
        


# getter e setters

# Getter --> usado para pegar informações de uma classe. 

#Setters --> usado para definir uma informação de uma classe.  


# Exercicio 1 
 
# class Gato: 
    
#     def __init__(self, nome, cor, data_de_nascimento):
#         self.nome = nome
#         self.cor = cor
#         self.data_de_nascimento = data_de_nascimento 

#     def getinformacoes(self):
#         info = f'Nome: {self.nome}, cor: {self.cor}, data_de_nascimento: {self.data_de_nascimento}' 
#         return info 
    
#     def sethumor(self, humor): 
#         self.humor = humor

# meu_gato1 = Gato('Luna, amarelo, 18 de maio 2025 ') 

# ----------------------------------------------------------------------------------------------------------------------- 
# Resumo da aula 12 --> Classes 

# class Gato: 
#     def __init__(self, nome, idade, cor):
#         self.nome = nome
#         self.idade = idade 
#         self.idade = cor 
        
#     def __str__(self):
#         return f'(self.nome) - (self.idade) - (self.cor)'

#     def miar(self):
#         print('miar') 

# gato1 = ('Luna', 3 'preto')
# garo2 = ('lua' , 6 'seamês')

# ---------------------------------------------------------------------------------------------------------------------------------
# Aula 13 --> Pilates  

# 1 - Abistração - Representação de um objeto do mundo real. 
# 2 - Encapsulamento - Privar atributos de uma classe., fazendo que eles so possam ser acessados dentro da propria classe.
# class Pessoa: 
#     __saldo = 20.5


#     def __init__(self, nome, idade, ):
#         self.nome = nome
#         self.idade = idade


#     def consultar_saldo(self):
#         print(f'Você tem R$ {self.__saldo}' )

#     def set_saldo(self, valor):
#         self.__saldo += valor

# pessoa1 = Pessoa('Otavio' , 14)


# pessoa1.set_saldo(483)

# print(pessoa1.get_saldo())
# Exercicio - 

# class Conta_Bancaria():
    
#     def titular(self, nome, saldo ):
#        self.__nome = nome
#        self.__saldo = saldo

#     def set_depositar(self, saldo):
#         self.__saldo += saldo 

#     def sacar(self, valor):
#         if valor > self.salto:
#             print('Você não tem saldo desponivel.')
#         else: 
#             print('Saque realizado!!')
#             self.saldo -= valor

    
#     def 

# # ------------------------------------------------------------ 
# 3 - Herança --> E a capacidade de uma classe filho herdar os metodos e atributos da classe pai.
# Classe base --> CLasse a ser herdada 
# Classe derivada --> Classe que herda.
# class Animal_Terrestre:

#     def __init__(self, nome, especie):
#         self.nome = nome
#         self.especie = especie


#     def andam(self):
#         print('Andando...')

#     def comer(self):
#         print('Comendo...') 

# # classe derivada (subclasse) 
# class Cachorro(Animal_Terrestre):
#     def __init__(self, nome, raca):
#         super().__init__(nome, "Cachorro")
#         self.raca = raca

# chachorro1 = Cachorro('Bob' , 'Vira-Lata')

# chachorro1.andam()
# chachorro1.comer()

# print(chachorro1.especie)
# print(chachorro1.nome)
# --------------------------------------------------------------------
# 4 - Polimorfismo -->
# class Animal: 
#     def fazer_som(self):
#         print('Som generico de um animal')

# class Gato(Animal):
#      def fazer_som(self):
#         return 'miau'

# class Cachorro(Animal):
#     def fazer_som(self):
#         return "au au"

# gato1 = Gato()
# print(gato1.fazer_som())

# cachorro1 = Cachorro()
# print(cachorro1.fazer_som())

# --------------------------------------------------------------------------------------------------------------
# Aula 14 -- Testes com python unittest 

# def sobrenome_da_ordem(nome, s1, s2): 
#     if len(s1) > len(s2):
#         return f'{nome} {s1} {s2}'
#     else: 
#         return f'{nome} {s2} {s1}'
    
# print(sobrenome_da_ordem('Sojé', 'dias', 'Saraiva'))
# print(sobrenome_da_ordem('Matheus', 'Fernandes', 'Barbosa'))

# assertNotEqual(a, b)          a != b
# assertEqual(a, b)             a == b      
#assertTrue(x)                  x é verdadeiro
# assertFalse(x)                x é falso
#assertIn(tem, lista)           item está na lista
# assertNotInt(item, lista )    item não está na lista 

# ------------------------------------------------------------------------ 
# ARQUIVO DE TESTES  ----
# 
# import unittest # Deve estar ativo. 
# # from otavio import sobrenome_da_ordem

# # class NomeText(unittest.TestCase):
# #     def test_sobrenome_na_ordem(self):
# #         nome_completo = sobrenome_da_ordem('Joao', 'Madureira', 'Silva')
# #         self.assertEqual(nome_completo, 'Joao Silva Madureira')


# #     def test_sobrenome_na_ordem(self):
# #         nome_completo = sobrenome_da_ordem('José', 'Dias', 'Saraiva')
# #         self.assertEqual(nome_completo, 'José Dias Saraiva')

# def soma(a, b):
#     return a + b 

# def subtracao(a, b):
#     return a - b 

# def multiplicacao(a , b ):
#     return a * b 

# def divisao(a , b ): 
#     return a / b 



# class ContaTest(unittest.TestCase):
#     def test_soma(self):
#         res = soma(5 , 2 )
#         self.assertEqual(res, 7)

#     def test_subtracao(self):
#         res = subtracao(56 , 24) 
#         self.assertEqual(res, 32)

#     def test_multiplicacao(self):
#         res = multiplicacao(3 , 9)
#         self.assertEqual(res,  27 )


#     def test_divisao(self):
#         res = divisao( 9 , 3 )
#         self.assertEqual(res, 3)




# unittest.main(argv=[' '], exit = False) # deve estar ativo tambem.
