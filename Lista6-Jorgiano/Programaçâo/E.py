def dia_da_semana(h,d):
    dias = ["Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
    dia_hoje = dias.index(h)
    dias_semana = (dia_hoje + d) % 7
    indice = dias[dias_semana]
    return indice

h = input()
d = int(input())
print(dia_da_semana(h,d))




