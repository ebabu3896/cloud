#In DFS if there is an restriction to not use recursive. 
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

    def inorder(root):
        stack = []
        curr = root

        while curr or stack:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                print(curr.val)
                curr = curr.right

    def preorder(root):
        stack = []
        curr = root

        while curr or stack:
            if curr:
                print(curr.val)
                if curr.right:
                    stack.append(curr.right)
                curr = curr.left
            else:
                curr = stack.pop()

    # In post order first we need to update left side of tree then right side of tree then root value.
    def postorder(root):
        stack = [root]
        visit = [False]

        while stack:
            curr, visited = stack.pop(), visit.pop()
            if curr:
                if visited:
                    print(curr.val)
                else:
                    stack.append(curr)
                    visit.append(True)
                    stack.append(curr.right)
                    visit.append(False)
                    stack.append(curr.left)
                    visit.append(False)
