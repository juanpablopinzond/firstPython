#Tipo entero o INTEGER
x = 10
print(x)
print(type(x))
#Tipo float 
x = 14.50
print(x)
print(type(x))
#Tipo String
x = "Hola mundo"
print(x)
print(type(x))
#Tipo Boolean
x = True
print(x)
print(type(x))
#String Cadena
myFavoriteDj = "Alan Walker"
print(myFavoriteDj)
print("Mi Dj Favorito es: " + myFavoriteDj)
pizza = "Pizza "
marcaFavoritaPizza1 = "Dominos"
marcaFavoritaPizza = "Hut"
print("Mi pizza favorita es " + pizza + marcaFavoritaPizza + " y " + pizza + marcaFavoritaPizza1)
print("Mi Dj Favorito es:", myFavoriteDj)
numero1 = 1
numero2 = 2
resultado = numero1 + numero2
print(resultado)
numero3 = "10"
numero4 = "20"
print("contatenacion:", numero4 + numero3)
resultado2 = int(numero3) + int(numero4)
print(resultado2)
true = True
print(true)
false = False
print(false)
answer = true == true    
print(answer)
a = 20
b = 10
c = a > b
print(c)
if c:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

#Input para procesar los datos del usuario
# info = input("Escribe un mensaje: ", )
# print("Valor proporcionado: ", info)
# print("Fin del programa")

# data = int(input("Escribe tu CI sin el ultimo numero: "))
# lastNumber = input("- ")
# print("Tu numero de CI es:", data , lastNumber)
# print("Fin del programa")


day = int(input("Como estuvo tu dia (1 a 10:): "))
if day >= 1 | day <= 10:
    print("Mi dia estuvo de:", day)
else:
    print("Ingresa un valor correcto")
print("Fin del Programa")



