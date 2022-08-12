//
//  합승 택시 요금.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/12.
//

import Foundation

func solution(_ n:Int, _ s:Int, _ a:Int, _ b:Int, _ fares:[[Int]]) -> Int {
    let INF = Int.max
    var nodes = Array(repeating: Array(repeating: INF, count: n+1), count: n+1)
    for i in 0..<n+1 {
        nodes[i][i] = 0
    }
    for fare in fares {
        let (c, d, f) = (fare[0], fare[1], fare[2])
        nodes[c][d] = f
        nodes[d][c] = f
    }
    for k in 1..<n+1 {
        for i in 1..<n+1 {
            for j in 1..<n+1 {
                if nodes[i][k] == INF || nodes[k][j] == INF {
                    continue
                }
                
                if nodes[i][j] > nodes[i][k] + nodes[k][j] {
                    nodes[i][j] = nodes[i][k] + nodes[k][j]
                }
            }
        }
    }
    var total = INF
    
    for i in 1..<n+1 {
        if nodes[s][i] == INF || nodes[i][a] == INF || nodes[i][b] == INF {
            continue
        }
        let route = nodes[s][i] + nodes[i][a] + nodes[i][b]
        total = min(total, route)
    }
    return total
}

