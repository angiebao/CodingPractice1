# 380. Insert Delete GetRandom O(1)
# public class Q_0380_Insert_Delete_GetRandom_O_1 {
#
#
#    public static void main(String[] args) {
#        RandomizedSet randomSet = new RandomizedSet();
#        System.out.println(randomSet.insert(1)); // -> true
#        System.out.println(randomSet.remove(2)); // -> false
#        System.out.println(randomSet.insert(2)); // -> true
#        System.out.println(randomSet.getRandom());
#        System.out.println(randomSet.remove(1)); // -> true
#        System.out.println(randomSet.insert(2)); // -> false
#        System.out.println(randomSet.getRandom());
#    }
#
#
#    // no duplicates randomized set
#    static class RandomizedSet<T> {
#
#
#        private Map<Integer, Integer> map; // val -> index map
#        private List<Integer> list; // holding all values
#        private Random random;
#
#
#        /** Initialize your data structure here. */
#        public RandomizedSet() {
#            map = new HashMap<>();
#            list = new ArrayList<>();
#            random = new Random();
#        }
#
#
#        /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
#        public boolean insert(int val) {
#            if (map.containsKey(val)) {
#                return false;
#            }
#            map.put(val, list.size());
#            list.add(val);
#            return true;
#        }
#
#
#        /** Removes a value from the set. Returns true if the set contained the specified element. */
#        public boolean remove(int val) {
#            if (!map.containsKey(val)) {
#                return false;
#            }
#
#
#            int rmIdx = map.remove(val);
#            int lastVal = list.remove(list.size()-1);
#            // if last element is the element to be removed, we are done
#            // otherwise, we replace the element to be removed with the last element (at index `rmIdx`)
#            if (lastVal != val) {
#                list.set(rmIdx, lastVal);
#                map.put(lastVal, rmIdx);
#            }
#            return true;
#        }
#
#
#        /** Get a random element from the set. */
#        public int getRandom() {
#            int idx = random.nextInt(list.size());
#            return list.get(idx);
#        }
#    }
# }

# Your input
# ["RandomizedSet","remove","remove","insert","getRandom","remove","insert"]
# [[],[0],[0],[0],[],[0],[0]]
# Output
# [null,false,false,true,0,true,true]
# Expected
# [null,false,false,true,0,true,true]


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = dict()
        self.lst = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.map:
            return False
        self.map[val] = len(self.lst)
        self.lst.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.map:
            return False
        # remove the element in the map, no need to random remove, becasue there is no duplicate
        # remove the value from map
        rmIdx = self.map.pop(val, None)
        # see if the last value is the val to remove
        lastVal = self.lst.pop()
        # if the last element is the element to remove, we are done
        # otherwise, since we popped out the last value in lst, we replace the element to to be removed with the last element, we know how to replace because we have the map tell us the remove index
        if lastVal != val:
            # replace the element to be removed with the last element
            self.lst[rmIdx] = lastVal
            # then update the mapping
            self.map[lastVal] = rmIdx
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.lst:
            return []
        return choice(self.lst)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
