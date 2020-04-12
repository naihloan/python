meses = ["Enero", "Febrero", "Marzo"];

# print(meses[0])
lenguajes = ['Python', 'Kotlin', 'Java', 'JavaScript']

# print(lenguajes)
# print(lenguajes[0])

# Ordenar los elementos (alfabéticamente)
lenguajes.sort()
print(lenguajes)
print(lenguajes[3])

# Acceder a un elemento dentro de un texto
aprendiendo = f'Estoy aprendiendo {lenguajes[3]}'
print(aprendiendo)

# Modificando valores de un arreglo/list
lenguajes[0] = 'C#'
print(lenguajes)

# Agregar elementos a un arreglo/list
lenguajes.append('Ruby')
print(lenguajes)

# Eliminar de un arreglo (list)
del lenguajes[1]
print(lenguajes)

# Eliminar último ítem de un arreglo (list)
lenguajes.pop()
print(lenguajes)

# Eliminar cualquier ítem de un arreglo (list)
lenguajes.pop(1)
print(lenguajes)

# Eliminar por nombre
lenguajes.remove('C#')
print(lenguajes)
