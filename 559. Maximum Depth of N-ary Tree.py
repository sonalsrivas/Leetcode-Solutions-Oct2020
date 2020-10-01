"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        '''
        # Using DFS
        depth=0
        def dfs(root,d=1):
            nonlocal depth
            if not root:
                return
            depth=max(depth, d)
            for i in root.children:
                dfs(i, d+1)        
        dfs(root)
        return depth
        '''
        
        # Using BFS
        import queue
        q=queue.Queue()
        if not root:
            return 0
        q.put((root, 1))
        while q.empty()==False:
            p,d=q.get()
            for i in p.children:
                q.put((i,d+1))
        return d
