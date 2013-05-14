
a = [1001,1001,1002,1003,1004,1004,1005]

def find(array,key,pos=0)
  if key < array[pos] or key > array[-1]
    return false
  elsif key > array[pos]
    return find(array,key,pos+(key-array[pos]))
  elsif key == array[pos]
    return true
  end 
end 

p find(a,1004)
p find(a,1009)
p find(a,10)
p find(a,1001)
