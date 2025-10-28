import unittest
# from otavio import sobrenome_da_ordem

# class NomeText(unittest.TestCase):
#     def test_sobrenome_na_ordem(self):
#         nome_completo = sobrenome_da_ordem('Joao', 'Madureira', 'Silva')
#         self.assertEqual(nome_completo, 'Joao Silva Madureira')


#     def test_sobrenome_na_ordem(self):
#         nome_completo = sobrenome_da_ordem('José', 'Dias', 'Saraiva')
#         self.assertEqual(nome_completo, 'José Dias Saraiva')


# assertNotEqual(a, b)          a != b
# assertEqual(a, b)             a == b      
#assertTrue(x)                  x é verdadeiro
# assertFalse(x)                x é falso
#assertIn(tem, lista)           item está na lista
# assertNotInt(item, lista )    item não está na lista 
def soma(a, b):
    return a + b 

def subtracao(a, b):
    return a - b 

def multiplicacao(a , b ):
    return a * b 

def divisao(a , b ): 
    return a / b 



class ContaTest(unittest.TestCase):
    def test_soma(self):
        res = soma(5 , 2 )
        self.assertEqual(res, 7)

    def test_subtracao(self):
        res = subtracao(56 , 24) 
        self.assertEqual(res, 32)

    def test_multiplicacao(self):
        res = multiplicacao(3 , 9)
        self.assertEqual(res,  27 )


    def test_divisao(self):
        res = divisao( 9 , 3 )
        self.assertEqual(res, 3)




unittest.main(argv=[' '], exit = False)
