#-*- coding:utf-8 -*-
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.parent = None
		self.left = None
		self.right = None

def bfs_search(root):
	"""
	input: root of tree
	return: leveltravers tree 
	modify: 2018-2-27
	author: winter
	"""
	if len(root) == None:
		return 
	queue = []                            #初始化队列
	queue.append(root)                    #把根节点加入到队列

	while (len(queue)):
		TreeNode cur = queue.pop(0)
		print(cur.val)                   #遍历打印节点

		if cur.left != None:
			queue.append(cur.left)
		if cur.right != None:
			queue.append(cur.right)

