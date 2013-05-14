mat = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]

def rotate(img)
  n = img.length 
  (0..(n/2)).each do |layer|
    first = layer 
    last = n - layer - 1
    (first...last).each do |i|
      last_offset = last - ( i - first )
      tmp = img[first][i]
      img[first][i] = img[last_offset][first] 
      img[last_offset][first] = img[last][last_offset]
      img[last][last_offset] = img[i][last]
      img[i][last] = tmp 
    end 
  end 
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
p " Input Matrix "
display(mat)
rotate(mat)
p " Rotated Matrix (90* to right)"
display(mat)

# Output: 
#
#" Input Matrix "
#1 2 3 4
#5 6 7 8
#9 10 11 12
#13 14 15 16
#" Rotated Matrix (90* to right)"
#13 9 5 1
#14 10 6 2
#15 11 7 3
#16 12 8 4
