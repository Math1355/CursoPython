Para escrever uma mensagem em python precisamos escrever a mensagem assim: print('ola mundo!')

Para escrever numeros, devemos escrever sem as aspas simples:
print(7+4)

Se escrever da seguinte forma: print('7'+'4') <- pode usar o '+' ou ','
Ele vai escrever '74'.

Variaveis <- São objetos 
Que pode receber valores '='

nome = 'Matheus' (nome recebe matheus)
idade = 25 (idade recebe 25)
peso = 75.8 (peso recebe 75.8)
print(nome, idade, peso)

nome = input <- escreva
idade = input <- escreva
peso = input <- escreva

Desafio 1 -  Aula 01

Criar um Script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.

print(' ===== DESAFIO 01 ===== ')
nome = input('Qual e o seu nome? ')
print('Olá ' + nome + ' Prazer em te conhecer!')

Desafio 02 - Aula 01

Crie um Script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.

print(' ===== DESAFIO 02 ===== ')
dia = input('Dia = ')
mes = input('Mes = ')
ano = input('Ano = ')
print('Você nasceu no dia', dia, 'de', mes, 'de', ano, 'Correto?')

Desafio 03 - Aula 01

Crie um script Python que leia dois números e tente mostrar a soma entre eles.

n1 = input('Primeiro número ')
n1 = int(n1)
n2 = input('Segundo número ')
n2 = int(n2)
soma = n1 + n2
print('A soma é ', soma)


