# AEGIS - Distribution System Visualization Software
# Imports, cleans, and reassigns node and branch data
# Lucas Manalo
# 9/27/22

from classes import *

def importData():
    # Imports and cleans node data
    with open('example_node_data.txt', 'r') as nodeFile:
        nodeTxtData = nodeFile.readlines()[2:]

    # Creates a list of node obejcts
    nodeData = []
    for line in nodeTxtData:
        line = line.split()
        nodeData.append(Node(
            int(line[0][:-1]), # index
            line[1][:-1], # label
            line[2][:-1], # phases
            float(line[3]) # base voltage
        ))

    # Imports and Cleans Branch Data
    with open('example_branch_data.txt', 'r') as branchFile:
        branchTxtData = branchFile.readlines()[2:]

    # Creates a list of node obejcts
    branchData = []
    for line in branchTxtData:
        line = line.split()

        if line[6] == "N/A":
            line[6] = 0

        branchData.append(Branch(
            int(line[0][:-1]), # index
            line[1][:-1],   # label
            line[2][:-1],   # type
            line[3][:-1],   # phases 
            int(line[4][:-1]), # from node 
            int(line[5][:-1]), # to node 
            float(line[6])  # length
        ))
    return(nodeData, branchData)