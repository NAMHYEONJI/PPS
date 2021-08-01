lon = 0

def diameterOfBinaryTree(self, root):
    def dfs(node):
        if not node:
            return -1
        
        left = dfs(node.left)
        right = dfs(node.right)
        
        self.lon = max(self.lon, left + right + 2)
        
        return max(left, right) + 1
    
    dfs(root)
    return self.lon