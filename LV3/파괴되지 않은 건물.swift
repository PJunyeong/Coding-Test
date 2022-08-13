//
//  파괴되지 않은 건물.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/13.
//

import Foundation

func solution(_ board:[[Int]], _ skill:[[Int]]) -> Int {
    let rowCnt = board.count + 1
    let colCnt = board[0].count + 1
    var nodes = Array(repeating: Array(repeating: 0, count: colCnt), count: rowCnt)
    for sk in skill {
        let (type, r1, c1, r2, c2, degree) = (sk[0], sk[1], sk[2], sk[3], sk[4], sk[5])
        let times = type == 1 ? -1 : 1
        nodes[r1][c1] += times * degree
        nodes[r2 + 1][c2 + 1] += times * degree
        nodes[r1][c2 + 1] += -1 * times * degree
        nodes[r2 + 1][c1] += -1 * times * degree
    }
    for r in 0..<rowCnt {
        for c in 0..<colCnt-1 {
            nodes[r][c+1] += nodes[r][c]
        }
    }
    for c in 0..<colCnt {
        for r in 0..<rowCnt-1 {
            nodes[r+1][c] += nodes[r][c]
        }
    }
    var total = 0
    for i in 0..<board.count {
        for j in 0..<board[0].count {
            if board[i][j] + nodes[i][j] > 0 {
                total += 1
            }
        }
    }
    
    return total
}
