from tokenize import String


nombre = input("Cual es tu nombre de usuario: ")

print("""\n\n\n\nHola """+ nombre +"""\n
***********************************
***********************************
***********************************
        Bienvenido al sistema 
        de devoluciones de tu 
        Banco Favorito       
***********************************
***********************************
***********************************
***********************************

Sabemos que tuviste algunos problemas pagando tu
tarjeta de credito, sabemos que el cambio de moneda te hizo 
una mala jugada, por favor indicanos si quieres cambiar de
quetazales a dls tu monto  o de dls a quetzales.

 """)

desicion =  int(input("""1. Cambiar de dls a Q
 2. Cambiar de Q a dls. """))

 