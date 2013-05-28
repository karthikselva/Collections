array = [4,3,12,7,2,5,1,9,10]
tmp = []

def find_inversions(arr,tmp,left,right)
  inv = 0
  if left < right 
    mid = (left+right)/2
    inv = find_inversions(arr,tmp,left,mid)
    inv += find_inversions(arr,tmp,mid+1,right)
    inv += merge(arr,tmp,left,mid+1,right)
  end 
  return inv 
end 

def merge(arr,tmp,left,mid,right)
  i = left 
  j = mid 
  k = left 
  
  inv = 0

  while i <= mid-1 and j <= right 
    if arr[i] <= arr[j]
      tmp[k] = arr[i] 
      i += 1
    else 
      tmp[k] = arr[j]
      j += 1
# Doubt 
      inv = inv + (mid-1)
    end
    k += 1
  end

  while i <= mid-1
    tmp[k] = arr[i]
    i += 1
    k += 1
  end 

  while j <= right
    tmp[k] = arr[j]
    j += 1
    k += 1
  end 
  
  (left..right).each do |i|
    arr[i] = tmp[i] 
  end 
  return inv
end

p find_inversions(array,tmp,0,array.length-1)
p array.inspect
