# Public int closetValue(TreeNode root, int target) {
# 	Return closetValue(root, target, root.val);
#
# }

# Private int findCloset(TreeNode node, int target, int min) {
# 	if(node == null) return min;
# 	if(target == node.val)
# return node.val;
# 	Min  = Math.abs(node.val - tartget) < Math.abs(min - target) ? node.val: min;
#
# 	if(target < node.val) {
# 	Min = findCloset(node.left,target,min);
# }else {
# 	Min = findCloset(node.right, target,min);
# }
# 	Return min;
# }


