# https://leetcode.com/discuss/interview-question/1112778/Amazon-OA
'''
'''
# Ques: https://aonecode.com/interview-question/maximum-bounded-array

def MaxBoundedArray(n, low, up):
	total = (up - low) * 2 + 1
	if (n > total or up < low or n < 3):
		return None
	# if above check is passed, there definitely exists a solution
	q = collections.deque()
	# create the decreasing part
	for ele in range(up, low-1, -1):
		q.append(ele)
	# case 1: decreasing part has length >= n
	if len(q) >= n:
		while len(q) > n-1:
			q.pop()
		q.appendleft(up-1)
		return list(q)
	# case 2: decreasing part has length < n, so now we can just append left elements
	else:
		for ele in range(up-1, low-1, -1):
			q.appendleft(ele)
			if len(q) == n:
				return list(q)
