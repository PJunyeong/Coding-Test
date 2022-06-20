//
//  1167_트리의 지름.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/20.
//

import Foundation

let N = Int(String(readLine()!))!
var nodes = Array(repeating: [(Int, Int)](), count: N+1)

for _ in 0..<N {
    let edges = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
    let tail = edges[0]
    for idx in stride(from: 1, to: edges.count - 2, by: 2) {
        nodes[tail].append((edges[idx], edges[idx + 1]))
    }
    // 연결 그래프 생성
}

func BFS(start: Int) -> (Int, Int) {
    var visited = Array(repeating: false, count: N+1)
    var queue = [(Int, Int)]()
    queue.append((start, 0))
    visited[start] = true
    var maxCost = 0
    var maxNode = start
    var index = 0
    
    while queue.count > index {
        let curData = queue[index]
        let curNode = curData.0
        let curCost = curData.1
        
        if maxCost < curCost {
            maxCost = curCost
            maxNode = curNode
            // start 시작, 연결 비용 가장 큰 노드 및 비용 리턴
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
    return (maxNode, maxCost)
}

let (node1, _) = BFS(start: 1)
// 루트 노드 -> 가장 비용이 큰 노드 리턴
let (_, cost) = BFS(start: node1)
// node1 -> 가장 거리가 먼 노드까지 걸리는 비용 cost 리턴
print(cost)
// 트리의 지름
