# public class Q_0023_Merge_k_Sorted_Lists {
#
#
#    public static void main(String[] args) {
#        Q_0023_Merge_k_Sorted_Lists solution = new Q_0023_Merge_k_Sorted_Lists();
#        ListNode l1 = Util.buildList(new int[]{1,4,5});
#        ListNode l2 = Util.buildList(new int[]{1,3,4});
#        ListNode l3 = Util.buildList(new int[]{2,6});
#        ListNode[] lists = new ListNode[]{l1, l2, l3};
#        Util.printListNode(solution.mergeKLists(lists));
#    }
#
#
#    public ListNode mergeKLists(ListNode[] lists) {
#        Queue<ListNode> pq = new PriorityQueue<>((a, b) -> a.val - b.val);
#        for (ListNode node : lists) {
#            if (node != null) {
#                pq.offer(node);
#            }
#        }
#        ListNode dummy = new ListNode(0);
#        ListNode curr = dummy;
#        while (!pq.isEmpty()) {
#            ListNode node = pq.poll();
#            curr.next = node;
#            curr = curr.next;
#            if (node.next != null) {
#                pq.offer(node.next);
#            }
#        }
#        return dummy.next;
#    }
# }