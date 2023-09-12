import copy
import networkx as nx
import matplotlib
import matplotlib.pyplot as plt
from DataStructures import node,edge
import streamlit as st
from netgraph import Graph,InteractiveGraph

class GraphHandler():
	def __init__(self):
		self.graphState={
			"nodes":[],
			"edges":[]
		}
	def clearState(self):
		self.graphState["nodes"]=[]
		self.graphState["edges"]=[]

	def updateGraph(self,updates):
		current_graph=copy.deepcopy(self.graphState)
		if len(updates)==0:
			return
		if type(updates[0])==str:
			updates=[updates]
		for update in updates:
			if len(update)==3:
				entity1=update[0]
				relation=update[1]
				entity2=update[2]

				node1=node(id=entity1,label=entity1)
				node2=node(id=entity2,label=entity2)

				if node1 not in current_graph["nodes"]:
					current_graph["nodes"].append(node1)
				if node2 not in current_graph["nodes"]:
					current_graph["nodes"].append(node2)
				edges=edge(_from=entity1,_to=entity2,label=relation)
				if edge not in current_graph["edges"]:
					current_graph["edges"].append(edges)
		self.graphState["nodes"]=current_graph["nodes"]
		self.graphState["edges"]=current_graph["edges"]

	def init_networkx(self):
		self.G = nx.DiGraph()
		for node_data in self.graphState["nodes"]:
			self.G.add_node(node_data.id, label=node_data.label, color=node_data.color)
		for edge_data in self.graphState["edges"]:
			self.G.add_edge(edge_data._from, edge_data._to, label=edge_data.label)
		self.pos = nx.spring_layout(self.G,seed=10002)  # You can choose different layout algorithms
		self.edge_labels = {(edge[0], edge[1]): edge[2]['label'] for edge in self.G.edges(data=True)}

	def init_figure(self,height,width):
		self.fig, self.ax = plt.subplots(figsize=(height,width))

	def draw_networkx_graph(self):
		nx.draw(self.G,self.pos, with_labels=True, labels=nx.get_node_attributes(self.G, 'label') , node_color=nx.get_node_attributes(self.G, 'color').values(), ax=self.ax)
		nx.draw_networkx_edge_labels(self.G,self.pos, edge_labels=self.edge_labels, font_color='blue', ax=self.ax)

	def show_output(self):
		st.pyplot(self.fig)


	def init_netgraph(self):
		self.netgraph=InteractiveGraph(
			self.G,
			edge_labels=self.edge_labels,
			node_labels=True,
			node_label_fontdict=dict(fontsize=15),
			edge_label_fontdict=dict(fontsize=13),
			ax=self.ax,
			edge_width=0.5,
			node_width=0.5,
			arrows=True,
		)