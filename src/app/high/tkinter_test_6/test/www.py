while True:
    year = input("Que año quieres revisar?: \n")
    try:
        year = int(year)
        print("numero verificado: "+year)
        break
    except ValueError:
        print("Esto no es un numero")

print(str(year))