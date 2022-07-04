from collections import deque


def solution(n, start, end, roads, traps):
    roads_mat = [[0] * n for i in range(n)]
    for i in roads:
        if roads_mat[i[0] - 1][i[1] - 1] == 0:
            roads_mat[i[0] - 1][i[1] - 1] = i[2]
        elif roads_mat[i[0] - 1][i[1] - 1] > i[2]:
            roads_mat[i[0] - 1][i[1] - 1] = i[2]
    traps = tuple(sorted(map(lambda x: x - 1, traps)))
    trapstatusindex = [-1] * n
    trapindexcount = 0
    for i in range(n):
        if i in traps:
            trapstatusindex[i] = trapindexcount
            trapindexcount += 1
    nodequeue = deque()
    nodequeue.append((start - 1, tuple([False] * len(traps))))
    usednode = {nodequeue[0]: 0}
    endvalue = -1

    while len(nodequeue) > 0:
        curnode = nodequeue.popleft()
        curtime = usednode[curnode]
        iscuract = curnode[1][trapstatusindex[curnode[0]]] if trapstatusindex[curnode[0]] > -1 else False
        for i in range(n):
            isiact = curnode[1][trapstatusindex[i]] if trapstatusindex[i] > -1 else False
            if iscuract ^ isiact:
                road_to_d = roads_mat[i][curnode[0]]
            else:
                road_to_d = roads_mat[curnode[0]][i]
            if road_to_d <= 0:
                continue
            if -1 < endvalue < (curtime + road_to_d):
                continue
            newtrapsnapshot = list(curnode[1])
            if trapstatusindex[i] > -1:
                newtrapsnapshot[trapstatusindex[i]] = False if newtrapsnapshot[trapstatusindex[i]] else True
            newnode = (i, tuple(newtrapsnapshot))
            if newnode not in usednode or usednode[newnode] > curtime + road_to_d:
                if newnode[0] == (end - 1):
                    endvalue = curtime + road_to_d
                usednode[newnode] = curtime + road_to_d
                nodequeue.append(newnode)
    return endvalue