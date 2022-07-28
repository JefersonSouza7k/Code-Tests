numero = int(input('Digite um número: '))
primeiro = 0
segundo = 1
print(f'{primeiro} -> {segundo}', end = '')
contador = 3
while contador <= numero:
   terceiro = primeiro + segundo
   print(f'-> {terceiro}', end = '')
   primeiro = segundo
   segundo = terceiro
   contador = contador + 1
print('-> FIM')