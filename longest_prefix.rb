class TrieNode
  attr_accessor :value , :child , :is_end 

  def initialize(ch)
    @value = ch 
    @child = {}
  end 
end 

class Trie 
  attr_accessor :root 
  def initialize()
    @root = TrieNode.new('0')
  end 

  def display
    tmp = @root 
    queue = [tmp] 
    parent = nil
    while !queue.empty?
      parent = queue 
      queue = []
      parent.each do |tmp|
        print "#{tmp.value}(#{tmp.is_end})  "
        tmp.child.each do |key,value|
          queue << value 
        end
      end 
      puts ""
    end 
  end 

  def insert(word)
    crawl = @root
    word.length.times do |i|
      child = crawl.child 
      existing = child[word[i..i]] 
      if existing
        crawl = existing 
      else
        tmp = TrieNode.new(word[i..i])
        child[word[i..i]] = tmp 
        crawl = tmp 
      end 
    end 
    crawl.is_end = true 
  end 

  def longest_prefix(word)
    crawl = @root 
    valid_level = 0
    word.length.times do |i|
      child = crawl.child 
      crawl = child[word[i..i]]
      if crawl and crawl.value.eql?(word[i..i]) and crawl.is_end
        valid_level = i+1
      end 
    end 
    return word[0...valid_level]
  end
end 

trie = Trie.new 
trie.insert('karthik')
trie.insert('me')
trie.insert('karthikselvakumar')
trie.insert('karthikkumar')
trie.insert('cracking')
trie.display
p trie.longest_prefix('karthik')
