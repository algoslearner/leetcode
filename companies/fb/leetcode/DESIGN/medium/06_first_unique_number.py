'''
You have a queue of integers, you need to retrieve the first unique integer in the queue.

Implement the FirstUnique class:

FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
void add(int value) insert value to the queue.
 

Example 1:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]
[[[2,3,5]],[],[5],[],[2],[],[3],[]]
Output: 
[null,2,null,2,null,3,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([2,3,5]);
firstUnique.showFirstUnique(); // return 2
firstUnique.add(5);            // the queue is now [2,3,5,5]
firstUnique.showFirstUnique(); // return 2
firstUnique.add(2);            // the queue is now [2,3,5,5,2]
firstUnique.showFirstUnique(); // return 3
firstUnique.add(3);            // the queue is now [2,3,5,5,2,3]
firstUnique.showFirstUnique(); // return -1
Example 2:

Input: 
["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]
[[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]
Output: 
[null,-1,null,null,null,null,null,17]
Explanation: 
FirstUnique firstUnique = new FirstUnique([7,7,7,7,7,7]);
firstUnique.showFirstUnique(); // return -1
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3]
firstUnique.add(3);            // the queue is now [7,7,7,7,7,7,7,3,3]
firstUnique.add(7);            // the queue is now [7,7,7,7,7,7,7,3,3,7]
firstUnique.add(17);           // the queue is now [7,7,7,7,7,7,7,3,3,7,17]
firstUnique.showFirstUnique(); // return 17
Example 3:

Input: 
["FirstUnique","showFirstUnique","add","showFirstUnique"]
[[[809]],[],[809],[]]
Output: 
[null,809,null,-1]
Explanation: 
FirstUnique firstUnique = new FirstUnique([809]);
firstUnique.showFirstUnique(); // return 809
firstUnique.add(809);          // the queue is now [809,809]
firstUnique.showFirstUnique(); // return -1
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^8
1 <= value <= 10^8
At most 50000 calls will be made to showFirstUnique and add.
'''

#########################################################################################
# Brute force: TLE
# TC: add : O(1), showfirstUniq: O(N2)
# SC: O(N)

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.queue = deque(nums)

    def showFirstUnique(self) -> int:
        for item in self.queue:
            if self.queue.count(item) == 1:
                return item
        return -1

    def add(self, value: int) -> None:
        self.queue.append(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)


############################################################################################
# using two sets
'''
nums_all_set: contains all the numbers that appeared so far
nums_dup_set: contains all the numbers that appeared more than once
idx: the first possible index for the answer in the queue

Time complexity :
constructor: O(K) (Where K = len(nums))
add(): O(1)
showFirstUnique(): O(1) (amortized).

Space complexity : O(N)
'''

class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums_all_set = set()
        self.nums_dup_set = set()
        self.queue = []
        self.idx = 0
        
        for num in nums:
            self.add(num)
        
    def showFirstUnique(self) -> int:
        while self.idx < len(self.queue):
            if self.queue[self.idx] not in self.nums_dup_set:
                return self.queue[self.idx]
            else:
                self.idx += 1
        return -1

    def add(self, value: int) -> None:
        if value in self.nums_all_set:
            self.nums_dup_set.add(value)
        self.nums_all_set.add(value)
        self.queue.append(value)
