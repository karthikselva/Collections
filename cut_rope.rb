class Rope
  attr_accessor  :price 
  def initialize(p)
    @price = p 
  end
end 

class Pricing 
  attr_accessor :ropes, :benefit 
  def initialize(r)
    @ropes = r
    @benefit = [0]*r.length
  end 

  def max_benefit(val)
    return max_benefit_util(val-1)
  end 

  def max_benefit_util(val)
    if val < 0 or val > (@ropes.length-1)
      return 0 
    elsif val == 0
      benefit[val] = @ropes[0].price
      return @ropes[0].price 
    elsif benefit[val] != 0 
      return benefit[val]
    else 
      max = @ropes[val].price
      val.times do |i|
        p " split as: #{i} + #{val-i-1}"
        tmp = @ropes[i].price + max_benefit_util(val-i-1)
        p "#{val} => #{tmp}"
        if tmp > max 
          max = tmp 
        end 
      end 
      return max 
    end 
  end 

end 

price_list = Pricing.new([
  Rope.new(1,1),
  Rope.new(2,5),
  Rope.new(3,8),
  Rope.new(4,9)
])

p price_list.max_benefit(ARGV.first.to_i)
