#!/usr/bin/python3
import numpy as np

class Calculadora:
    def __init__(self):
        self.n1 = None
        self.n2 = None
        self.escolha = None
        self.tamanholista = None
        self.lista = []
    
    def soma(self):
        return round(self.n1+self.n2, 2)

    def subtracao(self):
        return round(self.n1-self.n2, 2)

    def multiplicacao(self):
        return round(self.n1*self.n2, 2)

    def divisao(self):
        return round(self.n1/self.n2, 2)
    
    def appendLista(self):
        self.lista = None
        self.lista = list()
        for i in range(0, self.tamanholista):
            numero = float(input('Digite número por número para calcular a média: '))
            self.lista.append(numero)
        self.calculamedia()
    
    def calculamedia(self):
        return print(round(np.mean(self.lista), 2))
        
    
    def confere(self):
        if(self.escolha == 7):
            return False

        elif(self.escolha <= 0 or self.escolha >6):
            print("Voce escolheu uma opcao errada para operacao")
            return False 
        
        else: return True
    
    def porcentagem(self):
        return round(self.n1*(self.n2/100), 2)

    def apos_confere(self):
        if (self.escolha == 1):
            return print(f'A soma entre {self.n1} e {self.n2} é igual a', self.soma())
        
        elif self.escolha == 2:
            return print(f'A subtracao entre {self.n1} e {self.n2} é igual a', self.subtracao())
        
        elif self.escolha == 3:
            return print(f'A multiplicacao entre {self.n1} e {self.n2} é igual a', self.multiplicacao())
        
        elif self.escolha == 4:
            return print(f'A divisao entre {self.n1} e {self.n2} é igual a', self.divisao())

        elif self.escolha == 6:
            return print(f'A porcentagem de {self.n1} por {self.n2} é igual a', self.porcentagem())


calculadora = Calculadora()

while True:
    
    calculadora.escolha = int(input('Qual operacao deseja fazer? 1 = soma 2 = subtracao 3 = multiplicacao 4 = divisao 5 = media 6 = porcentagem 7 = sair: '))
    
    if not calculadora.confere():   
        break
    
    if calculadora.escolha == 5:
        calculadora.tamanholista = int(input('Digite a quantidade de números para calcular a média: '))
        calculadora.appendLista()
    
    elif calculadora.escolha == 6:
            calculadora.n1 = float(input('Digite o número para calcular a porcentagem: '))
    
            calculadora.n2 = float(input('Digite a porcentagem que queira calcular: '))
    
            calculadora.apos_confere()
    else:
            calculadora.n1 = float(input('Digite um número: '))
            calculadora.n1 = round(calculadora.n1, 2)
    
            calculadora.n2 = float(input('Digite um número: '))
            calculadora.n2 = round(calculadora.n2, 2)
    
            calculadora.apos_confere()

