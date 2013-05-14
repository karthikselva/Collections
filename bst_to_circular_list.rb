class Tree
  attr_accessor :right , :left , :data
  def initialize(d,l,r)
    @right = r
    @left = l
    @data = d
  end 

  def join(a,b)
    a.left = b 
    b.right = a
  end 

  def append(a,b)
    return b if a.nil?
    return a if b.nil?

    aLast = a.left 
    bLast = b.left 

    join(aLast,b)
    join(bLast,a)

    return a
  end

  def bst_to_circular(node)
    return nil if node.nil?

    aList = bst_to_circular(node.left)
    bList = bst_to_circular(node.right)
    
    node.left = node 
    node.right = node 

    aList = append(aList,node)
    aList = append(bList,node)

    return aList
  end

  def print_list
    node = self.right
    p self.data 
    while !node.eql?(self)
      puts node.data 
      node = node.right 
    end 
  end
end 

test_tree = Tree.new(5,Tree.new(3,Tree.new(1,nil,nil),Tree.new(4,nil,nil)),
        Tree.new(7,Tree.new(6,nil,nil),Tree.new(8,nil,nil)))
test_tree.bst_to_circular(test_tree)
test_tree.print_list
