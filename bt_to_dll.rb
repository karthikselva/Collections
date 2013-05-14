class Tree
  attr_accessor :right , :left , :data
  def initialize(d,l,r)
    @right = r
    @left = l
    @data = d
  end 

  def display 
    puts @data 
    @right.display if !@right.nil?
    @left.display if !@left.nil?
  end 

  def bt_to_dll(node)
    if node.nil? 
      return node
    end 

    if !node.left.nil?
      tleft = bt_to_dll(node.left)
      while !tleft.right.nil?
        tleft = tleft.right 
      end 
      tleft.right = node 
      node.left = tleft
    end 

    if !node.right.nil?
      tright = bt_to_dll(node.right)
      while !tright.left.nil?
        tleft = tright.left
      end 
      tright.left = node 
      node.right = tright
    end 
  end

  def get_dll 
    if self.nil?
      return 
    end 

    troot = bt_to_dll(self)
    while !troot.left.nil?
      troot = troot.left 
    end 
    return troot
  end
end 

test_tree = Tree.new(5,Tree.new(3,Tree.new(1,nil,nil),Tree.new(4,nil,nil)),
        Tree.new(7,Tree.new(6,nil,nil),Tree.new(8,nil,nil)))

puts test_tree.get_dll
#
