def reading():
    aleatory_numbers =[]
    with open("./carpetaejemplo/ejemplo_write.txt", "r", encoding="utf-8") as f:
        for line in f:
            aleatory_numbers.append(line)
        print(aleatory_numbers)    

def written():
    nombres = ["Victor", "Alejandro", "Aneliz", "Gárcia"]
    with open("./carpetaejemplo/ejemplo_write.txt", "a", encoding="utf-8") as f:
        for name in nombres:
            f.write(name)
            f.write("\n")


def run():
    written()    
    reading()
        
    



if __name__ == "__main__":
    run()