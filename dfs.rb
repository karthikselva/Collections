def dfs(root)
  if root.blank?
    return 
  end
  root.visited = true
  root.adjacent.each do |node|
    unless root.visited
      dfs(node)
    end
  end 
end 

