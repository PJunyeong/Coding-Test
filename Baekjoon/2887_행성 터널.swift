//
//  2887_행성 터널.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/21.
//

import Foundation

let N = Int(readLine()!)!
var nodes = [(Int, Int, Int, Int)]()
for idx in 0..<N{
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (x, y, z) = (input[0], input[1], input[2])
    nodes.append((x, y, z, idx))
}
var parents:[Int] = []
for i in 0..<(N){
    parents.append(i)
}
var pq = [(Int, Int, Int)]()
nodes.sort(by:{$0.0 < $1.0})
for i in 0..<N-1{
    let node1 = nodes[i]
    let node2 = nodes[i+1]
    pq.append((node2.0-node1.0, node1.3, node2.3))
}
nodes.sort(by:{$0.1 < $1.1})
for i in 0..<N-1{
    let node1 = nodes[i]
    let node2 = nodes[i+1]
    pq.append((node2.1-node1.1, node1.3, node2.3))
}
nodes.sort(by:{$0.2 < $1.2})
for i in 0..<N-1{
    let node1 = nodes[i]
    let node2 = nodes[i+1]
    pq.append((node2.2-node1.2, node1.3, node2.3))
}
pq.sort(by:<)
let MST = Kruskal()
print(MST)

func find(node:Int)->Int{
    if parents[node] == node{
        return node
    } else {
        parents[node] = find(node:parents[node])
        return parents[node]
    }
}

func union(node1: Int, node2: Int) -> Bool{
    let root1 = find(node:node1)
    let root2 = find(node:node2)
    if root1 == root2{
        return false
    } else {
        parents[root2] = root1
        return true
    }
}

func Kruskal() -> Int{
    var total = 0
    var edgeCnt = 0
    for curData in pq{
        let cost = curData.0
        let node1 = curData.1
        let node2 = curData.2
        
        if union(node1: node1, node2: node2) == true{
            total += cost
            edgeCnt += 1
            if edgeCnt == N-1{
                return total
            }
        }
    }
    return -1
}
