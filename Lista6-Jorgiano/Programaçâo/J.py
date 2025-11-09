def sublista_sem_menor(lista):
    lista= lista.copy()
    lista.remove(min(lista))
    return lista
