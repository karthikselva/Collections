def perm(str)
  if str.length == 0
    return ['']
  else
    f = str[0..0]
    ps = perm(str[1..-1])
    res = []
    p ps.inspect 
    ps.each do |w|
      (w.length+1).times do |i|
        res << w[0...i]+f+w[i..-1] 
      end 
    end 
    return res 
  end 
end 

p perm('abc').inspect
