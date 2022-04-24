//
//  1600_말이 되고픈 원숭이.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/24.
//

import Foundation

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]
let dx2 = [-2, -2, -1, -1, 1, 1, 2, 2]
let dy2 = [1, -1, 2, -2, 2, -2, 1, -1]

var K = Int(readLine()!)!
let input = readLine()!.split(separator: " ").map({Int(String($0))!})
let (M, N) = (input[0], input[1])
var nodes = [[Int]]()
for _ in 0..<N{
    let row = readLine()!.split(separator: " ").map({Int(String($0))!})
    nodes.append(row)
}

let answer = BFS()
print(answer)

func BFS() -> Int{
    var visited = Array(repeating: Array(repeating: Array(repeating: false, count: M), count: N), count: K+1)
    var queue = [(Int, Int, Int, Int)]()
    queue.append((0, 0, 0, K))
    visited[K][0][0] = true
    var index = 0
    while queue.count > index{
        let curData = queue[index]
        let curRow = curData.0
        let curCol = curData.1
        let curCnt = curData.2
        let curK = curData.3
        
        if curRow == N-1 && curCol == M-1{
            return curCnt
        }
        
        if curK > 0{
            for i in 0..<8{
                let nextRow = curRow + dy2[i]
                let nextCol = curCol + dx2[i]
                if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
                    continue
                }
                if nodes[nextRow][nextCol] == 0 && visited[curK-1][nextRow][nextCol] == false{
                    visited[curK-1][nextRow][nextCol] = true
                    queue.append((nextRow, nextCol, curCnt+1, curK-1))
                }
            }
        }
        
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
                continue
            }
            
            if nodes[nextRow][nextCol] == 0 && visited[curK][nextRow][nextCol] == false{
                visited[curK][nextRow][nextCol] = true
                queue.append((nextRow, nextCol, curCnt + 1, curK))
            }
        }
        index += 1
    }
    return -1
}

