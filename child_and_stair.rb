# Child and Stairs 
def find_chances_for(n)
	if n < 0
		return 0
	elsif n == 0
		return 1
	else 
		return ( find_chances_for(n-3) + 
				 find_chances_for(n-2) +
				 find_chances_for(n-1) )
	end 
end 
p find_chances_for(3)

# Output 
# ------
# 4
# Explanation
# -----------
# They are 
# (1,1,1)
# (1,2)
# (2,1)
# (3)