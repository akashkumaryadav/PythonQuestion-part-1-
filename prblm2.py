import numpy as np

row = col = int(input("Enter the number of rows of square matrix"))
cornerValue = input("first charachter")
borderValue = input("second charachter")
centerValue = input("third charachter")

if row and col > 3 and row and col < 10:
    cr = cc = 0
    corners = [(0, 0), (0, row-1), (col-1, 0), (row-1, col-1)]
    center = cr > 0 and cr < row-1 and cc > 0 and cc < col-1
    sqmatrix = np.array(range(row*col), dtype=str).reshape(row, col)

    # filling the matrix with data
    for cr in range(row):
        for cc in range(col):
            if (cr, cc) in corners:
                sqmatrix[cr][cc] = cornerValue
            elif cr > 0 and cr < row-1 and cc > 0 and cc < col-1:
                sqmatrix[cr][cc] = centerValue
            else:
                sqmatrix[cr][cc] = borderValue

    for r in range(row):
        for c in range(col):
            print(sqmatrix[r][c], end=" ")
        print()
else:
    print("Size out of range")
