from collections import OrderedDict


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        # use dictionary
        self.d = OrderedDict()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.d:
            self.d.move_to_end(key, last=True)
            return self.d[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #         if key in self.d:
        #             self.d[key] = value
        #         elif len(self.d) == self.capacity :
        #             self.d.popitem(last = False) # move item from  beginning
        #             self.d[key] = value

        #         self.d.move_to_end(key, last = True)

        if key in self.d:
            self.d[key] = value

        else:
            if len(self.d) == self.capacity:
                self.d.popitem(last=False)
            self.d[key] = value

        self.d.move_to_end(key, last=True)