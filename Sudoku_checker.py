def main():
  choice = int(input("Do you want to try a random sudoku or check it in a .txt file? [1/2]: "))
  if choice == 1:	
    sudoku = [[5, 4, 3, 6, 7, 8, 9, 1, 2], [6, 7, 2, 1, 9, 5, 3, 4, 8], [1, 9, 8, 3, 4, 2, 5, 6, 7], [8, 5, 9, 7, 6, 1, 4, 2, 3], [4, 2, 6, 8, 5, 3, 7, 9, 1], [7, 1, 3, 9, 2, 4, 8, 5, 6], [9, 6, 1, 5, 3, 7, 2, 8, 4], [2, 8, 7, 4, 1, 9, 6, 3, 5], [3, 4, 5, 2, 8, 6, 1, 7, 9]]
    x = row_check(sudoku)
    matrix = column_creator(sudoku)
    column = column_divider(matrix)
    y = row_check(column)
    if x and y:
     print sudoku
     return true
    return false
  else:
    sudoku = reader()
    print sudoku
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

##############################################################################

def reader():
  import string 
  path = raw_input('Inserisci il percorso del file: ')
  file = open(path,'r')
  elem = []
  row = []
  while 1:
    line = file.readlines()
    if line == []:
      break
    for i in range(0,len(line)):
     elem = string.split(line[i],"\t")
     for x in range(0,len(elem)):
       row.append(int(elem[x]))
  return column_divider(row)
  file.close()
  
