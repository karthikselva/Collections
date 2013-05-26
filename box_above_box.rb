class Box
  attr_accessor :width , :height 
  def initialize(width,height)
    @width = width
    @height = height
  end 

  def can_be_above(box)
    return true if box.nil?
    if box.width > @width and box.height > @height 
      return true 
    else
      return false 
    end 
  end 

  def to_s
    "Box(#{@width},#{@height})"
  end
end 

def stack_up(boxes,bottom,cache={})
  
  if !bottom.nil? and !cache[bottom].nil?
    return cache[bottom]
  end 

  max_stack = nil
  boxes.each do |box|
    if box.can_be_above(bottom)
      stack = stack_up(boxes,box)
      if max_stack.nil? or stack.size > max_stack.size
        max_stack= stack
      end 
    end 
  end 

  max_stack = [] if max_stack.nil?
  max_stack << bottom unless bottom.nil? 
  cache[bottom] = max_stack
  return max_stack
end 

boxes = [Box.new(1,1),Box.new(2,2),Box.new(1,4),Box.new(3,4),Box.new(2,4)]
p stack_up(boxes,nil).inspect

