def row_check(sudoku):
# @param sudoku: list; list of the rows of the sudoku
# @return boolean; true if every rows contain no repetitions
  oki = []                                        #Boolean Matrix. Its purpose is to control that every rows is correct
  for row in sudoku:                             
   bool_matrix = [false,false,false]              #Boolean Matrix. Its purpose is to control that every element are present just one time         
   number = [1,2,3]                               # 9 element if you want to check a 9x9 sudoku
   for elem in row:
     pos = number.index(elem)                     #If a number is present set the value of the matrix as "true"
     bool_matrix[pos] = true
   if bool_matrix == [true,true,true] :           #If the Boolean Matrix contains only true values, the row is correct and the program will append the true value
     oki.append(true)
   else:
    oki.append(false)
  if oki[0] and oki[1] and oki[2]:               #Every rows is ok? Yes or no
   return true
  else:
   return false
  
  
    
