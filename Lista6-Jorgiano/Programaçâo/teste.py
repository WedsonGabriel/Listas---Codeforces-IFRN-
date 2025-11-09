def lista_troca_menor_primeiro(lista):
      if len(lista) < 2:
         return lista
      
      indice_menor = lista.index(min(lista))
      
      lista[0], lista[indice_menor] = lista[indice_menor], lista[0]
      
      return lista


numeros_teste = [50, 12, 99, 4, 25]

resultado = lista_troca_menor_primeiro(numeros_teste)

print(f"Lista original: [50, 12, 99, 4, 25]")
print(f"Lista modificada: {resultado}")