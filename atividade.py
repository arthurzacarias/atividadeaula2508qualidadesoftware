ano = int(input("Insira o ano que você deseja: "))

if ano < 2000 or ano > 4000:
    print("O ano tem que ser entre 2000 e 4000")
    exit()

vezes = 0

for i in range(2000, ano + 1):
    if i % 4 == 0:
        vezes += 1

print("No ano de {0}, foram contabilizados {1} anos bissextos.".format(ano, vezes))




