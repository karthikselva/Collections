def clear_and_set(n,m,i,j)
	if j >= n.length or i < 0
		return 'ERROR'
	end 
	# Create a mask of all 1's
	mask = (1 << (n.length+1)) - 1
	# Create right mask with ones only till end
	right = (1 << (n.length-j)) -1
	# Shift the mask till 'i' and merge with right
	mask = ((mask << (j-i)) << (n.length-j)) | right
	# Reset all these bits at 'n'
	cleard = n.to_i(2) & mask
	# Prepare m for appropriate place
	m = (m.to_i(2) << (n.length-j-1))
	# Merge 'm' into 'n'
	cleard = cleard | m
	return cleard.to_s(2)
end

p clear_and_set('100000000','10011',2,6)

# Output:
# karthiks-MacBook-Pro-2:code karthikselvakumarbhuvaneswaran$ ruby merge_m_to_n_bit.rb
# "101001100"