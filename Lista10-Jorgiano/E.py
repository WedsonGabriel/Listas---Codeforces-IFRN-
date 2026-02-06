while True:
    try:
        def saltadores(sequencia):
            verificacao = []
            if len(sequencia) == 2:
                return "Alegre"
 
            for i in range(2, len(sequencia)):
                calc = abs(sequencia[i] - sequencia[i-1])
                if calc > sequencia[0]-1 or calc < 1:
                    return "Nao alegre"
                else:
                    if calc not in verificacao:
                        verificacao.append(calc)
                    else:
                        return "Nao alegre"
            return "Alegre"
        
        
        sequencia = list(map(int,input().split()))
        print(saltadores(sequencia))
 
    except EOFError:
        break
