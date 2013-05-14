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

  def zigzag
    result = []
    currentlevel = []
    nextlevel = []

    toggle = false 
    currentlevel.push(self)

    while !currentlevel.empty?
      tree = currentlevel.pop
      unless tree.nil?
        result << tree.data
        if toggle
          nextlevel.push(tree.right)
          nextlevel.push(tree.left)
        else 
          nextlevel.push(tree.left)
          nextlevel.push(tree.right)
        end
      end

      if currentlevel.empty?
        toggle = !toggle 
        tmp = currentlevel 
        currentlevel = nextlevel 
        nextlevel = tmp 
      end
    end
    return result
  end

end 

test_tree = Tree.new(5,Tree.new(3,Tree.new(1,nil,nil),Tree.new(4,nil,nil)),
        Tree.new(7,Tree.new(6,nil,nil),Tree.new(8,nil,nil)))

puts test_tree.zigzag.inspect
#test_tree.display
