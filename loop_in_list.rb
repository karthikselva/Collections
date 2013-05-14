class List
	attr_accessor :next , :data 
	def initialize(d)
		self.data = d
	end

	def has_loop
		hare,tortoise = self,self
		while !hare.nil? and !hare.next.nil?
			tortoise = tortoise.next 
			hare = hare.next.next
			if hare.eql?(tortoise)
				return true
			end
		end
		return false
	end

  def remove_loop 
  	hare,tortoise = self,self
		while !hare.nil? and !hare.next.nil?
			tortoise = tortoise.next 
			hare = hare.next.next
			if hare.eql?(tortoise)
				break
			end
		end

    hare = self 
    while !tortoise.nil? and !hare.eql?(tortoise.next)
      hare = hare.next 
      tortoise = tortoise.next 
    end
    tortoise.next = nil 
  end 

end


test_list = List.new(1)
test_list.next = List.new(2)
test_list.next.next = List.new(3)
test_list.next.next.next = List.new(4)
test_list.next.next.next.next = List.new(5)
test_list.next.next.next.next.next = test_list.next.next

p test_list.has_loop
test_list.remove_loop
p test_list.has_loop
