def isBalanced(self, root):
    def check(node):
        if not node:
            return 0
    
        left = check(node.left)
        right = check(node.right)
        
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return check(root) != -1