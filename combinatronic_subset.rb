def subsets(str)
  n = 2 << (str.length - 1)
  result = []  
  n.times do |i|
    result << convert_in_to_set(i,str)
  end
  return result
end 

def convert_in_to_set(x,str)
  tmp = x
  index = 0
  set = ''
  while tmp > 0
    if (tmp & 1) == 1
      set << str[index..index]
    end 
    index = index + 1
    tmp = tmp >> 1 
  end 
  return set 
end 

p subsets('abc')
#["", "a", "b", "ab", "c", "ac", "bc", "abc"]
