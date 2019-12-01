#!usr/bin/python
# -*- coding: utf-8 -*-
"""This code defines a non binary tree node data structure 
with the associated methods needed in the coding assignement"""

class node:
# this methods 
	def __init__(self, node_id):
        # Node class constructor 
        # args : node_id => tuple ( ID of a new node, ID of the parent node)
		self.id = node_id[0]
		self.parent = node_id[1]
		self.child = []

	def add_child(self, childNode):
		newNode = node((childNode, self.id))
		self.child.append(newNode)
	
	def get_childs(self):
		return [child.id for child in self.child]