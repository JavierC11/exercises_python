def run():
    variable_lambda = lambda string: string == string[::-1]
    print(variable_lambda("jaja"))

if __name__ == "__main__":
    run()