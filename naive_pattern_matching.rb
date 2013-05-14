# Complexity: O((n-m+1)*m) 
def naive_search(source,find)
  i = 0 
  j = 0
  (source.length-find.length).times do |i|
    find.length.times do |j|
      if source[i+j] != find[j]
        break 
      end 
    end 
    if j == (find.length-1) 
      return i 
    end 
  end
  return -1
end

source = "THIS IS A TEST STRING"
find="TEST"

p naive_search(source,find)
