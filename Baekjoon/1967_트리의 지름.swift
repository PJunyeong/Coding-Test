//
//  1967_트리의 지름.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/14.
//

import Foundation

let N = Int(String(readLine()!))!
var nodes = Array(repeating: [(Int, Int)](), count: N+1)

for _ in 0..<(N-1) {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (parent, child, cost) = (input[0], input[1], input[2])
    
    nodes[parent].append((child, cost))
    nodes[child].append((parent, cost))
}

let nodeInfo1 = BFS(start: 1)
let node1 = nodeInfo1.0
let nodeInfo2 = BFS(start: node1)
let cost = nodeInfo2.1

print(cost)

func BFS(start: Int) -> (Int, Int) {
    var queue = [(Int, Int)]()
    queue.append((start, 0))
    var visited = Array(repeating: false, count: N+1)
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
        
        for nextData in nodes[curNode] {
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
