def row_check():        
# @param sudoku: list; list of the rows of the sudoku
# @return boolean; true if every rows contain no repetition
  sudoku = randos()
  oki = []                                        #Boolean Matrix. Its purpose is to control that every rows is correct
  for row in sudoku:                             
   bool_matrix = 9*[False]             #Boolean Matrix. Its purpose is to control that every element are present just one time         
   number = [1,2,3,4,5,6,7,8,9]                               # 9 element if you want to check a 9x9 sudoku
   for elem in row:
     pos = number.index(elem)                     #If a number is present set the value of the matrix as "true"
     bool_matrix[pos] = True
   if bool_matrix == 9*[True] :           #If the Boolean Matrix contains only true values, the row is correct and the program will append the true value
     oki.append(True)
   else:
    oki.append(False)
  if oki == 2*[True]:               #Every rows is ok? Yes or no
   return True
  else:
   return False

def randos():
# @return sudoku: list; A sudoku matrix
  import random 
  sudoku = []
  row = []
  for y in range(0,9):
    row.append(random.randrange(1,9))
  for x in range(0,9):
   sudoku.append(row)
  return sudoku
  
  
  
    
