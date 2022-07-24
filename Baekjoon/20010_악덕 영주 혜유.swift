//
//  20010_악덕 영주 혜유.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/24.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, K) = (input[0], input[1])
var pq = [(Int, Int, Int)]()
var parents = [Int]()
var edges = Array(repeating: [(Int, Int)](), count: N)
for i in 0..<N {
    parents.append(i)
}
for _ in 0..<K {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (a, b, c) = (input[0], input[1], input[2])
    pq.append((a, b, c))
}
pq.sort(by: {$0.2 < $1.2})

func find(node: Int) -> Int {
    if parents[node] == node {
        return node
    } else {
        parents[node] = find(node: parents[node])
        return parents[node]
    }
}

func union(node1: Int, node2: Int) -> Bool {
    let root1 = find(node: node1)
    let root2 = find(node: node2)
    if root1 == root2 {
        return false
    } else {
        parents[root2] = root1
        return true
    }
}

func Kruskal() -> Int {
    var total = 0
    var edgeCnt = 0
    for edge in pq {
        let node1 = edge.0
        let node2 = edge.1
        let cost = edge.2
        
        if union(node1: node1, node2: node2) {
            total += cost
            edgeCnt += 1
            edges[node1].append((node2, cost))
            edges[node2].append((node1, cost))
            if edgeCnt == N-1 {
                return total
            }
        }
    }
    return -1
}

let MST = Kruskal()
print(MST)

let nodeInfo1 = BFS(start: 0)
let node1 = nodeInfo1.0
let nodeInfo2 = BFS(start: node1)
let maxCost = nodeInfo2.1
print(maxCost)


func BFS(start: Int) -> (Int, Int) {
    var queue = [(Int, Int)]()
    queue.append((start, 0))
    var visited = Array(repeating: false, count: N)
    visited[start] = true
    var localMaxCost = 0
    var localMaxNode = start
    var index = 0
    
    while queue.count > index {
        let curData = queue[index]
        let curNode = curData.0
        let curCost = curData.1
        
        if localMaxCost < curCost {
            localMaxCost = curCost
            localMaxNode = curNode
        }
        
        for nextData in edges[curNode] {
            let nextNode = nextData.0
            let nextCost = nextData.1
            
            if !visited[nextNode] {
                visited[nextNode] = true
                queue.append((nextNode, curCost + nextCost))
            }
        }
        index += 1
    }
    return (localMaxNode, localMaxCost)
}
