//
//  11048_이동하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/01.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var nodes = [[Int]]()
let dx = [0, 1, 1]
let dy = [1, 0, 1]

for _ in 0..<N {
    let row = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
    nodes.append(row)
}
var dp = Array(repeating: Array(repeating: 0, count: M), count: N)
dp[0][0] = nodes[0][0]

func BFS() {
    var queue = [(Int, Int)]()
    var visited = Array(repeating: Array(repeating: false, count: M), count: N)
    visited[0][0] = true
    queue.append((0, 0))
    var index = 0
    
    while queue.count > index {
        let curData = queue[index]
        let curRow = curData.0
        let curCol = curData.1
        
        for i in 0..<3 {
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M {
                continue
            }
            
            if !visited[nextRow][nextCol] {
                visited[nextRow][nextCol] = true
                dp[nextRow][nextCol] = dp[curRow][curCol] + nodes[nextRow][nextCol]
                queue.append((nextRow, nextCol))
            } else if dp[nextRow][nextCol] < dp[curRow][curCol] + nodes[nextRow][nextCol] {
                dp[nextRow][nextCol] = dp[curRow][curCol] + nodes[nextRow][nextCol]
                queue.append((nextRow, nextCol))
            }
        }
        index += 1
    }
    
}

BFS()
print(dp[N-1][M-1])
