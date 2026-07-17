class Solution:
    def isSubtree(self, root, subRoot) -> bool:
        # 1. The Base Cases
        if not subRoot: 
            return True
        if not root: 
            return False
            
        # 2. current node check
        if self.isSameTree(root, subRoot):
            return True
            
        # 3. The Delegation
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p, q) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)