def get_perm(str)
  return [] if str.nil?
  return [''] if str.length == 0
  perms = []
  start = str[0]
  rem = str[1..-1]
  res = get_perm(rem)
  res.each do |word|
    (0..word.length).each do |i|
      tmp = word[0...i]+start+word[i..-1] 
      perms << tmp
    end 
  end 
  return perms 
end 

p get_perm(ARGV.first).inspect
