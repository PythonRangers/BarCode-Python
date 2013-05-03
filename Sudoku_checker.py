def main():
  sudoku = [[4,1,2,5,7,6,9,3,8],[8,6,9,2,3,1,7,5,4],[5,3,7,8,9,4,6,2,1],[9,8,6,3,1,5,4,7,2],[1,4,5,6,2,7,3,8,9],[2,7,3,4,8,9,5,1,6],[7,2,1,9,4,3,8,6,5],[3,5,4,1,6,8,2,9,7],[6,9,8,7,5,2,1,4,3]]
  x = row_check(sudoku)
  matrix = column_creator(sudoku)
  column = column_divider(matrix)
  y = row_check(column)
  if x and y:
    print sudoku
    return true
  return false
  
##############################################################################
  
def row_check(sudoku):        
# @param sudoku: list; list of the rows of the sudoku
# @return boolean; true if every rows contain no repetition
  #sudoku = randos()
  oki = []                                        #Boolean Matrix. Its purpose is to control that every rows is correct
  for row in sudoku:                             
   bool_matrix = 9*[false]             #Boolean Matrix. Its purpose is to control that every element are present just one time         
   number = [1,2,3,4,5,6,7,8,9]                               # 9 element if you want to check a 9x9 sudoku
   for elem in row:
     pos = number.index(elem)                     #If a number is present set the value of the matrix as "true"
     bool_matrix[pos] = true
   if bool_matrix == 9*[true] :           #If the Boolean Matrix contains only true values, the row is correct and the program will append the true value
     oki.append(true)
   else:
    oki.append(false)
  if oki == 9*[true]:               #Every rows is ok? Yes or no
   return true
  else:
   return false
   
##############################################################################

def column_creator(sudoku):
  #sudoku = randos()
  column = []
  columns = []
  for i in range(0,9):
    for j in range(0,9):
      #column.append(sudoku[j][i])
      column = column + [sudoku[j][i]]
  columns.append(column)
  return column
  
##############################################################################
      
def column_divider(matrix):
  #matrix = column_creator()
  new_matrix = []
  row = []
  for y in range(0,9):
    row = []  
    for x in range(0,9):
      row = row + [matrix.pop(0)]
    new_matrix.append(row)
  return new_matrix
  
##############################################################################
  
def randos():
# @return sudoku: list; A sudoku matrix
  from random import randrange 
  sudoku = []
  row = []
  for y in range(0,9):
     row.append([randrange(1,9),randrange(1,9),randrange(1,9),randrange(1,9),randrange(1,9),randrange(1,9),randrange(1,9),randrange(1,9),randrange(1,9)])
  sudoku.extend(row)
  return sudoku