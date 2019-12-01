#!usr/bin/python
# -*- coding: utf-8 -*-
"""This code defines methods to manipulate the structure (adding, extracting ...)"""
from node import node

class Database(object):

	def __init__(self, root_parent = None):
		# Database class constructor 
        # args : root_parent => string (ensemble of all existing objects)
		newNode = node((root_parent, None)) 
		self.root = newNode 
		self.extract = {} # dictionary : contains node features (neighbours & children)

	def add_nodes(self, nodesList):
		for nodeArg in nodesList:
			node = self.search(self.root, nodeArg[1]) # search for node parent
			node.add_child(nodeArg[0])

	def search(self, parent, node_id): 
		# recursive search for a specified node
		# args : parent => node (parent node), node_id 
			if node_id == parent.id:
				return parent
			else:
				r = None
				for node in parent.child:
					if r == None:
						r = self.search(node, node_id)
				return r 

	def add_extract(self, nodes_to_extract):
		# Browse the database (tree) and store the informations
		# args : nodes_to_extract => dictionary ({"image": ["node"],...})
		for image, nodesList in nodes_to_extract.items(): 
			self.extract.update({image : {}})
			for nodeId in nodesList:
				node = self.search(self.root, nodeId)
				if node == None:
					self.extract[image].update({nodeId : None}) # in case of node doesn't exist (invalid)
				else:
					self.extract[image].update({nodeId : {"child" : []	,"neighbours" : []}})

					self.extract[image][nodeId]["child"] = node.get_childs().copy()
					
					parentNodeId = node.parent
					parentNode = self.search(self.root, parentNodeId)
					if parentNode != None :
						self.extract[image][nodeId]["neighbours"]= parentNode.get_childs().copy()



	def get_extract_status(self):
		# returns the status of the considering graph
		status = {} 
		for image, nodeIds in self.extract.items():
			res = "valid"
			for nodeId in nodeIds:
				if self.extract[image][nodeId] == None:
					res = "invalid"
					break
				else:
					node = self.search(self.root, nodeId)
					parentNodeId = node.parent
					parentNode = self.search(self.root, parentNodeId)
					if parentNode != None :
						childsLen = len(parentNode.get_childs().copy())
					else:
						childsLen = 0
					# Tests by node child list lengths
					if len(self.extract[image][nodeId]["neighbours"]) - childsLen != 0:	
						res = "coverage_staged"
					elif len(self.extract[image][nodeId]["child"]) - len(node.get_childs().copy()) != 0:
						if res == "granularity_staged" or res == "valid" :
							res = "granularity_staged"
			status.update({image : res})
		return status



