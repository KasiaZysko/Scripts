""" This script determines how many boats are sunk damaged and untouched from a set amount of attacks. 
You will need to create a function that takes two arguments, the playing board and the attacks.
Example of use:
board = [[0,0,0,2,2,0],
         [0,3,0,0,0,0],
         [0,3,0,1,0,0],
         [0,3,0,1,0,0]]
attacks = [[2, 1], [1, 3], [4, 2]]
damaged_or_sunk(board, attacks) """

def damaged_or_sunk (board, attacks):
    results = {'sunk' : 0, 'damaged' : 0, 'not_touched': 0, 'points':0}
    board_list = [elem for row in board for elem in row]
    ships = {x: board_list.count(x) for x in list(set(board_list))}
    ships_new = dict(ships)
    hit = [board[len(board)-z[1]][z[0]-1] for z in attacks]
    
    for n in hit:
        ships_new[n] -=  1
   
    del ships[0]
    del ships_new[0]  
    
    for key, value in ships_new.items():
        if value == 0: 
            results['sunk'] += 1
            results['points'] += 1
        elif ships_new.get(key) == ships.get(key):
            results['not_touched'] += 1
            results['points'] -= 1
        else:
            results['damaged'] += 1 
            results['points'] += 0.5
          
    return results
