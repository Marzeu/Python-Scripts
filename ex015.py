d = int(input('Quantos dias o carro foi alugado? '))
k = float(input('Quantos quilometros o carro percorreu? '))
dia = 60 * d
dist = 0.15 * k
print('O valor total é R$ {:.2f} sendo que as {} diárias custaram R$ {} e os quilômetros rodados {} custaram R$ {}'.format(
    dia+dist, d, dia, k, dist))
