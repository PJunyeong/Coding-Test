//
//  1185_유럽여행.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/23.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var costs = [Int]()
costs.append(0)
var minCost = Int.max
for _ in 0..<N {
    let cost = Int(readLine()!)!
    minCost = min(minCost, cost)
    costs.append(cost)
}
// 최소 비용 minCost, 각 노드 비용 배열 costs

var pq = [(Int, Int, Int)]()
for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (node1, node2, cost) = (input[0], input[1], input[2])
    let totalCost = cost * 2 + costs[node1] + costs[node2]
    pq.append((totalCost, node1, node2))
    // 왕복 노선: 간선 * 2 + 노드1 비용 + 노드2 비용
}
pq.sort{$0.0 < $1.0}
// 왕복할 때 가장 비용이 작은 간선부터 MST

var parents = [Int]()
for i in 0..<N+1{
    parents.append(i)
}

func find(node: Int) -> Int {
    if parents[node] == node {
        return node
    } else {
        parents[node] = find(node:parents[node])
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

func Kruskal() -> Int {
    var total = 0
    var edgeCnt = 0
    
    for curData in pq {
        let curCost = curData.0
        let curNode1 = curData.1
        let curNode2 = curData.2
        
        if union(node1: curNode1, node2: curNode2) == true {
            total += curCost
            edgeCnt += 1
            if edgeCnt == N-1 {
                return total
            }
        }
    }
    return -1
}

let answer = minCost + Kruskal()
// 시작/마지막 국가는 노드 자체에서 가장 비용이 적은 minCost
print(answer)
