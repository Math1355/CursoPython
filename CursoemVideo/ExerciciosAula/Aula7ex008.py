print('=' * 20)
preco = float(input('Insira o preço do produto: R$ '))
desconto = preco * 0.05
novo_preco = preco - desconto
print('O preço do produto com desconto fica: R$ {:.2f}'.format(novo_preco))
print('=' * 20)
