# def run():
#     my_dicc = {i:i*i*i for i in range(1,101) if i%3 != 0}
#     print(my_dicc)

def run():
    ##Redondeamos el valor para tener 2 decimales
    my_dicc = {i:round(i**0.5, 2) for i in range(1,1001)}
    print(my_dicc)


if __name__ == "__main__":
    run()