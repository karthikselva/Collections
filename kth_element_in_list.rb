
class List
	attr_accessor :next , :data 
	def initialize(d)
		self.data = d
	end

	def print_list
		root = self 
		while !root.nil?
			print "#{root.data} => "
			root = root.next
		end 
		p "NULL"
	end

	def kth_element(node,k,l=0)
		return nil if node.nil?
		list = kth_element(node.next,k,l+1)
		if k == l
			return node 
		end 
		return list
	end

end


test_list = List.new(1)
test_list.next = List.new(2)
test_list.next.next = List.new(3)
test_list.next.next.next = List.new(2)
test_list.next.next.next.next = List.new(1)

p test_list.kth_element(test_list,2).data

#Output:
# karthiks-MacBook-Pro-2:code karthikselvakumarbhuvaneswaran$ ruby kth_element_in_list.rb
# => 3