# def esPalindromo(palabra):
#     palabra = palabra.replace(" ","")
#     palabra = str(palabra).strip().lower()  
#     if palabra == palabra[::-1]:
#         print("Es Palindomo")
#     else:
#         print("No es Palindromo")   



# P = input("Ingresa el posible palindromo:")

# esPalindromo(P)

# def run():  
#     elevado = 0
#     limite = 1000000    
#     resultado = 2**elevado
#     while resultado <    limite  :
#         print("La potencia de dos es igual a " + str(resultado))
#         elevado = elevado +1    
#         resultado = 2**elevado


# if __name__ == "__main__":
#     run()


# def run():
#     LIMITE = 1000000
#     contador = 0
#     potencia_2 = 2**contador
#     while potencia_2 < LIMITE:
#         print('2 elevado a ' + str(contador) +
#               ' es igual a: ' + str(potencia_2))
#         contador = contador + 1
#         potencia_2 = 2**contador

# if __name__ == "__main__":
#     run()




# def run():
#     LIMITE = 1+ int(input("Ingresa hasta que numero quieres revisar si existen numeros"
#      " primos "))
#     for numero in range(1,LIMITE):
#         saltar = True
#         for itemdivisor in range(numero):
#             if itemdivisor == 1 or itemdivisor == numero or itemdivisor==0:
#                 continue
#             if int(numero % itemdivisor) == 0:
#                 saltar = False
#             elif int(numero%itemdivisor)!= 0:
#                 continue
#         if saltar == False:        
#             print(str(numero))           
#         else:
#             print("*"+str(numero))



# if __name__ == "__main__":
#     run()


