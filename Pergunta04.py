faturamento_SP = 67836.43
faturamento_RJ = 36678.66
faturamento_MG = 29229.88
faturamento_ES = 27165.48
faturamento_Outros = 19849.53

faturamento_total = faturamento_SP + faturamento_RJ + faturamento_MG + faturamento_ES + faturamento_Outros

percentual_SP = (faturamento_SP / faturamento_total) * 100
percentual_RJ = (faturamento_RJ / faturamento_total) * 100
percentual_MG = (faturamento_MG / faturamento_total) * 100
percentual_ES = (faturamento_ES / faturamento_total) * 100
percentual_Outros = (faturamento_Outros / faturamento_total) * 100

print(f"SP: {percentual_SP:.2f}%")
print(f"RJ: {percentual_RJ:.2f}%")
print(f"MG: {percentual_MG:.2f}%")
print(f"ES: {percentual_ES:.2f}%")
print(f"Outros: {percentual_Outros:.2f}%")