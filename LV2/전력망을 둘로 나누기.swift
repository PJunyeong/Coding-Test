//
//  전력망을 둘로 나누기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/30.
//

import Foundation

func solution(_ n:Int, _ wires:[[Int]]) -> Int {
    var parents = Array(repeating: 0, count: n+1)
    func resetNodes() {
        for idx in 0..<n+1 {
            parents[idx] = idx
        }
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
            if root1 > root2 {
                parents[root2] = root1
            } else {
                parents[root1] = root2
            }
            return true
        }
    }
    
    func getComponentsDiff() -> Int {
        var nodeDict = [Int:Int]()
        for idx in 1..<parents.count {
            let root = find(node: parents[idx])
            let count = nodeDict[root] ?? 0
            nodeDict[root] = count + 1
        }
        let values = Array(nodeDict.values)
        return abs(values[0] - values[1])
    }
    
    var answer = Int.max
    for cut in 0..<wires.count {
        resetNodes()
        for idx in 0..<wires.count {
            if idx == cut {
                continue
            }
            let wire = wires[idx]
            let (parent, child) = (wire[0], wire[1])
            union(node1: parent, node2: child)
        }
        answer = min(answer, getComponentsDiff())
    }
    return answer
}
