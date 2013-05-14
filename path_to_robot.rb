realtime_grid = [
[1,0,0,1,0],
[1,1,0,0,0],
[1,1,1,1,1],
[0,0,0,0,1]
]

def is_safe(x,y,mat)
  return mat[x][y].eql?(1) ? true : false
end 

def path_finder(x,y,mat,path)
  path << [x,y] 
  if x == 0 and y == 0
    return true 
  end 

  success = false 
  if x >= 1 and is_safe(x-1,y,mat)
    success = path_finder(x-1,y,mat,path)
  end 

  if !success and y >= 1 and is_safe(x,y-1,mat)
    success = path_finder(x,y-1,mat,path) 
  end 

  if !success
    path.remove([x,y])
  end 

  return success
end 

def display(arr)
  arr.each do |ar|
    ar.each do |i|
      print i
      print ' '
    end 
    puts ""
  end 
end 

path = []
path_finder(realtime_grid.length-1,realtime_grid[0].length-1,realtime_grid,path)
display(realtime_grid)
p path.inspect


#Output:
#-------
#1 0 0 1 0
#1 1 0 0 0
#1 1 1 1 1
#0 0 0 0 1

#"[[3, 4], [2, 4], [2, 3], [2, 2], [2, 1], [1, 1], [1, 0], [0, 0]]"
