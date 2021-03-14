# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
#
#
#
# Example 1:
#
#
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
# Example 2:
#
# Input: n = 1
# Output: [["Q"]]


# store the result
# each row , the column position of the queen
# [1,3, 0 , 2]
# loop the column, if current condition , [1, 3], current row is 2, what number can be put in the list


#is valid :

# since we put row by row, we avoid the horizonal conflict
# diagnal conflict: 1.for each eleement on the diagnal,
#                   horizontal coordinate and vertical coordinate diff is the same
#                    2. for each eleement on the diagnal,
# #                   horizontal coordinate and vertical coordinate sum is the same


