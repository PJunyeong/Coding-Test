//
//  가장 큰 정사각형 찾기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/13.
//

import Foundation

func solution(_ board:[[Int]]) -> Int {
    let rowCount = board.count
    let colCount = board[0].count
    var dp = Array(repeating: Array(repeating: 0, count: colCount + 1), count: rowCount + 1)
    var answer = 0
    for row in 1..<rowCount+1 {
        for col in 1..<colCount+1 {
            if board[row-1][col-1] == 1 {
                dp[row][col] = min(dp[row-1][col], dp[row][col-1], dp[row-1][col-1]) + 1
                answer = max(answer, dp[row][col])
            }
        }
    }
    return answer * answer
}
