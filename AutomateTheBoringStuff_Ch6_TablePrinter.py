tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable():
    to_print = ""
    col_widths = [0] * len(tableData)

    x = 0
    for i in tableData:
        col_widths[x] = len(max(i, key=len))
        x = x + 1

    for i in range(0, len(tableData[0])):
        for j in range(len(tableData)):
            if j == len(tableData) - 1:
                to_print += ((tableData[j][i]).rjust(col_widths[j]) + "\n")
            else:
                to_print += ((tableData[j][i]).rjust(col_widths[j]) + " ")

    return to_print


print(printTable())
