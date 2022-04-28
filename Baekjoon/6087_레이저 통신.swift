//
//  6087_레이저 통신.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/28.
//

import Foundation

let input = readLine()!.split(separator: " ").map({Int(String($0))!})
let (M, N) = (input[0], input[1])
var nodes = [[String]]()
var points = [(Int, Int)]()
for i in 0..<N{
    let row = Array(readLine()!.map({String($0)}))
    for j in 0..<M{
        if row[j] == "C"{
            points.append((i, j))
        }
    }
    nodes.append(row)
}

print(BFS())

func BFS()->Int{
    let dx = [1, -1, 0, 0]
    let dy = [0, 0, 1, -1]
    var visited = Array(repeating: Array(repeating: Int.max, count: M), count: N)
    let start = points[0]
    let end = points[1]
    visited[start.0][start.1] = 0
    var queue = [(Int, Int, Int, Int)]()
    var answer = Int.max
    for i in 0..<4{
        queue.append((start.0, start.1, i, 0))
    }
    var index = 0
    
    while queue.count > index{
        let curData = queue[index]
        let curRow = curData.0
        let curCol = curData.1
        let curDir = curData.2
        let curCnt = curData.3
        
        if curRow == end.0 && curCol == end.1{
            answer = min(answer, curCnt)
        }
        
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            var nextCnt = curCnt
            
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
                continue
            }
            
            if i != curDir{
                nextCnt += 1
            }
            
            if nodes[nextRow][nextCol] != "*" && visited[nextRow][nextCol] >= nextCnt{
                visited[nextRow][nextCol] = nextCnt
                queue.append((nextRow, nextCol, i, nextCnt))
            }
        }
        index += 1
    }
    return answer
}
