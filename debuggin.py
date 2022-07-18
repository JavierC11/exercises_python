# def divisors(nums):
#     divisors = []
#     for i in range(1,nums+1):
#         if nums%i != 0:
#             divisors.append(i)
#     return divisors


# def run():
#     try:
#         numero = int(input("Ingresa el numero a trabajar: "))
#         print(divisors(numero))
#     except ValueError as ve:
#         print("Solo se puede ingresar Numeros, Error '🐍"  + str(ve) )
    
#     print("termino el programa")

# if __name__ == "__main__":
#     run()

def palindromo(word):
    ##assert nos funciona para afirmar algo y si no es verdad, podemos mostrar un mensaje de error.
    assert len(word)>0 and word.isnumeric()== False, "No puede realizarse con cadenas vacias, Ni numeros."
    return word == word[::-1] 



def run():
    palabra = input("Ingresa la palabra a revisar: ")
    print("La palabra es un palindromo? "+ str(palindromo(palabra)))



if __name__ == "__main__":
    run()