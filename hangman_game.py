from random import randint
import os



def getletters():
    data = []
    letters_diccionary = {}
    ##  Get the list of the reandom words
    with open("./carpetaejemplo/data.txt", "r", encoding="utf-8") as f:
        data = [line for line in f]

    ##Getting  the random word and all the letters of that word
    word_goals = randint(0,len(data))
    word_goals = data[word_goals]
    word_goals = word_goals[:len(word_goals)-1:]
    print(word_goals)
    newword_goal = word_goals.maketrans("áéíóú", "aeiou")
    n_word = word_goals.translate(newword_goal)
    #input("hoal " + n_word)
    i= 0
    for letter in n_word:
        letters_diccionary[i]= n_word[i]
        i=i+1  
    return letters_diccionary


def empty_spaces1(nloop):
    
    with open("./carpetaejemplo/hangman_game.txt", "w", encoding="utf-8") as f:
        i = 0
        for i in range(0,20):
            spaces[i] = ""
        for i in range(0,nloop):
            spaces[i] = "_"
        for svalues in spaces.values():
            f.write(svalues)
        return spaces
    



def run():
 
    #We get the random word and the each letter of that word
    letters = getletters()
    print(letters[0])
    print(len(letters))

    #In this function we making the "__" we need for our word
    spaces3 = []
 
    for letra in letters:
        spaces3.append("_")
    # spaces3 = "".join(spaces3)
    # print("**"+str(spaces3))

    #Start the ViewMenu

    ganador = False
    try_number = 15
    
    while ganador == False:
        os.system("clear")
        print("\n\n***********************************************************")
        print("🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮🎮")
        print("🐍🐍BIENVENIDO A TU JUEGO HANGMAN DESARROYADO EN PYTHON🐍🐍")
        print("💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣💣")
        print("***********************************************************")
        print("""                                                          

        
                +-----------+
                |           |
                |           |
                            |
                            |
                            |
                            |
                            |
                            |
                            |
                =========================
--------------------------------------------------------
        
        """)
        print("El numero de intentos sobrantes es de: " + str(try_number))
        print("\n\nLa palabra tiene la siguiente cantidad de letras.")        
        print(spaces3)
        posible_try = input("\nIngresa la palabra con la que quieres intentar: ")


        for i in range(0,len(letters)):
            
            if posible_try != letters[i]:
                
                continue
            elif posible_try == letters[i]:
                spaces3[i] = posible_try
                      
        
        try_number= try_number -1


        if try_number < 1:
            os.system("clear")          
            print("\n\n\n"+str(spaces3))
            print("\n\n-------------------------------------------")
            print("😞😞 LO SENTIMOS PERDISTE EL JUEGO 😞😞")
            print("-----------------------------------------------\n\n\n\n")
            print("La palabra era " + str(letters.values()))
            exit()

        if "_" in spaces3:
            continue
        else:
            ganador = True





    os.system("clear")          
    print("\n\n\n"+str(spaces3))
    print("\n\n✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨")
    print("😎😎 FELICIDADES GANASTE EL JUEGO 😎😎")
    print("✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨✨\n\n\n\n")

if __name__ == "__main__":
    spaces = {}
    run()