tempo_meia_vida , massa = map(int,input().split())
contador = 0

while massa >= 0.5:
    massa = massa / 2
    contador += 1

tempo_gasto = tempo_meia_vida * contador

dias = tempo_gasto // 86400
resto_apos_dias = tempo_gasto % 86400

horas = resto_apos_dias // 3600
resto_horas = resto_apos_dias % 3600

minutos = resto_horas // 60
segundos = resto_horas % 60

print(f"{dias} dias {horas:02d}:{minutos:02d}:{segundos:02d}")




