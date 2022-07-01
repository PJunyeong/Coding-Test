//
//  섬 연결하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/01.
//

import Foundation

func solution(_ n:Int, _ costs:[[Int]]) -> Int {
    
    var parents = [Int]()
    for i in 0..<n {
        parents.append(i)
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
        var costs = costs
        costs.sort(by: {$0[2] < $1[2]})
        
        var total = 0
        var edgeCnt = 0
        
        for data in costs {
            let node1 = data[0]
            let node2 = data[1]
            let cost = data[2]
            
            if union(node1: node1, node2: node2) {
                total += cost
                edgeCnt += 1
                if edgeCnt == n-1 {
                    return total
                }
            }
        }
        return -1
    }
    
    let total = Kruskal()
    return total
}
