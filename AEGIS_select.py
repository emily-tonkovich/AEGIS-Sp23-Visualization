from importData import *
from classes import *

def selectPhase(phases, nodeData, branchData):
    nodeList = []
    branchList = []
    options= ['A', 'B', 'C']
    vals= [options[x] for x in phases] #Finds which phases are selected
    for node in nodeData.values():
        if any(ele in node.phases for ele in vals): #Checks if phase contains any checked phases
            nodeList.append(node.label)
    for branch in branchData.values():
        if any(ele in branch.phases for ele in vals):
            branchList.append(branch.label)
    return nodeList, branchList

def selectVolt(volt, nodeData):
    nodeList = []
    for node in nodeData.values():
        if volt == node.baseV: #Checks if node matches voltage specified
            nodeList.append(node.label)
    return nodeList
