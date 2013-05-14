def set(array,num)
  ((num**num)..array.length).step(num) do |i|
    array[i-1] = 1
  end 
  return array
end 

def seive(num)
  if num < 2
    return nil
  end 
  a = [0]*num
  (1..num).each do |i|
    if a[i] == 0
      puts "#{i+1}"
      a=set(a,i+1)
    end
  end 

  return a
end 

p seive(50).inspect
##Output
#2
#3
#5
#7
#9
#11
#13
#15
#17
#19
#21
#23
#25
#29
#31
#35
#37
#41
#43
#47
#49
#"[0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1]"
