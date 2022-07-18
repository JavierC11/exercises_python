from os import lseek

# def run():
#     lista=[]
#     for i in range(1,101):
#         numero = i*i
#         if i%3  != 0:
#             lista.append([numero])
        
#     print(lista)    

# listcomplehensions = [ i*i for i in range(1,101) if i%3 != 0]
# print(listcomplehensions)

def run():
    listcomplehensionsn = [ i for i in range(1,10001) if i%4 == 0 and i%6 == 0 and i%9 == 0 ]
    print(listcomplehensionsn)


if __name__ == "__main__":
    run()