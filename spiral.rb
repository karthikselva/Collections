require 'pp'
m = [(1..10).to_a]*10
PP.pp m

def spiral(mat,n,layer)
  if n == layer
    return 
  end
  last_row = n-layer
  first = layer
  n.times do |i|
    print "#{mat[first][i+layer]} "
  end 

  (n-1).times do |i|
    print "#{mat[i+1+layer][last_row]} "
  end 

  (n-1).times do |i|
    print "#{mat[last_row][last_row-i]} "
  end 

  (n-2).times do |i|
    print "#{mat[last_row-i][first]} "
  end 
  spiral(mat,n-1,layer+1)
end

spiral(m,m.length-1,0)
