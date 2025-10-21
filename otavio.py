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

# --------------------------------------------------------
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
class Animal_Terrestre:

    def __init__(self, nome, especie):
        self.nome = nome
        self.especie = especie


    def andam(self):
        print('Andando...')

    def comer(self):
        print('Comendo...') 

# classe derivada (subclasse) 
class Cachorro(Animal_Terrestre):
    def __init__(self, nome, raca):
        super().__init__(nome, "Cachorro")
        self.raca = raca

chachorro1 = Cachorro('Bob' , 'Vira-Lata')

chachorro1.andam()
chachorro1.comer()

print(chachorro1.especie)
print(chachorro1.nome)