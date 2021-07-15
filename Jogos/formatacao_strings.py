print("Tentativa {} de {}".format(1, 3))
print("Tentativa {1} de {0}".format(1, 3))
print("R$ {}".format(1.59))
print("R$ {:f}".format(1.59))
print("R$ {:.2f}".format(1.59))
print("R$ {:.2f}".format(1.5))
print("R$ {:.2f}".format(1234.50))
print("R$ {:7.2f}".format(1234.50))
print("R$ {:7.2f}".format(1.5))
print("R$ {:07.2f}".format(1.5))
print("R$ {:07d}".format(4))
print("Data {:02d}/{:02d}".format(9, 4))
print("Data {:02d}/{:02d}".format(19, 11))
print("Ola Sr.{1} {0}".format("Cordeiro","Leonardo"))

# Novo recurso f-string apareceu a partir do python 3.6

nome = 'Bobby'
print(f'Meu nome é {nome}')

nome = 'Bobby'
print(f'Meu nome é {nome.lower()}')

