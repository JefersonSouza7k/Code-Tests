sao_paulo = 67836.43
rio_de_janeiro = 36678.66
minas_gerais = 29229.88
espirito_santo = 27165.48
outros = 19849.53

percentualSP = 0
percentualRJ = 0
percentualMG = 0
percentualES = 0
percentualOutros = 0

soma = sao_paulo + rio_de_janeiro + minas_gerais + espirito_santo + outros
percentualSP = (sao_paulo * 100) / soma
percentualRJ = (rio_de_janeiro * 100) / soma
percentualMG = (minas_gerais * 100) / soma
percentualES = (espirito_santo * 100) / soma
percentualOutros = (outros * 100) / soma
print(f'\n O estado de São Paulo teve um percentual de {percentualSP}. \n O estado do Rio de Janeiro teve um percentual de {percentualRJ}. \n O estado de Minas Gerais teve um percentual de {percentualMG}. \n O estado do Espírito Santo teve um percentual de {percentualES}. \n E os outros estados tiveram um percentual de {percentualOutros}.')
