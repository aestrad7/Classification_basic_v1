# Tipos de numero

## Enteros
a1=10
a2=4
r11= a1+a2
r12 =a1*a2
r13=a1/a2
r14=a1//a2
r15=a1**a2
print("Suma ", r11)
print("Multiplicacion ", r12)
print("Division ", r13) #Regresa un numero flotante
print("Division entera", r14) #Regresa un numero entero
print("exponencial\n",r15)

## Flotantes

## Complejos
## Boleanos


#####___#####

# Strings
coro=["cumbia", "reina", "region"]
texto1="Yo me llamo "+ coro[0] + "yo soy la " + coro[1] + "de la " + coro[2]
texto2="Yo me llamo %s y yo soy la %s de la %s" %(coro[0], coro[1], coro[2])
texto3="Yo me llamo {} yo soy la {} de la {}".format(coro[0], coro[1], coro[2])
print ("",texto1,"\n", texto2, "\n", texto3)

my_string = "Curso de Código Facilito!"
print(my_string[0:9:3])
print(my_string[::-1])