# https://school.programmers.co.kr/tryouts/72095/challenges

import sys
sys.setrecursionlimit(10**6)

def solution(nodeinfo):
    answer = []
    nodelist = list()
    for i in range(len(nodeinfo)):
        nodelist.append([i+1, nodeinfo[i][0], nodeinfo[i][1]])

    nodelist.sort(key=lambda node: node[2], reverse=True)
    headidx = nodelist[0][0]

    tree = [[-1, -1] for _ in range(len(nodelist)+1)] # left, right

    def add(beforeidx, nowidx):
        if nodeinfo[nowidx-1][0] > nodeinfo[beforeidx-1][0]: # right
            if tree[beforeidx][1] != -1:
                add(tree[beforeidx][1], nowidx)
                return
            tree[beforeidx][1] = nowidx
        else: # left
            if tree[beforeidx][0] != -1:
                add(tree[beforeidx][0], nowidx)
                return
            tree[beforeidx][0] = nowidx

    for i in range(1, len(nodelist)):
        add(headidx, nodelist[i][0])

    # preorder
    def preorder(idx):
        if idx < 1:
            return []
        value = [idx]
        left = preorder(tree[idx][0])
        for l in left:
            value.append(l)
        right = preorder(tree[idx][1])
        for r in right:
            value.append(r)
        return value

    # postorder
    def postorder(idx):
        if idx < 1:
            return []
        value = []
        left = postorder(tree[idx][0])
        for l in left:
            value.append(l)
        right = postorder(tree[idx][1])
        for r in right:
            value.append(r)
        value.append(idx)
        return value

    answer.append(preorder(headidx))
    answer.append(postorder(headidx))

    return answer