# // LeetCode解法
#
# class LRUCache {
#
#     private Map<Integer, Node> map;
#     private List list;
#     private int capacity;
#
#     public LRUCache(int capacity) {
#         this.capacity = capacity;
#         map = new HashMap<>();
#         list = new List();
#     }
#
#     public int get(int key) {
#         Node node = map.get(key);
#         if (node == null) {
#             return -1;
#         }
#         int res = node.val;
#         list.addNodeToHead(node, true);
#         return res;
#     }
#
#     public void put(int key, int value) {
#         Node node = map.get(key);
#         if (node != null) {
#             node.val = value;
#             list.addNodeToHead(node, true);
#             return;
#         }
#         node = new Node(key, value);
#         if (map.size() == capacity) {
#             map.remove(list.removeLast().key);
#         }
#         map.put(key, node);
#         list.addNodeToHead(node, false);
#     }
#
#     private class Node {
#         private int key;
#         private int val;
#         private Node prev;
#         private Node next;
#         Node(int key, int val) {
#             this.key = key;
#             this.val = val;
#         }
#     }
#
#     private class List {
#         private Node head;
#         private Node tail;
#         List() {
#             head = new Node(0, 0);
#             tail = new Node(0, 0);
#             head.next = tail;
#             tail.prev = head;
#         }
#
#         private void addNodeToHead(Node node, boolean exist) {
#             if (exist) {
#                 remove(node);
#             }
#             Node first = head.next;
#             node.next = first;
#             first.prev = node;
#             head.next = node;
#             node.prev = head;
#         }
#
#         private Node remove(Node node) {
#             node.prev.next = node.next;
#             node.next.prev = node.prev;
#             return node;
#         }
#
#         private Node removeLast() {
#             Node last = tail.prev;
#             return remove(last);
#         }
#     }
# }
#
#
# // Generic 解法
#
# public class Q_0146_LRU_Cache {
#
#
#    public static void main(String[] args) {
#        LRUCache<Integer, Integer> cache = new LRUCache<>(2);
#        cache.put(1, 1);
#        cache.put(2, 2);
#        System.out.println(cache.get(1));       // returns 1
#        cache.put(3, 3);                        // evicts key 2
#        System.out.println(cache.get(2));       // returns -1 (not found)
#        cache.put(4, 4);                        // evicts key 1
#        System.out.println(cache.get(1));       // returns -1 (not found)
#        System.out.println(cache.get(3));       // returns 3
#        System.out.println(cache.get(4));       // returns 4
#    }
#
#
#    static class LRUCache<K, V> {
#
#
#        private Map<K, Node<K, V>> map;
#        private List<K, V> list;
#        private int capacity;
#
#
#        public LRUCache(int capacity) {
#            map = new HashMap<>();
#            list = new List<>();
#            this.capacity = capacity;
#        }
#
#
#        public V get(K key) {
#            Node<K, V> node = map.get(key);
#            if (node == null) {
#                return null;
#            }
#            V val = node.val;
#            list.addFirst(list.remove(node));
#            return val;
#        }
#
#
#        public void put(K key, V value) {
#            Node<K, V> node = map.get(key);
#            if (node != null) {
#                node.val = value;
#                list.addFirst(list.remove(node));
#                return;
#            }
#            node = new Node<>(key, value);
#            if (map.size() == capacity) {
#                map.remove(list.removeLast().key);
#            }
#            list.addFirst(node);
#            map.put(key, node);
#        }
#    }
#
#
#    /*================== private class members ==================*/
#
#
#    private static class Node<K, V> {
#        private K key;
#        private V val;
#        private Node<K, V> prev;
#        private Node<K, V> next;
#
#
#        Node(K key, V val) {
#            this.key = key;
#            this.val = val;
#        }
#    }
#
#
#    private static class List<K, V> {
#        Node<K, V> head;
#        Node<K, V> tail;
#        List() {
#            head = new Node<>(null, null);
#            tail = new Node<>(null, null);
#            head.next = tail;
#            tail.prev = head;
#        }
#
#
#        private void addFirst(Node<K, V> node) {
#            Node<K, V> first = head.next;
#            head.next = node;
#            node.prev = head;
#            node.next = first;
#            first.prev = node;
#        }
#
#
#        private Node<K, V> remove(Node<K, V> node) {
#            node.next.prev = node.prev;
#            node.prev.next = node.next;
#            return node;
#        }
#
#
#        private Node<K, V> removeLast() {
#            Node<K, V> last = tail.prev;
#            return remove(last);
#        }
#    }
# }

class Node():
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.prev = None
        self.next = None


class Lists():
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def addNodeToHead(self, node, exist):
        if exist:
            self.remove(node)
        first = self.head.next
        node.next = first
        first.prev = node
        self.head.next = node
        node.prev = self.head

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node

    def removeLast(self):
        last = self.tail.prev
        return self.remove(last)


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = collections.defaultdict(Node)
        self.lst = Lists()

    def get(self, key: int) -> int:
        node = self.map[key] if key in self.map else None
        if node is None:
            return -1
        res = node.val
        self.lst.addNodeToHead(node, True)
        return res

    def put(self, key: int, value: int) -> None:
        node = self.map[key] if key in self.map else None
        if node is not None:
            node.val = value
            self.lst.addNodeToHead(node, True)
            return
        node = Node(key, value)
        if len(self.map) == self.capacity:
            self.map.pop(self.lst.removeLast().key, None)
        self.map[key] = node
        self.lst.addNodeToHead(node, False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)