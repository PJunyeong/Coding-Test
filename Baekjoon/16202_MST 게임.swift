//
//  16202_MST 게임.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/22.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M, K) = (input[0], input[1], input[2])
var edges = [(Int, Int, Int)]()
// edges: (edgeIndex, node1, node2)

for i in 1..<M+1 {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (node1, node2) = (input[0], input[1])
    edges.append((i, node1, node2))
}

var parents = Array(repeating: 0, count: N+1)
var answers = Array(repeating: 0, count: K)

func find(node: Int) -> Int {
    if parents[node] == node {
        return node
    } else {
        parents[node] = find(node: parents[node])
        return parents[node]
    }
}

func union(node1:Int, node2:Int) -> Bool {
    let root1 = find(node: node1)
    let root2 = find(node: node2)
    
    if root1 == root2 {
        return false
    } else {
        parents[root2] = root1
        return true
    }
}

for i in 0..<K {
    for i in 0..<N+1{
        parents[i] = i
    }
    
    var total = 0
    var edgeCnt = 0
    
    for edge in edges[i...edges.count-1] {
        let cost = edge.0
        let node1 = edge.1
        let node2 = edge.2
        if union(node1: node1, node2: node2) == true {
            total += cost
            edgeCnt += 1
            if edgeCnt == N-1 {
                break
            }
        }
    }
    if edgeCnt == N-1 {
        answers[i] = total
    } else {
        break
    }
}

for item in answers {
    print(item, terminator: " ")
}
