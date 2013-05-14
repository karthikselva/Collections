a = [3,5,4,1,2,7,8,6]

def merge(a,left=0,right=-1)
  p "left: #{left} right: #{right}"
  if left == right
    return
  else
    mid = (left + right)/2
    merge(a,left,mid)
    merge(a,mid,right)
    return 
  end 
end

p merge(a,0,a.length)
