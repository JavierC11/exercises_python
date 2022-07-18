from functools import reduce

def run():
    my_list = [0,1,2,3,4,5,6,7,8,9]
    # variable_filter = list(filter(lambda x: x, my_list))
    # print(variable_filter)
    # variable_map = list(map(lambda x: x/2, my_list))
    # print(variable_map)

    variable_reduce = reduce(lambda a,b: a+b, my_list)
    print(variable_reduce)


if __name__ == "__main__":
    run()