from multiprocessing.sharedctypes import Value


def run():
    my_list =  [1, "Hello", 1.6, True]
    my_dicc = {"Nombre": "Javier", "Apellido": "Castillo"}

    my_super_list = [
        {"first_name": "Fernando", "Last_name": "Cifuentes"},
        {"first_name": "Javier", "Last_name": "Castillo"},
        {"first_name": "Heizel", "Last_name": "Giron"},
    ]

    my_super_dicc = {
        "natural_numbers": [1,2,3,4,5],
        "real_numbers": [-1,-2,-3,0,1,2,3],
        "floating_numbers":[1.3, 1.74, 1.8, 1.8, 10.8]
    }

    for i in my_super_list:
        for  key, value in i.items():
            print(key,"-",value)

    # for key, value in my_super_dicc.items():
    #     print(key, "-" ,  value)

    # # print(my_list)
    # # print(my_dicc)
     

if __name__ == "__main__":
    run()