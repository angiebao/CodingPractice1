# 381. Insert Delete GetRandom O(1) - Duplicates allowed
# public class Q_0381_Insert_Delete_GetRandom_O_1_Duplicates_allowed {
#
#
#    public static void main(String[] args) {
#        RandomizedCollection collection = new RandomizedCollection();
#        System.out.println(collection.insert(1)); // -> true
#        System.out.println(collection.list);
#        System.out.println(collection.insert(1)); // -> false
#        System.out.println(collection.list);
#        System.out.println(collection.insert(2)); // -> true
#        System.out.println(collection.list);
#        System.out.println(collection.getRandom());
#        System.out.println(collection.list);
#        System.out.println(collection.remove(1)); // -> true
#        System.out.println(collection.list);
#        System.out.println(collection.getRandom());
#        System.out.println(collection.list);
#    }
#
#
#    // allow duplicate random set
#    static class RandomizedCollection {
#
#
#        private Map<Integer, Set<Integer>> map; // value -> set of indices
#        private List<Integer> list;
#        private Random random;
#
#
#        /** Initialize your data structure here. */
#        public RandomizedCollection() {
#            map = new HashMap<>();
#            list = new ArrayList<>();
#            random = new Random();
#        }
#
#
#        /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
#        public boolean insert(int val) {
#            boolean res = !map.containsKey(val);
#            insertToMap(val, list.size());
#            list.add(val);
#            return res;
#        }
#
#
#        /** Removes a value from the collection. Returns true if the collection contained the specified element. */
#        public boolean remove(int val) {
#            if (!map.containsKey(val)) {
#                return false;
#            }
#            int lastIdx = list.size()-1;
#            int lastVal = list.remove(lastIdx);
#            // remove last element and update map
#            removeFromMap(lastVal, lastIdx);
#            if (lastVal != val) {
#                // 1. find the indices for 'val'
#                // 2. pick one index out of the above indices
#                // 3. replace it with last element
#                // 4. update map with the new idx mapping, remove `val` and insert `lastVal`
#                Set<Integer> set = map.get(val);
#                int idx = set.iterator().next();
#                list.set(idx, lastVal);
#                removeFromMap(val, idx);
#                insertToMap(lastVal, idx);
#            }
#            return true;
#        }
#
#
#        /** Get a random element from the collection. */
#        public int getRandom() {
#            int idx = random.nextInt(list.size());
#            return list.get(idx);
#        }
#
#
#        /*============== private section ==============*/
#        private void insertToMap(int val, int idx) {
#            Set<Integer> set = map.computeIfAbsent(val, k -> new HashSet<>());
#            set.add(idx);
#        }
#
#        private void removeFromMap(int val, int idx) {
#            Set<Integer> set = map.get(val);
#            set.remove(idx);
#            if (set.isEmpty()) {
#                map.remove(val);
#            }
#        }
#    }
# }


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # map store (value, index in list) in map
        # lst store values

        self.map = collections.defaultdict(set)
        self.lst = []

    # Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        res = True if val not in self.map else False
        self.map[val].add(len(self.lst))
        self.lst.append(val)
        return res

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if len(self.map[val]) == 0: return False

        # one way
        # removeIdx = self.map[val].pop()
        # lastIdx = self.lst[-1]
        # self.lst[removeIdx] = last
        # self.map[lastIdx].add(removeIdx)
        # self.map[lastIdx].remove(len(self.lst) - 1)
        # self.lst.pop()

        # the other way
        # cannot remove like this, because even this value is the last element in list, what we removed might not be the last index
        # rmIdx  = self.map[val].pop()
        lastIdx = len(self.lst) - 1
        lastVal = self.lst.pop()
        # different from  380, we first remove the last element in map
        self.map[lastVal].remove(lastIdx)

        # if the removed element is the last element we are done, otherwise we need to replace the to be removed element with the last element index(keep the last element)
        if lastVal != val:
            # randomly pic an index of the particular value
            rmIdx = self.map[val].pop()
            # put back the last element in the list
            self.lst[rmIdx] = lastVal
            # append the rmIdx to the last value's set
            self.map[lastVal].add(rmIdx)

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return choice(self.lst)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()