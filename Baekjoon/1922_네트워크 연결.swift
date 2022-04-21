//
//  1922_네트워크 연결.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/21.
//

import Foundation

let N = Int(readLine()!)!
let M = Int(readLine()!)!
var pq = [(Int, Int, Int)]()
for _ in 0..<M{
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (node1, node2, cost) = (input[0], input[1], input[2])
    pq.append((cost, node1, node2))
}
pq.sort(by:{$0.0 < $1.0})
var parents:[Int] = []
for i in 0..<(N+1){
    parents.append(i)
}

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
