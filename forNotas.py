notas_acumulo = 0

for i in range(1, 5, 1):
    nota = float(input(f"Informe a {i}ª nota: \n"))

    notas_acumulo += nota

    media = notas_acumulo / 4

    print(f"Sua nota é: {media}")
