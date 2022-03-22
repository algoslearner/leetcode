'''
On a single-threaded CPU, we execute a program containing n functions. Each function has a unique ID between 0 and n-1.

Function calls are stored in a call stack: when a function call starts, its ID is pushed onto the stack, and when a function call ends, its ID is popped off the stack. The function whose ID is at the top of the stack is the current function being executed. Each time a function starts or ends, we write a log with the ID, whether it started or ended, and the timestamp.

You are given a list logs, where logs[i] represents the ith log message formatted as a string "{function_id}:{"start" | "end"}:{timestamp}". For example, "0:start:3" means a function call with function ID 0 started at the beginning of timestamp 3, and "1:end:2" means a function call with function ID 1 ended at the end of timestamp 2. Note that a function can be called multiple times, possibly recursively.

A function's exclusive time is the sum of execution times for all function calls in the program. For example, if a function is called twice, one call executing for 2 time units and another call executing for 1 time unit, the exclusive time is 2 + 1 = 3.

Return the exclusive time of each function in an array, where the value at the ith index represents the exclusive time for the function with ID i.

 Example 1:

Input:
n = 2
logs = 
["0:start:0",
 "1:start:2",
 "1:end:5",
 "0:end:6"]
Output:[3, 4]
Explanation:
Function 0 starts at time 0, then it executes 2 units of time and reaches the end of time 1. 
Now function 0 calls function 1, function 1 starts at time 2, executes 4 units of time and end at time 5.
Function 0 is running again at time 6, and also end at the time 6, thus executes 1 unit of time. 
So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally execute 4 units of time.
'''

###############################################################################################
# STACK
# Time : O(n)
# Space : O(n)

class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        output = [0] * n
        
        stack = []
        for log in logs:
            cols = log.split(':')
            fn_id = int(cols[0])
            timestamp = int(cols[2])
            
            if cols[1] == 'start':
                stack.append((fn_id,timestamp))
            else:
                curr_id, curr_start = stack.pop()
                curr_fn_time = timestamp - curr_start + 1
                output[curr_id] += curr_fn_time
                
                if len(stack) != 0:
                    prev_fn_id = stack[-1][0]
                    output[prev_fn_id] -= curr_fn_time
        
        return output
