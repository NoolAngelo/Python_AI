colombian = float(input("What do you have left in pesos? "))
cur_colombian = colombian/0.00026
print(cur_colombian)

Peruvian = float(input("What do you have left in soles? "))
cur_soles = Peruvian/0.27

brazil = float(input("What do you have left in Brazilian currency? "))
cur_reais = brazil/0.20

cur_colombian = colombian/0.00026

result = cur_colombian + cur_soles + cur_reais
print(result)
