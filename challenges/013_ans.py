
#Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].
#
#Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.
#
#For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.


board = [
    [" ", "X", " "],
    [" ", "O", "O"],
    ["X", " ", " "],
]

for index,i in enumerate(board):
    for g in board[index]:
        print(f"{g}  ",end="")
        #if index == len(board[index]) - 1:
        #    print(g)
        #else:
        #    print(f"{g}\t",end="")

    if index != len(board) -1 :
        print("\n--------")
print()

def get_row_col(par):
    columns = {
        "A": 0,
        "B": 1,
        "C": 2
    }
    
    if len(par) > 2 or len(par) < 2:
        print("Ingrese una letra y un numero, por ejemplo A1")
        return False
    else:
        div = [x for x in par]
        try:
            letra = div[0].upper()
            if letra.upper() not in columns.keys():
                print("o es una de las opciones validas. las opciones validas son A, B o C")


            numero = 0
            if int(div[1]):
                numero = int(div[1])
                if numero > 0 and numero < 4:
                    return (numero-1, columns[letra])
                else:
                    print("iene un valor muy alto o muy bajo, los valores tienen que ser 1, 2 o 3")
            else:
                print("NO es un numero aceptable")

        except ValueError:
            print("Formato incorrecto. El formato es A1")
        

    return False







#    if index % 2 == 0:
#        for g in range(len(i)):
#            if g == len(i)-1:
#                print("---")
#                print(g)
#            else:
#                print(g)
#                print("---",end="")
    #for f in i:
    #    print(f)

def get_row_col(par: str):
    columns = {
        "A": 0,
        "B": 1,
        "C": 2
    }
    

    if len(par) > 2 or len(par) < 2:
        print("Ingrese una letra y un numero, por ejemplo A1")
        return False
    else:
        div = [*par]
        try:
            letra = div[0].upper()
            if letra.upper() in columns.keys():
                pass
            else:
                print(f"{letra} no es una de las opciones validas. las opciones validas son A, B o C")


            numero = 0
            if int(div[1]):
                numero = int(div[1])
                if numero > 0 and numero < 4:
                    return (numero-1, columns[letra])
                else:
                    print(f"{numero} tiene un valor muy alto o muy bajo, los valores tienen que ser 1, 2 o 3")
            else:
                print(f"{div[1]} NO es un numero aceptable")

        except ValueError:
            print(f"Formato `{par}` incorrecto. El formato es A1")
        

    return False

#print(get_row_col("A3"))


