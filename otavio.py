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
 
class Gato: 
    
    def __init__(self, nome, cor, data_de_nascimento):
        self.nome = nome
        self.cor = cor
        self.data_de_nascimento = data_de_nascimento 

    def getinformacoes(self):
        info = f'Nome: {self.nome}, cor: {self.cor}, data_de_nascimento: {self.data_de_nascimento}' 
        return info 
    
    def sethumor(self, humor): 
        self.humor = humor

meu_gato1 = Gato('Luna, amarelo, 18 de maio 2025 ')
