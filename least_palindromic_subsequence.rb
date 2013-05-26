def lps(str,start,send)
  if start == send
    return 1
  elsif start+1 == send 
    if str[start] == str[send]
      return 2 
    else
      return 1
    end 
  elsif str[start] == str[send]
    return lps(str,start+1,send-1) + 2
  else 
    return [lps(str,start,send-1),lps(str,start+1,send)].max
  end 
end 

str = 'paybzba'
p lps(str,0,str.length-1)

