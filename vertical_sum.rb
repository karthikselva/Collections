SUM = Hash.new(0)
class Tree
  attr_accessor :right , :left , :data
  def initialize(d,l,r)
    @right = r
    @left = l
    @data = d
  end 
  
  def vertical_sums(node,dist=0)
    if !node.nil?
      SUM[dist] += node.data 
      vertical_sums(node.left,dist-1)
      vertical_sums(node.right,dist+1)
    end 
  end
end 

test_tree = Tree.new(5,Tree.new(3,Tree.new(1,nil,nil),Tree.new(4,nil,nil)),
        Tree.new(7,Tree.new(6,nil,nil),Tree.new(8,nil,nil)))

test_tree.vertical_sums(test_tree)
puts SUM.inspect

# Output:
# {0=>15, -1=>3, -2=>1, 1=>7, 2=>8}
