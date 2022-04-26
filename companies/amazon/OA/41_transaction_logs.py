# https://leetcode.com/discuss/interview-question/989768/Amazon-or-OA-2020-or-Transaction-logs
'''
A Company parses logs of online store user transactions/activity to flag fraudulent activity.

The log file is represented as an Array of arrays. The arrays consist of the following data:

[ <# of transactions>]

For example:

[345366 89921 45]

Note: the data is space delimited

So, the log data would look like:

[
[345366 89921 45],
[029323 38239 23]
...
]
Write a function to parse the log data to find distinct users that meet or cross a certain threshold.

The function will take in 2 inputs:
logData: Log data in form an array of arrays

threshold: threshold as an integer

Output:
It should be an array of userids that are sorted.

If same userid appears in the transaction as userid1 and userid2, it should count as one occurrence, not two.

Example:
Input:
logData:

[
[345366 89921 45],
[029323 38239 23],
[38239 345366 15],
[029323 38239 77],
[345366 38239 23],
[029323 345366 13],
[38239 38239 23]
...
]
threshold: 3

Output: [345366 , 38239, 029323]
Explanation:
Given the following counts of userids, there are only 3 userids that meet or exceed the threshold of 3.

345366 -4 , 38239 -5, 029323-3, 89921-1
'''

# Solution idea with question description: https://github.com/phoenix-254/Amazon-OA/blob/main/transaction_logs.java

Python solution using hashMap + hashSet
N: # of logData line
M: # of user ids in logData
Time: O(N)
Space: O(M)

from collections import defaultdict


def transactionLog(logData, threshold):
    hashTable, res = defaultdict(int), set()
    for line in logData:
        userId1, userId2, uselessData = line.split()
        if userId1 != userId2:
            hashTable[userId2] += 1
        hashTable[userId1] += 1
        if hashTable[userId1] >= threshold:
            res.add(userId1)
        if hashTable[userId2] >= threshold:
            res.add(userId2)
    return sorted(res)


if __name__ == '__main__':
    print(transactionLog([
    '345366 89921 45',
    '029323 38239 23',
    '38239 345366 15',
    '029323 38239 77',
    '345366 38239 23',
    '029323 345366 13',
    '38239 38239 23'
    ], 3)) # ['029323', '345366', '38239']

    print(transactionLog([
    '345366 89921 45',
    '029323 38239 23',
    '38239 345366 15',
    '029323 38239 77',
    '345366 38239 23',
    '029323 345366 13',
    '38239 38239 23'
    ], 4)) # ['345366', '38239']

    print(transactionLog([
    '345366 89921 45',
    '029323 38239 23',
    '38239 345366 15',
    '029323 38239 77',
    '345366 38239 23',
    '029323 345366 13',
    '38239 38239 23'
    ], 5)) # ['38239']
    
 You need to return res.sort(key='int')
# Amazon Transaction Logs Problem: https://leetcode.com/playground/k5mQfFb5
