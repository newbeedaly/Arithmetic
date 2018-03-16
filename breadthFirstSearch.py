# 广度优先搜索代码
# deque()队列实现
from collections import deque
# import collections
def person_is_seller(name):
	return name[-1] == 'r'
def search(name):
	search_queue = deque()
	search_queue.appendleft(name)
	searched = [] # 这个数组记录检查过的人
	while search_queue:
		person = search_queue.popleft()
		if person not in searched: # 当这个人没有检查过
			if person_is_seller(person):
				print(person+" is a mango seller!")
				return True
			else:
				search_queue.appendleft(name)
				searched.append(person) # 将这个人标记为检查过
				return False

search("mongor")		
