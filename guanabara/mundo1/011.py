largura = float(input('Insira a largura da parede: '))
altura = float(input('Insira a altura da parede: '))
área = largura * altura
tinta = área / 2



print('A parede tem dimensão de {:.1f}x{:.1f} e sua área é de {:.1f}m².'.format(largura, altura, área))
print('Apartir disso, é possível concluir que é preciso de {:.1f}L de tinta para pintar a parede.'.format(tinta))
