def safe?(board,row,col)
  display(board)
  p "received: row=#{row} col=#{col}"

  (0..col).each do |r|
    p "horizontal: (#{r},#{col})"
    if board[row][r] == 1
      return false
    end 
  end 

  r = row 
  c = col 
  while r >= 0 and c >= 0
    p "upper diagonal: (#{r},#{c})"
    if board[r][c] == 1
      return false 
    end 
    r -= 1
    c -= 1
  end 

  r = row 
  c = col 
  while r < board.length and c >= 0
    p " low diagonal: (#{r},#{c})"
    if board[r][c] == 1
      return false 
    end 
    r += 1
    c -= 1
  end 

  return true
end 

def solve(board,col=0)
  if col >= board.length
    return true
  end 
  (0...board.length).each do |i|
    if safe?(board,i,col)
      board[i][col] = 1 
      if solve(board,col+1)
        return true
      end 
    end
    p "Backtracking .. "
    board[i][col] = 0
  end 
  return false 
end 

def display(array)
  array.each do |a|
    p a.inspect 
  end 
end
if !ARGV.first.nil?
  N = ARGV.first.to_i
else
  N = 4
end
board  = []
N.times do 
  board << [0]*N
end 

solve(board)
display(board)
