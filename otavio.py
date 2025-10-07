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


# -------------------------------------------------------------------------------------------------------