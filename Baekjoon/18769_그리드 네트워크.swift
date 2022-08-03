//
//  18769_그리드 네트워크.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/03.
//

import Foundation

let T = Int(String(readLine()!))!
var parents = [Int]()
var pq = [(Int, Int, Int)]()
var R = 0
var C = 0
for _ in 0..<T {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    (R, C) = (input[0], input[1])
    pq = []
    for i in 0..<R {
        let input = readLine()!.split(separator: " ").map{Int(String($0))!}
        for j in 0..<C-1 {
            pq.append((input[j], i*C+j, i*C+j+1))
        }
    }
    for i in 0..<R-1 {
        let input = readLine()!.split(separator: " ").map{Int(String($0))!}
        for j in 0..<C {
            pq.append((input[j], i*C+j, (i+1)*C+j))
        }
    }
    pq.sort(by: {$0.0 < $1.0})
    parents = []
    for i in 0..<R*C {
        parents.append(i)
    }
    let MST = Kruskal()
    print(MST)
}

func find(node: Int) -> Int {
    if parents[node] == node {
        return node
    } else {
        parents[node] = find(node: parents[node])
        return parents[node]
    }
}

func union(node1: Int, node2: Int) -> Bool {
    let root1 = find(node:node1)
    let root2 = find(node:node2)
    
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
        let cost = edge.0
        let node1 = edge.1
        let node2 = edge.2
        
        if union(node1: node1, node2: node2) {
            total += cost
            edgeCnt += 1
            if edgeCnt == R*C-1 {
                return total
            }
        }
    }
    return -1
}
