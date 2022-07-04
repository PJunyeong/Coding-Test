//
//  7044_Bad Cowtractors.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/04.
//

import Foundation

let INF = Int.max
let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])

var parents = [Int]()
for i in 0..<(N+1) {
    parents.append(i)
}

var pq = [(Int, Int, Int)]()

for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (node1, node2, cost) = (input[0], input[1], input[2])
    pq.append((node1, node2, cost))
}

pq.sort(by: {$0.2 > $1.2})

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
            if edgeCnt == N-1 {
                return total
            }
        }
    }
    return -1
}

let answer = Kruskal()
print(answer)
