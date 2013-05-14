
def swap(str,from,to)
	t = str.clone
	d = t[from]
	c = t[to]
	t[from] = c 
	t[to] = d 
	return t 
end 

def perms(set,i=0)
	p set
	l = set.length
	if i == l
		return 
	end 

	(l-i).times do |index|
		perms(swap(set,index+i-1,0),i+1)
	end
end 

perms('abc')