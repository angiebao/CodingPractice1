# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
#
# Example:
#
# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:
#
# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # use the sliding window technique
        l = 0
        r = 0

        dictT = collections.Counter(t)
        required = len(dictT)

        # formed is used to store if all the requirement is satisfied.
        formed = 0

        # dictionary to keep count of all the unique characters in the current windows
        window_counts = {}
        # a tuple to store the info (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):  # moving right pointer to next until the condition satisfied.
            # add one character from the right of the window

            character = s[r]
            # dictionary.get(character, 0), if the keywords character does not exist, return 0
            # get the count of the character in current window
            window_counts[character] = window_counts.get(character, 0) + 1

            # see if the characters in windowis is engough for the same characters in T
            if character in dictT and window_counts[character] == dictT[character]:
                formed += 1

            # try to reduce the window size by moviing left pointer to next, and still satiesfy the condition
            while l <= r and formed == required:
                character = s[l]

                # save the smallest window till now
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # remove the charcter pointed by the left pointer and see if t is still in s
                window_counts[character] -= 1
                if character in dictT and window_counts[character] < dictT[character]:
                    formed -= 1

                l += 1

            r += 1

        return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]