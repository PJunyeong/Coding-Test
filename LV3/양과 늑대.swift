//
//  양과 늑대.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/12.
//

import Foundation

func solution(_ info:[Int], _ edges:[[Int]]) -> Int {
    var total = 0
    var visited = Array(repeating: false, count: info.count)
    visited[0] = true

    DFS(1, 0)
    
    func DFS(_ curSheep: Int, _ curWolf: Int) {
        if curSheep <= curWolf {
            return
        } else {
            total = max(total, curSheep)
        }
        
        for edge in edges {
            let parent = edge[0]
            let child = edge[1]
            let nextState = info[child] == 0 ? (1, 0) : (0, 1)
            if visited[parent] && !visited[child] {
                visited[child] = true
                DFS(curSheep + nextState.0, curWolf + nextState.1)
                visited[child] = false
            }
        }
    }
    return total
}
