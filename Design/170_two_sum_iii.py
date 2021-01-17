# Design a data structure that accepts a stream of integers and checks if it has a pair of integers that sum up to a particular value.
#
# Implement the TwoSum class:
#
# TwoSum() Initializes the TwoSum object, with an empty array initially.
# void add(int number) Adds number to the data structure.
# boolean find(int value) Returns true if there exists any pair of numbers whose sum is equal to value, otherwise, it returns false.
#
#
# Example 1:
#
# Input
# ["TwoSum", "add", "add", "add", "find", "find"]
# [[], [1], [3], [5], [4], [7]]
# Output
# [null, null, null, null, true, false]
#
# Explanation
# TwoSum twoSum = new TwoSum();
# twoSum.add(1);   // [] --> [1]
# twoSum.add(3);   // [1] --> [1,3]
# twoSum.add(5);   // [1,3] --> [1,3,5]
# twoSum.find(4);  // 1 + 3 = 4, return true
# twoSum.find(7);  // No two integers sum up to 7, return false

#
# public class Q_0170_Two_Sum_III_Data_structure_design {
#
#
#    public static void main(String[] args) {
#        TwoSum1 twoSum11 = new TwoSum1();
#        twoSum11.add(1);
#        twoSum11.add(3);
#        twoSum11.add(5);
#        System.out.println(twoSum11.find(4));
#        System.out.println(twoSum11.find(7));
#
#
#        Util.printSeparator();
#
#
#        TwoSum1 twoSum12 = new TwoSum1();
#        twoSum12.add(3);
#        twoSum12.add(1);
#        twoSum12.add(2);
#        System.out.println(twoSum12.find(3));
#        System.out.println(twoSum12.find(6));
#
#
#        Util.printSeparator();
#
#
#        TwoSum2 twoSum21 = new TwoSum2();
#        twoSum21.add(1);
#        twoSum21.add(3);
#        twoSum21.add(5);
#        System.out.println(twoSum21.find(4));
#        System.out.println(twoSum21.find(7));
#
#
#        Util.printSeparator();
#
#
#        TwoSum2 twoSum22 = new TwoSum2();
#        twoSum22.add(3);
#        twoSum22.add(1);
#        twoSum22.add(2);
#        System.out.println(twoSum22.find(3));
#        System.out.println(twoSum22.find(6));
#    }
#
#
#
#
#    /*
#        LeetCode Time Limit Exceeded: 14 / 16 test cases passed.
#        Time complexity:  read/find - O(1), write/add - O(n)
#        Space complexity: O(n^2) where num set uses O(n) space but sum set uses upto O(n^2) space
#        where n is the unique count of numbers
#     */
#    static class TwoSum1 {
#
#
#        private Set<Integer> num;
#        private Set<Integer> sum;
#        /** Initialize your data structure here. */
#        public TwoSum1() {
#            num = new HashSet<>();
#            sum = new HashSet<>();
#        }
#
#
#        /** Add the number to an internal data structure.. */
#        public void add(int number) {
#            for (int n : num) {
#                sum.add(n + number);
#            }
#            num.add(number);
#        }
#
#
#        /** Find if there exists any pair of numbers which sum is equal to the value. */
#        public boolean find(int value) {
#            return sum.contains(value);
#        }
#    }
#
#
#    /*
#        Passes LeetCode test cases
#        Time complexity:  read/find - O(n), write/add - O(1)
#        Space complexity: O(n)
#        where n is the unique count of numbers
#     */
#    static class TwoSum2 {
#
#
#        private Map<Integer, Integer> map;
#
#
#        /** Initialize your data structure here. */
#        public TwoSum2() {
#            map = new HashMap<>();
#        }
#
#
#        /** Add the number to an internal data structure.. */
#        public void add(int number) {
#            map.put(number, map.getOrDefault(number, 0) + 1);
#        }
#
#
#        /** Find if there exists any pair of numbers which sum is equal to the value. */
#        public boolean find(int value) {
#            for (int num : map.keySet()) {
#                int complement = value - num;
#                if (complement != num && map.containsKey(complement)) return true;
#                if (complement == num && map.get(num) >= 2) return true;
#            }
#            return false;
#        }
#    }
# }


# add not efficient, find efficient
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num = set()
        self.sum = set()

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        for n in self.num:
            self.sum.add(n + number)

        self.num.add(number)

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """

        if value in self.sum:
            return True

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)



# add efficient, find not efficient

class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = defaultdict(int)

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.map[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.map.keys():
            complement = value - num
            if complement != num and (complement in self.map):
                return True
            elif complement == num and self.map[num] >= 2:
                return True

        return False

# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)