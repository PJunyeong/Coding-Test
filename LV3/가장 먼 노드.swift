//
//  가장 먼 노드.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/11.
//

import Foundation

func solution(_ n:Int, _ edge:[[Int]]) -> Int {
    var nodes = Array(repeating: [Int](), count:n+1)
    for data in edge {
        let node1 = data[0]
        let node2 = data[1]
        nodes[node1].append(node2)
        nodes[node2].append(node1)
    }
    let answer = BFS(start: 1, nodes: nodes)
    return answer
}

func BFS(start: Int, nodes: [[Int]]) -> Int {
    var queue = [(Int, Int)]()
    var visited = Array(repeating: false, count: nodes.count + 1)
    queue.append((start, 0))
    visited[start] = true
    var index = 0
    var leafDict = [Int:Int]()
    while queue.count > index {
        let curData = queue[index]
        let curNode = curData.0
        let curCost = curData.1
        
        var isLeaf = true
        for nextNode in nodes[curNode] {
            if !visited[nextNode] {
                isLeaf = false
                visited[nextNode] = true
                queue.append((nextNode, curCost + 1))
            }
        }
        if isLeaf {
            let leafValue = leafDict[curCost] ?? 0
            leafDict[curCost] = leafValue + 1
        }
        index += 1
    }
    let farthest = leafDict.keys.max() ?? 0
    return leafDict[farthest] ?? 0
}
