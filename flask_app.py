from flask import Flask,request

app = Flask(__name__)

def print_board(b):
    x = ""
    for row in range(len(b)):

        if row % 3 == 0 and row != 0:
            x += "----------------------------------<br/>"

        for col in range(len(b[row])):

            if col % 3 == 0 and col != 0:
                x += " &nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;" + " {} ".format(b[row][col])
            elif col == 8:
                x += " {} ".format(b[row][col])+"<br/>"
            else:
                x += " {} ".format(b[row][col])

    return x


def find_empty(b):
    for row in range(len(b)):
        for col in range(len(b[row])):
            if b[row][col] == 0:
                return row, col
    return None


def valid(b, pos, num):
    # check row
    for col in range(len(b[pos[0]])):
        if b[pos[0]][col] == num and pos[1] != col:
            return False

    # check col
    for row in range(len(b)):
        if b[row][pos[1]] == num and pos[0] != row:
            return False

    #check box
    box_row = pos[0] // 3
    box_col = pos[1] // 3

    for row in range(box_row*3,(box_row*3)+3):
        for col in range(box_col*3, (box_col*3)+3):
            if b[row][col] == num and row != pos[0] and col != pos[1]:
                return False

    return True


def solve(b):
    find = find_empty(b)
    if not find:
        return True
    else:
        row, col = find

        for i in range(1, 10):
            if valid(b,(row, col), i):
                b[row][col] = i

                if solve(b):
                    return True

                b[row][col] = 0

        return False





@app.route("/")
def answer():
    sudoku = []
    for i in range(1,10):
        x = request.args.get("row{}".format(i))
        sudoku.append([int(i) for i in x])

    solve(sudoku)
    return print_board(sudoku)
