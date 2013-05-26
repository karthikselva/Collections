class Result 
  attr_accessor :node , :result 
  def initialize(n,r)
    @node = n 
    @result = r 
  end 
end 

class List
  attr_accessor :data , :next 
  def initialize(d,n)
    @data = d 
    @next = n 
  end 

  def self.new_with_string(str)
    if str.empty? 
      return null 
    end 
    root = List.new(str[0..0],nil)
    tmp = root
    str[1..-1].split(//).each do |chr|
      tmp.next = List.new(chr,nil)
      tmp = tmp.next 
    end 
    return root 
  end 

  def display
    tmp = self 
    while !tmp.nil?
      print "#{tmp.data} -> "
      tmp = tmp.next
    end 
    puts " NULL"
  end 

  def is_palindrome 
    tmp = self 
    len = 0
    while !tmp.nil?
      tmp = tmp.next 
      len+=1
    end 
    res = Result.new(nil,true)
    is_palindrome_util(self,len,res)
    p res.result
  end 

  def is_palindrome_util(node=self,length,res)
    if length == 1
      res.node = node.next 
      res.result = true 
      return
    end 

    if length == 2 and res.node.next.data == node.data 
      res.node = res.node.next.next
      res.result = true 
      return
    end 

    is_palindrome_util(node.next,length-2,res)
    if res.result
      res.result = (res.node.data == node.data) 
      p "Comparing #{res.node.data} with #{node.data} result #{res.result} with length #{length}"
      res.node = res.node.next 
    end 
  end 
end 

palin = List.new_with_string('malayalam')
palin.display
p palin.is_palindrome
non_palin = List.new_with_string('karthik')
non_palin.display
p non_palin.is_palindrome
