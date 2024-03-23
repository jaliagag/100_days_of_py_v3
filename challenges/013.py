#Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].
#
#Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.
#
#For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.


board = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def get_row_col(par: str, option: str):
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
                    pass
                else:
                    print(f"{numero} tiene un valor muy alto o muy bajo, los valores tienen que ser 1, 2 o 3")
            else:
                print(f"{div[1]} NO es un numero aceptable")

        except ValueError:
            print(f"Formato `{par}` incorrecto. El formato es A1")
        
    column = columns[letra]
    print(f"columns {columns[letra]}\t rows {numero}")
    board[column][numero-1] = option
    for i in board:
        print(i)

    return par




turn = 1
plays = []
for i in range(9):
    print(f"Turno {turn}")

    if turn % 2 == 0:
        p2 = input("Ingrese su jugada: ")
        get_row_col(p2,"X")

        turn += 1
    else:
        p1 = input("Ingrese su jugada: ")
        get_row_col(p1,"O")
        turn += 1


#get_row_col("a2")
