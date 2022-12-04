# Time - O(N+E)
# Space - O(N+E)
# N - Number of Nodes
# E - Number of Edges

# Solution 1
def topologicalSort(jobs, deps):
    jobGraph = JobGraph(jobs, deps)
    return getOrederdJobs(jobGraph)


def getOrederdJobs(jobGraph):
    orderdJobs = []
    for node in jobGraph.graph.values():
        loopExists = depthFirstSearch(node, orderdJobs)
        if loopExists:
            return []
    return orderdJobs


def depthFirstSearch(node, orderdJobs):
    if node.isVisited:
        return False
    if node.isVisiting:
        return True
    node.setVisiting(True)
    for req in node.preReq:
        loopExists = depthFirstSearch(req, orderdJobs)
        if loopExists:
            return True
    node.setVisiting(False)
    node.setVisited(True)
    orderdJobs.append(node.value)
    return False


class JobGraph:
    def __init__(self, jobs, preRequisits):
        self.graph = {}
        for job in jobs:
            self.addNode(job)
        for preReq, job in preRequisits:
            self.addPrereq(job, preReq)

    def addNode(self, job):
        self.graph[job] = Node(job)

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

    def addPrereq(self, job, preReq):
        jobNode = self.getNode(job)
        prereqNode = self.getNode(preReq)
        jobNode.addPreReq(prereqNode)


class Node:
    def __init__(self, value):
        self.value = value
        self.preReq = []
        self.isVisiting = False
        self.isVisited = False

    def addPreReq(self, dep):
        self.preReq.append(dep)

    def setVisiting(self, bool):
        self.isVisiting = bool

    def setVisited(self, bool):
        self.isVisited = bool

# Solution 2 
class JobNode:
    def __init__(self, job):
        self.job = job
        self.deps = []
        self.numOfPrereqs = 0


class JobGraph:
    def __init__(self, jobs):
        self.nodes = []
        self.graph = {}
        for job in jobs:
            self.addNode(job)

    def addDep(self, job, dep):
        jobNode = self.getNode(job)
        depNode = self.getNode(dep)
        jobNode.dep.append(depNode)
        depNode.numOfPrereqs += 1

    def addNode(self, job):
        self.graph[job] = JobNode(job)
        self.nodes.append(self.graph[job])

    def getNode(self, job):
        if job not in self.graph:
            self.addNode(job)
        return self.graph[job]

#   O(v + e) time | O(v + e) space


def topologicalSort(jobs, deps):
    jobGraph = createJobGraph(jobs, deps)
    return getOrderedJobs(jobGraph)


def createJobGraph(jobs, deps):
    graph = JobGraph(jobs)
    for job, dep in deps:
        graph.addDep(job, dep)
    return graph


def getOrderedJobs(graph):
    orderedJobs = []
    nodesWithNoPrereqs = list(
        filter(lambda node: node.numOfPrereqs == 0, graph.nodes))
    while len(nodesWithNoPrereqs):
        node = nodesWithNoPrereqs.pop()
        orderedJobs.append(node.job)
        removeDeps(node, nodesWithNoPrereqs)
    graphHasEdges = any(node.numOfPrereqs for node in graph.nodes)
    return [] if graphHasEdges else orderedJobs


def removeDeps(node, nodesWithNoPrereqs):
    while len(node.deps):
        dep = node.deps.pop()
        dep.numOfPrereqs -= 1
        if dep.numOfPrereqs == 0:
            nodesWithNoPrereqs.append(dep)
