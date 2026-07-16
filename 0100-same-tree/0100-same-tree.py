class Solution:
    def isSameTree(self, p, q) -> bool:
    
        # check if p and q both null 
        if not p and not q: 
            return True

        ## check if p or q one of them is null 
        if not p or not q:
            return False

        ## compare the value of p and q
        if p.val != q.val:
            return False

        ## return True (if the trees are same) 
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 