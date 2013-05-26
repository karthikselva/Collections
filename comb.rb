def get_sub(str,set)
  return [] if str == nil 
  return [''] if str.length == 0
  start = str[0]
  rem = str[1..-1]
  tmp_set = get_sub(rem,set)
  set.concat(tmp_set.clone)
  tmp_set.each do |s|
    set << start+s
  end 
  return set 
end 

p get_sub('abc',[]).inspect
