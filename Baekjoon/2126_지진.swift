//
//  2126_지진.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/28.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M, F) = (input[0], input[1], input[2])
var edges = [(Int, Int, Int, Int)]()
for _ in 0..<M {
    let edge = readLine()!.split(separator: " ").map{Int(String($0))!}
    edges.append((edge[0], edge[1], edge[2], edge[3]))
}
var left = 0.0
var right = Double(F)

func find(node:Int) -> Int {
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

func Kruskal(mid:Double) -> Bool {
    func edgeSort(num1: (Int, Int, Int, Int), num2: (Int, Int, Int, Int)) -> Bool {
        return (Double(num1.2) + Double(num1.3) * mid) < (Double(num2.2) + Double(num2.3) * mid)
    }
    edges.sort(by: edgeSort)
    var total = 0.0
    var edgeCnt = 0
    for edge in edges {
        let node1 = edge.0
        let node2 = edge.1
        let cost = edge.2
        let time = edge.3
        if union(node1: node1, node2: node2) == true {
            total += (Double(cost) + Double(time) * mid)
            edgeCnt += 1
            if edgeCnt == N-1 {
                break
            }
        }
    }
    if total <= Double(F) {
        return true
    } else {
        return false
    }
}

var parents = Array(repeating: 0, count: N+1)
var mid = 0.0
for _ in 0..<100 {
    for i in 0..<N+1 {
        parents[i] = i
    }
    
    mid = (left + right) / 2
    if Kruskal(mid:mid) == true {
        left = mid
    } else {
        right = mid
    }
}

if mid < 0 {
    print("0.0000")
} else {
    let midString = String(format: "%.4f", mid)
    print(midString)
}
