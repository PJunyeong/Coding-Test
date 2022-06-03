//
//  4650_Jungle Roads.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/03.
//

import Foundation

let alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
var letterNum = [String:Int]()

for data in alphabets.enumerated(){
    let letter = String(data.element)
    let idx = data.offset
    
    letterNum[letter] = idx
}

while true {
    let N = Int(readLine()!)!
    if N == 0 {
        break
    }
    
    var pq = [(Int, Int, Int)]()
    
    for _ in 0..<(N-1) {
        let edges = Array(readLine()!.split(separator: " ").map{String($0)})
        let node1 = letterNum[edges[0]]!
        for i in stride(from: 2, to: edges.count, by: 2) {
            let (node2, cost) = (letterNum[edges[i]]!, Int(edges[i+1])!)
            pq.append((cost, node1, node2))
        }
    }
    
    pq.sort(by: {$0.0 < $1.0})

    var parents = Array(repeating: 0, count: N+1)
    for i in 0..<N+1 {
        parents[i] = i
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
    
    func Kruskal() -> Int {
        var total = 0
        var edgeCnt = 0
        
        for data in pq {
            let cost = data.0
            let node1 = data.1
            let node2 = data.2
            
            if union(node1: node1, node2: node2) == true {
                total += cost
                edgeCnt += 1
                if edgeCnt == N-1 {
                    return total
                }
            }
        }
        return -1
    }
}

