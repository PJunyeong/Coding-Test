//
//  경주로 건설.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/12.
//

import Foundation

func solution(_ board:[[Int]]) -> Int {
    let INF = Int.max
    let N = board.count
    var dp = Array(repeating: Array(repeating: Array(repeating: INF, count: 4), count: N), count: N)
    var queue = [(Int, Int, Int, Int)]()
    // curRow, curCol, curCost, curDir
    let dx = [0, 0, 1, -1]
    let dy = [1, -1, 0, 0]
    var index = 0
    for idx in 0..<4 {
        queue.append((0, 0, 0, idx))
        dp[0][0][idx] = 0
    }
    
    while queue.count > index {
        let curData = queue[index]
        let curRow = curData.0
        let curCol = curData.1
        let curCost = curData.2
        let curDir = curData.3
        
        for idx in 0..<4 {
            let nextRow = curRow + dy[idx]
            let nextCol = curCol + dx[idx]
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= N || board[nextRow][nextCol] == 1 {
                continue
            }
            
            let nextCost = idx == curDir ? curCost + 100 : curCost + 600
            if dp[nextRow][nextCol][idx] > nextCost {
                dp[nextRow][nextCol][idx] = nextCost
                queue.append((nextRow, nextCol, nextCost, idx))
            }
        }
        
        index += 1
    }
    let answer = dp[N-1][N-1].min()!
    return answer
}
