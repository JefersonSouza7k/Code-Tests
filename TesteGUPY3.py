vetor_faturamento = []
contador = 0
while True:
    faturamento_dia = float(input('Informe o faturamento diário (digite 0 para encerrar): R$ '))
    if faturamento_dia == 0:
        break
    contador = contador + 1
    vetor_faturamento.append(faturamento_dia)
maior = 0
menor = 0
for i in range(len(vetor_faturamento)):
    if i == 0:
        maior = menor = vetor_faturamento[i]
    else:
        if vetor_faturamento[i] > maior:
            maior = vetor_faturamento[i]
        if vetor_faturamento[i] < menor:
            menor = vetor_faturamento[i]

media_mensal = 0
media_final = 0
dias = 0
for i in range(len(vetor_faturamento)):
    media_mensal = media_mensal + vetor_faturamento[i]
    media_final = media_mensal / contador
    if vetor_faturamento[i] > media_final:
        dias = dias + 1
print(f'\n O MAIOR faturamento do mês foi de R$ {maior} reais \n E o MENOR foi de R$ {menor} reais.')
print(f'\n O número de dias no mês que teve faturamento maior em relação a média foi de {dias} dias no mês.')