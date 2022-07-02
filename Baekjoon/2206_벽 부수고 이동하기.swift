//
//  2206_벽 부수고 이동하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/02.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var nodes = [[Int]]()
let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]

for _ in 0..<N {
    let line = Array(readLine()!.map{Int(String($0))!})
    nodes.append(line)
}

func BFS() -> Int {
    var queue = [(Int, Int, Int)]()
    queue.append((0, 0, 0))
    var visited = Array(repeating: Array(repeating: [0, 0], count: M), count: N)
    visited[0][0][0] = 1
    var index = 0
    
    while queue.count > index {
        let curData = queue[index]
        let curRow = curData.0
        let curCol = curData.1
        let curWall = curData.2
        
        if curRow == (N-1) && curCol == (M-1) {
            return visited[curRow][curCol][curWall]
        }
        
        for i in 0..<4 {
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M {
                continue
            }
            
            if visited[nextRow][nextCol][curWall] == 0 && nodes[nextRow][nextCol] == 0 {
                visited[nextRow][nextCol][curWall] = visited[curRow][curCol][curWall] + 1
                queue.append((nextRow, nextCol, curWall))
            }
            
            if nodes[nextRow][nextCol] == 1 && curWall == 0 {
                visited[nextRow][nextCol][1] = visited[curRow][curCol][0] + 1
                queue.append((nextRow, nextCol, 1))
            }
            
        }
        index += 1
    }
    
    return -1
}

let answer = BFS()
print(answer)
