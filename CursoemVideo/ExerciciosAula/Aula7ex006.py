print('=' * 20)
reais = float(input('Quanto dinheiro você ja tem na carteira: R$ '))
v_dolar = reais / 3.27
print('Com R$ {}, você consegue comprar US$ {:.2f}'.format(reais,v_dolar))
print('=' * 20)