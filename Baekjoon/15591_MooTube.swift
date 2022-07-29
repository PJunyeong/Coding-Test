//
//  15591_MooTube.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/29.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, Q) = (input[0], input[1])
var nodes = Array(repeating: [(Int, Int)](), count: N+1)

for _ in 0..<N-1 {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (a, b, c) = (input[0], input[1], input[2])
    nodes[a].append((b, c))
    nodes[b].append((a, c))
}

func BFS(K: Int, node: Int) -> Int {
    let INF = Int.max
    var visited = Array(repeating: false, count: N+1)
    var numbers = Array(repeating: INF, count: N+1)
    visited[node] = true
    var queue = [(Int, Int)]()
    queue.append((node, INF))
    var index = 0
    
    while queue.count > index {
        let curData = queue[index]
        let curNode = curData.0
        let curCost = curData.1
        
        numbers[curNode] = min(numbers[curNode], curCost)
        
        for nextData in nodes[curNode] {
            let nextNode = nextData.0
            let nextCost = nextData.1
            
            if !visited[nextNode] {
                visited[nextNode] = true
                let minCost = min(curCost, nextCost)
                queue.append((nextNode, minCost))
            }
        }
        index += 1
    }
    return numbers.filter{$0 >= K}.count - 2
}

for _ in 0..<Q {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (K, node) = (input[0], input[1])
    let answer = BFS(K: K, node: node)
    print(answer)
}
