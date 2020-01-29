""" Given an array arr of strings landPerimeter function calculates the total perimeter of all the islands. 
Each piece of land will be marked with 'X' while the water fields are represented as 'O'. 
Consider each tile being a perfect 1 x 1piece of land. Example of arr below:
['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO']    """

def land_perimeter(arr):
    board_list = [[x for x in elem] for elem in arr]
    count = 0
    for x in range(len(board_list)):
        if board_list[x][0] == "X" : count +=1
        if board_list[x][-1] == "X" : count += 1 
        for y in range(len(board_list[x])-1):
            if (board_list[x][y] + board_list[x][y+1]) == "XO" or (board_list[x][y] + board_list[x][y+1]) == "OX":
                count += 1
    for x in range(len(board_list)-1):
        for y in range(len(board_list[x])):    
            if (board_list[x][y] + board_list[x+1][y]) == "XO" or (board_list[x][y] +board_list[x+1][y]) == "OX":
                count += 1
    for y in range(len(board_list[0])):
        if board_list[0][y] == "X":
            count += 1
        if board_list[-1][y] == "X":
            count += 1     

    return "Total land perimeter: {}".format(count)
