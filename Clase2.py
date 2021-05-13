course ='Curso'
my_string='Código Facilito!'

result = '{} de {}'.format(course, my_string)

print(result)

#####___#####

# Formato
course ='Curso'
my_string='Código Dacilito!'

result2 = '{a} de {b}'.format(b=course, a=my_string)

print(result2)

#####___#####

# Otros metdos de formato
## lower
print(result.lower())
print(result.upper())
print(result.title())

#####___#####

# Metodos de busqueda
## .find()
print(result.find("Código"))

## .count()
result=result.lower()
print(result.count("c"))

## .replace()
print(result.replace('c', 'x'))

## .split()
new_string =result.title().split(' ')
print(new_string)

#####___#####
#####___#####

# Listas
my_list=["string", 15,15.6,True]
print(my_list)

## .append()
my_list.append(6)
print (my_list)

## .insert()
my_list.insert(1, "insert") #el primero es un numero entero para indicar la posicion en que entrará el nuevo elemento, el segundo es el nuevo elemento.
print(my_list)

## .remove()
my_list.remove(15)
print(my_list)

## pop _ toma el ultimo valor de la lista y lo borra de la lista
print(my_list)
last_value=my_list.pop()
print(my_list)
print(last_value)

#####___#####

## .sort()
my_list=[1,9,12,22,8,4,65,78,15,100]
my_list.sort(reverse=True) #reverse opcional para decendente, por defecto viene en acendente
print(my_list)

my_list2=[22,23]

## .extend()
my_list.extend(my_list2)
print(my_list)

my_list.append(my_list2) # no agrega los numeros de la lista, agrega una lista como valor de la otra lista [[]]
print(my_list)

#####___#####
#####___#####

# Tuplas
### no se pueden mutar elementos, datos constantes.
my_tuple = (1, "string", True)
print(my_tuple)
print(my_tuple[0:2])

#####___#####
#####___#####

# Diccionarios
diccionario = { 'a' : 55, 'e' : True,  5 : 'Un string', (1,2) : False }  #llave : valor
print(diccionario)

### el diccionario toma el valor de la ultima llave

## agregar valores al diccionario
diccionario['c']="nuevo string"
diccionario['e'] = False
print(diccionario)

## Valor del diciconario
valor = diccionario['e']
print(valor)

## get
valor=diccionario.get('z',"valor no encontrado")
print(valor)
valor2=diccionario.get(5)
print(valor2)

## eliminar del diccionario
del diccionario[5] # del elimina del diccionario llave y valor
print(diccionario)

# .keys -> objeto iterable
llaves = list (diccionario.keys()) #list devuelve una lista
valores = diccionario.values()
### se puede agregar "tuple()" para que devuelva una tupla y no una lista
print(llaves)
print(valores)

## extender diccionario de bloque
diccionario_dos = { 'z': 23 , 'w' : 88}
diccionario.update(diccionario_dos)
print(diccionario)














