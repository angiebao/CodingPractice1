# Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
#
# Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.
#
# It is possible that several messages arrive roughly at the same time.
#
# Example:
#
# Logger logger = new Logger();
#
# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true;
#
# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;
#
# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;
#
# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;
#
# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;
#
# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;


# 359. Logger Rate Limiter
# public class Q_0359_Logger_Rate_Limiter {
#
#
#    public static void main(String[] args) {
#
#
#        // 方法1: bucket
#        Logger1 logger1 = new Logger1();
#        System.out.println(logger1.shouldPrintMessage(1, "foo"));
#        System.out.println(logger1.shouldPrintMessage(2, "bar"));
#        System.out.println(logger1.shouldPrintMessage(3, "foo"));
#        System.out.println(logger1.shouldPrintMessage(8, "bar"));
#        System.out.println(logger1.shouldPrintMessage(10, "foo"));
#        System.out.println(logger1.shouldPrintMessage(11, "foo"));
#
#
#        Util.printSeparator();
#
#
#        // 方法2: Simple HashMap
#        Logger2 logger2 = new Logger2();
#        System.out.println(logger2.shouldPrintMessage(1, "foo"));
#        System.out.println(logger2.shouldPrintMessage(2, "bar"));
#        System.out.println(logger2.shouldPrintMessage(3, "foo"));
#        System.out.println(logger2.shouldPrintMessage(8, "bar"));
#        System.out.println(logger2.shouldPrintMessage(10, "foo"));
#        System.out.println(logger2.shouldPrintMessage(11, "foo"));
#
#
#        Util.printSeparator();
#
#
#        // 方法3: 维护Queue & Set
#        Logger3 logger3 = new Logger3();
#        System.out.println(logger3.shouldPrintMessage(1, "foo"));
#        System.out.println(logger3.shouldPrintMessage(3, "bar"));
#        System.out.println(logger3.shouldPrintMessage(3, "foo"));
#        System.out.println(logger3.shouldPrintMessage(8, "bar"));
#        System.out.println(logger3.shouldPrintMessage(10, "foo"));
#        System.out.println(logger3.shouldPrintMessage(11, "foo"));
#    }
#
#
#    static class Logger1 {
#
#
#        private static final int SECONDS = 10;
#        int[] times;
#        Set<String>[] logs;
#
#
#        /** Initialize your data structure here. */
#        public Logger1() {
#            times = new int[SECONDS];
#            logs = new Set[SECONDS];
#            for (int i = 0; i < SECONDS; i++) {
#                logs[i] = new HashSet<>();
#            }
#        }
#
#
#        /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
#         If this method returns false, the message will not be printed.
#         The timestamp is in seconds granularity. */
#        public boolean shouldPrintMessage(int timestamp, String message) {
#            int idx = timestamp % SECONDS;
#            if (timestamp != times[idx]) {
#                times[idx] = timestamp;
#                logs[idx].clear();
#            }
#            for (int i = 0 ; i < SECONDS; i++) {
#                if (timestamp - times[i] < SECONDS && logs[i].contains(message)) {
#                    return false;
#                }
#            }
#            logs[idx].add(message);
#            return true;
#        }
#    }
#
#
#    static class Logger2 {
#
#
#        private static final int SECONDS = 10;
#        Map<String, Integer> map;
#
#
#        /** Initialize your data structure here. */
#        public Logger2() {
#            map = new HashMap<>();
#        }
#
#
#        /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
#         If this method returns false, the message will not be printed.
#         The timestamp is in seconds granularity. */
#        public boolean shouldPrintMessage(int timestamp, String message) {
#            if (timestamp < map.getOrDefault(message, 0)) {
#                return false;
#            }
#            map.put(message, timestamp + 10);
#            return true;
#        }
#    }
#
#
#    static class Logger3 {
#
#
#        private static final int SECONDS = 10;
#        Queue<Pair> q;
#        Set<String> set;
#
#
#        /** Initialize your data structure here. */
#        public Logger3() {
#            q = new LinkedList<>();
#            set = new HashSet<>();
#        }
#
#
#        /** Returns true if the message should be printed in the given timestamp, otherwise returns false.
#         If this method returns false, the message will not be printed.
#         The timestamp is in seconds granularity. */
#        public boolean shouldPrintMessage(int timestamp, String message) {
#            cleanObsolete(timestamp);
#            if (set.contains(message)) {
#                return false;
#            }
#            q.offer(new Pair(message, timestamp));
#            set.add(message);
#            return true;
#        }
#
#        private void cleanObsolete(int timestamp) {
#            while (!q.isEmpty() && timestamp - q.peek().timestamp >= SECONDS) {
#                set.remove(q.poll().message);
#            }
#        }
#
#        private static class Pair {
#            String message;
#            int timestamp;
#            Pair(String message, int timestamp) {
#                this.message = message;
#                this.timestamp = timestamp;
#            }
#        }
#    }
# }