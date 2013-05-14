class List
  attr_accessor :data , :next 
  def initialize(tdata,tnext)
    @data = tdata
    @next = tnext
  end 

  def display
    tmp = self 
    print "ROOT"
    while !tmp.nil?
      print "->#{tmp.data}"
      tmp = tmp.next 
    end 
    print "->NULL\n" 
  end 

end 

list = List.new(1,List.new(2,List.new(3,List.new(4,List.new(5,nil)))))
list.display
