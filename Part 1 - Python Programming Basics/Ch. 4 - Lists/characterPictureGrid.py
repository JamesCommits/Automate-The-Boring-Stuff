grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

# You can think of grid[x][y] as being the character at the x- and y- coordinates of a 'picture' drawn with text characters.
# The (0,0) origin will be in the upper-left corner, the x-coordinates increase going right and the y-coordinates
# increase going down.  Copy the previous grid value, and write code that uses it to print the image

for j in range(len(grid[0])):
    for i in range(len(grid)):
        print(grid[i][j],end='')
    print('')