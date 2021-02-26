
# class Solution {
#     public TreeNode constructFromPrePost(int[] pre, int[] post) {
#         if(pre.length == 0 || post.length == 0) {
#             return null;
#         }
#         return helper(pre, 0, pre.length - 1, post, 0, post.length - 1);
#     }
#
#     public TreeNode helper(int[]pre, int preStart, int preEnd, int[]post, int postStart, int postEnd) {
#         if(preStart > preEnd || postStart > postEnd) {
#             return null;
#         }
#         TreeNode root = new TreeNode(pre[preStart]);
#         int index = postEnd - 1;
#         while(index >= postStart && post[index] != pre[preStart + 1]) {
#             index --;
#         }
#         int left = index - postStart + 1;
#
#         root.left = helper(pre,  preStart + 1,        preStart + left, post,      postStart,    index);
#         root.right = helper(pre, preStart + left + 1, preEnd,          post,      index + 1,    postEnd - 1);
#         return root;
#     }
# }

# find the root position in post order
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        return self.helper(pre, 0, len(pre) - 1, post, 0, len(post) - 1)

    def helper(self, preorder, pre1, pre2, postorder, post1, post2):
        if pre1 > pre2 or post1 > post2:
            return None

        root = TreeNode(preorder[pre1])
        index = post2 - 1

        while index >= post1 and postorder[index] != preorder[pre1 + 1]:
            index -= 1

        # index is based on post order, if there is inorder list, usually the index is based on inorder
        leftCount = index - post1 + 1
        root.left = self.helper(preorder, pre1 + 1, pre1 + leftCount, postorder, post1, index)
        root.right = self.helper(preorder, pre1 + leftCount + 1, pre2, postorder, index + 1, post2 - 1)
        return root