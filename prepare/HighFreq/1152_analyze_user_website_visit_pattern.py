

import itertools
import collections

class Solution(object):
    def mostVisitedPattern(self, username, timestamp, website):
        """
        :type username: List[str]
        :type timestamp: List[int]
        :type website: List[str]
        :rtype: List[str]
        """
        #
        mapping = collections.defaultdict(list)
        n = len(username)
        # zip to a tuple so that we can sort by timestamp

        pack_tuples = zip(timestamp, username, website)
        pack_tuples = sorted(pack_tuples, key=lambda x: x[0])

        # put all in dictionary use username as keyvalues

        for (t, u, w) in pack_tuples:
            mapping[u].append(w)

        count = collections.defaultdict(int)
        # count the sequence in dictionary
        for u, map_list in mapping.items():
            # no repeated 3 sequence in one user, this will generate tuple

            # combos_r = itertools.combinations(map_list, 3)
            # for combo in combos_r:
            #     print(combo)

            combos = set(itertools.combinations(map_list, 3))
            for combo in combos:
                count[combo] += 1

        sorted_count = sorted(count, key=lambda x: (-count[x], x))

        return sorted_count[0]


username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"]
timestamp = [1,2,3,4,5,6,7,8,9,10]
website = ["home","about","career","home","cart","maps","home","home","about","career"]
s=Solution()
s.mostVisitedPattern(username,timestamp,website )
# pack_tuples = list(zip(timestamp, username, website))
# pack_tuples1 = sorted( pack_tuples, key=lambda x: x[0])
#
# print(pack_tuples)
# print(pack_tuples1)