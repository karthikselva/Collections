def get_max_sum(num)
  if num < 1
    return 0
  else
    return (26**num)+get_max_sum(num-1)
  end 
end 

def cal_sum(st)
  sum = get_max_sum(st.length - 1)
  st.length.times do |i|
    sum += (st[i]-97)*(26**(st.length-i-1))
  end 
  return sum
end

p cal_sum('abc')
