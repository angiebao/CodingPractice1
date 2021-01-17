Def findValue(root, target):
	If root is None:
		return

	If target < root.val

		findValue(root.left, target)
	elif target > root.val:
		findValue(root.right, target)
	Else:
		res=true



# public boolean searchBST2(TreeNode root, int val) {
#        TreeNode curr = root;
#        while (curr != null) {
#            if (val < curr.val) {
#                curr = curr.left;
#            } else if (val > curr.val) {
#                curr = curr.right;
#            } else {
#                return true;
#            }
#        }
#        return false;
#    }