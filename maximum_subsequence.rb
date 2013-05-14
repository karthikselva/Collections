arr = [ -1,1,2,-1,8,-3,5,7,-4,-2,9,-2,4,-5] 

start = 0
ending = 0 
maxsofar = 0 
maxendinghere = 0

def max(i,j)
  if i > j
    return i 
  else 
    return j 
  end 
end

arr.each_with_index do |val,i|
  maxendinghere = max(maxendinghere + val,0)
  if maxendinghere > maxsofar 
    ending = i
    maxsofar = maxendinghere
  end 
end 

sum = 0 
# Backtrack to find the start 
# Another n traversal => 2n :: O(n)
(0..ending).to_a.each do |from_end|
  sum += arr[ending - from_end]
  if sum == maxsofar
    start = arr.length - from_end
  end 
end 
p " starting from index: #{start}"
p " ending at index: #{ending}"
p "Maximum sum is: #{maxsofar}" 
# Output:
#" starting from index: 3"
#" ending at index: 12"
#"Maximum sum is: 24"
