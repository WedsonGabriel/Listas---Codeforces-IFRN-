def dia(dia, mes, ano):
    meses= [None, "janeiro", "fevereiro", "marco", "abril", "maio", "junho","julho","agosto","setembro","outubro", "novembro", "dezembro"]
    dia_por_mes= [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if not (1 <= mes <= 12):
        return "Data Invalida"
    
    max_dias= dia_por_mes[mes]
    nome_mes= meses[mes]

    if not (1 <= dia <= max_dias):
        return "Data Invalida"
    
    dia_formatado= f"{dia:02d}"

    return f"{dia_formatado} de {nome_mes} de {ano}"
    




    