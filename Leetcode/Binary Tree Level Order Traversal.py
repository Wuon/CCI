class Solution:
    def levelOrder(self, root: 'TreeNode') -> 'List[List[int]]':
        store = []
        s = set()
        self.helper(root, store, s)
        return store

    def helper(self, root, store, s, i=0):
        if not root:
            return
        if i not in s:
            s.add(i)
            store.append([])
        store[i].append(root.val)
        self.helper(root.left, store, s, i + 1)
        self.helper(root.right, store, s, i + 1)
