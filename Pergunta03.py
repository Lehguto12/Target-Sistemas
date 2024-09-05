import json

with open('faturamento.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = dados['faturamento_diario']

faturamento_valores = [dia['valor'] for dia in faturamento_diario if dia['valor'] > 0]

menor_faturamento = min(faturamento_valores)
maior_faturamento = max(faturamento_valores)

media_mensal = sum(faturamento_valores) / len(faturamento_valores)
dias_acima_da_media = len([valor for valor in faturamento_valores if valor > media_mensal])

print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")