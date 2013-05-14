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

	def find_length
		root = self 
		l = 0
		while !root.nil?
			l += 1
			root = root.next
		end 
		return l
	end

	def is_palindrome
		st = []
		node = self
		l = 0
		while !node.nil?
			if l <= (find_length/2)
				st.push(node.data)
			end
			
			if l >= (find_length/2) and st[-1].eql?(node.data)
				st.pop()
			end
			node = node.next 
			l += 1
		end
		return st.empty?
	end

end


test_list = List.new(1)
test_list.next = List.new(2)
test_list.next.next = List.new(3)
test_list.next.next.next = List.new(2)
test_list.next.next.next.next = List.new(1)

p test_list.is_palindrome