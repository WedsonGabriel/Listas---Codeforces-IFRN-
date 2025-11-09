def lista_troca_menor_primeiro(lista):
     if len(lista) < 2:
        return 0
     
     indice_menor= lista.index(min(lista))
     if indice_menor == 0:
         return 0

     lista[0], lista[indice_menor] = lista[indice_menor], lista[0]
     return 1

    

