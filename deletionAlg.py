from classes import *
from deleteData import deleteData

def deletionAlg(nodeData, branchData, delNode):
    queue = [] # nodes which need to be visited
    deleteNodes = [delNode] #nodes to be deleted
    deleteBranches = [] #branches to be deleted

    for b in nodeData[delNode].toBranch: #finds all branches coming from deleted node
        deleteBranches.append(b.label) #Adds following branches to be deleted
        queue.append(b.toNode) #Adds branches to queue
    j = 0
    while j < len(queue): #keeps looping until end of queue
        #Repeats process from earlier
        deleteNodes.append(queue[j]) #Adds nodes to be deleted as well
        for b in nodeData[queue[j]].toBranch:
            deleteBranches.append(b.label)
            queue.append(b.toNode)
        j += 1

    return deleteBranches, deleteNodes