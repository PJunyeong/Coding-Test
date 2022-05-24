//
//  1937_욕심쟁이 판다.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/25.
//

import Foundation

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]
let N = Int(readLine()!)!
var dp = Array(repeating: Array(repeating: -1, count: N), count: N)
var nodes = Array(repeating: [Int](), count: N)
for i in 0..<N {
    let row = readLine()!.split(separator: " ").map{Int(String($0))!}
    nodes[i] = row
}

func DFS(row:Int, col: Int) -> Int {
    if dp[row][col] != -1 {
        return dp[row][col]
    } else {
        dp[row][col] = 1
        for i in 0..<4{
            let nextRow = row + dy[i]
            let nextCol = col + dx[i]
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= N {
                continue
            }
            
            if nodes[nextRow][nextCol] > nodes[row][col] {
                dp[row][col] = max(dp[row][col], DFS(row: nextRow, col: nextCol) + 1)
            }
        }
        return dp[row][col]
    }
}

var answer = 0
for i in 0..<N {
    for j in 0..<N {
        answer = max(answer, DFS(row: i, col: j))
    }
}

print(answer)
