def get_first(str)
	str[0..0]
end

def exclude_first(str)
	str[1..-1]
end 

def subsets(set)
	if set.length > 0
		all_sets = subsets(exclude_first(set))
		all_sets.clone.each do |val|
			all_sets << val+get_first(set)
		end	
		return all_sets
	else
		return [set]
	end
end 

puts subsets('abcd').sort.inspect

#Output:
#["", "a", "b", "ba", "c", "ca", "cb", "cba", "d", "da", "db", "dba", "dc", "dca", "dcb", "dcba"]
