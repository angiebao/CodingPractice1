# 989. Add to Array-Form of Integer
# public class Q_0989_Add_to_Array_Form_of_Integer {
#
#
#    public static void main(String[] args) {
#        Q_0989_Add_to_Array_Form_of_Integer solution = new Q_0989_Add_to_Array_Form_of_Integer();
#        int[] A1 = {1,2,0,0};
#        int K1 = 34;
#        int[] A2 = {2,7,4};
#        int K2 = 181;
#        int[] A3 = {2,1,5};
#        int K3 = 806;
#        int[] A4 = {9,9,9,9,9,9,9,9,9,9};
#        int K4 = 1;
#        System.out.println(solution.addToArrayForm(A1, K1));
#        System.out.println(solution.addToArrayForm(A2, K2));
#        System.out.println(solution.addToArrayForm(A3, K3));
#        System.out.println(solution.addToArrayForm(A4, K4));
#    }
#
#
#    public List<Integer> addToArrayForm(int[] A, int K) {
#        List<Integer> res = new ArrayList<>();
#        int i = A.length-1;
#        int carry = 0;
#        while (i >= 0 || K != 0 || carry > 0) {
#            int val1 = i >= 0 ? A[i] : 0;
#            int val2 = K % 10;
#
#
#            int sum = val1 + val2 + carry;
#            carry = sum / 10;
#            res.add(sum % 10);
#
#
#            i--;
#            K /= 10;
#        }
#
#
#        Collections.reverse(res);
#        return res;
#    }
# }

# [2,1,2,4]
# integer k = 312
# output [2,4,3,6]
#
# input
# "10011"
def addListNumber(nums, k):
    res = []
    carry = 0
    i = len(nums) - 1

    while i >= 0 or k != 0 or carry > 0:

       val1 =  nums[i] if i >= 0 else 0
       val2 = k % 10

       sums = val1 + val2 + carry
       carry = sums// 10
       res.append(sums % 10)


       i -= 1
       k = k/10

    return res[::-1]
