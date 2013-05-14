def gcd(a,b)
  if b == 0
    return a
  else
    return gcd(b,a%b)
  end 
end

p gcd(8,11)
