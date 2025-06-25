# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []

        level_nodes = [root]
        left_to_right = True
        result = []

        def getChildNodes(nodes):
            new_nodes = []
            for node in nodes:
                if node.left:
                    new_nodes.append(node.left)
                if node.right:
                    new_nodes.append(node.right)
            return new_nodes

        while level_nodes:
            level_values = [node.val for node in level_nodes]
            if not left_to_right:
                level_values.reverse()
            result.append(level_values)

            level_nodes = getChildNodes(level_nodes)
            left_to_right = not left_to_right

        return result
