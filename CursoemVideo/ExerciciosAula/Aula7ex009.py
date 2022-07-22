print('=' * 20)
salario = float(input('Qual o valor do funcionario? R$ '))
aumento = salario * 0.15
print('O aumento do funcionario será de R$ {:.2f}'.format(aumento))
novo_salario = salario + aumento
print('O novo salário do funcionario será R$ {:.2f}'.format(novo_salario))
