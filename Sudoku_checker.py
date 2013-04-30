def row_check(sudoku):
# @param sudoku: list; list of the rows of the sudoku
# @return boolean; true if every rows contain no repetitions
  oki = []
  for row in sudoku: 
   bool_matrix = [false,false,false]              
   number = [1,2,3]                               
   for elem in row:
     pos = number.index(elem)
     bool_matrix[pos] = true
   if bool_matrix == [true,true,true] :
     oki.append(true)
   else:
    oki.append(false)
  if oki[0] and oki[1] and oki[2]:
   return true
  else:
   return false
  
  
    