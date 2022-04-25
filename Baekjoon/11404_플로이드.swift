//
//  11404_플로이드.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/26.
//

import Foundation

let N = Int(readLine()!)!
let M = Int(readLine()!)!
let INF = Int.max
var nodes = Array(repeating: Array(repeating: INF, count: N+1), count: N+1)
for i in 1..<N+1{
    nodes[i][i] = 0
}
for _ in 0..<M{
    let input = readLine()!.split(separator: " ").map({Int(String($0))!})
    let (node1, node2, cost) = (input[0], input[1], input[2])
    if nodes[node1][node2] > cost{
        nodes[node1][node2] = cost
    }
}

for k in 1..<N+1{
    for i in 1..<N+1{
        for j in 1..<N+1{
            if nodes[i][k] == INF || nodes[k][j] == INF{
                continue
            }
            if nodes[i][j] > nodes[i][k] + nodes[k][j]{
                nodes[i][j] = nodes[i][k] + nodes[k][j]
            }
        }
    }
}

for i in 1..<N+1{
    for j in 1..<N+1{
        if nodes[i][j] == INF{
            nodes[i][j] = 0
        }
    }
}

for i in 1..<N+1{
    for j in 1..<N+1{
        print(nodes[i][j], terminator: " ")
    }
    print()
}
