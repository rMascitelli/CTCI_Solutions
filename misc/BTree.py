# Binary Tree code

# Binary Tree Node
class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxDepth(root):
        """
        :type root: TreeNode
        :rtype: int
        """
        cur_depth = 0
        max_depth = 0
        stack = []
        
        # temp node for traversing
        t = root
        
        while(True):
            if(cur_depth > max_depth):
                    max_depth = cur_depth
            
            # Append to the stack, if possible
            if(t):
                cur_depth += 1
                stack.append(t)
                t = t.left
                
            # If anything left in stack, pop from stack and move right from there
            elif(stack):
                t = stack.pop()
                t = t.right
                if(not(t)):
                    cur_depth -= 1
            
            else:
                break
                    
        return max_depth

""" Example binary tree is 
            1 
          /   \ 
         2     3 
       /  \ 
      4    5
            \
             7          """
  
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5)
root.left.right.right = Node(7)
root.left.right.right.right = Node(8)

print("maxDepth =", maxDepth(root))
