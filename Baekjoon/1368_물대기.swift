//
//  1368_물대기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/24.
//

import Foundation

let N = Int(readLine()!)!
var pq = [(Int, Int, Int)]()
for node in 0..<N {
    let cost = Int(readLine()!)!
    pq.append((cost, N, node))
}
// 0~N-1가 기본, N번 노드를 처음 시작하는 노드로 설정한다.

for i in 0..<N {
    let line = readLine()!.split(separator: " ").map{Int(String($0))!}
    for j in 0..<N {
        if i == j {
            continue
        } else {
            pq.append((line[j], i, j))
        }
    }
}

pq.sort{$0.0 < $1.0}

var parents = [Int]()
for i in 0..<N+1 {
    parents.append(i)
}

let answer = Kruskal()
print(answer)

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

func Kruskal()-> Int {
    var total = 0
    var edgeCnt = 0
    
    for curData in pq {
        let curCost = curData.0
        let curNode1 = curData.1
        let curNode2 = curData.2
        
        if union(node1: curNode1, node2: curNode2) == true {
            total += curCost
            edgeCnt += 1
            
            if edgeCnt == N {
                // N+1 개의 노드를 연결하는 MST 구성 간선 개수는 N개.
                return total
            }
        }
    }
    return -1
}
