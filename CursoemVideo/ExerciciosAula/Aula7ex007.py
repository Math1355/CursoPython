print('=' * 20)
largura = float(input('Qual e a largura da parede: '))
altura = float(input('Qual e a altura da parede: '))
raio = largura * altura
print('A parede tem a dimensão de {}x{} é sua área é de {:.3f}m²'.format(largura, altura, raio))
tinta = raio / 2
print('Vai ser necessario {}l de tinta para pintar a parede.'.format(tinta))
print('=' * 20)
