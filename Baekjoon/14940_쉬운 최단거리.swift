//
//  14940_쉬운 최단거리.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/11.
//

import Foundation

let dx = [0, 0, 1, -1]
let dy = [1, -1, 0, 0]
let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var nodes = [[Int]]()
var result = Array(repeating: Array(repeating: Int.max, count: M), count: N)
var goal: (Int, Int) = (-1, -1)
for i in 0..<N{
    let row = readLine()!.split(separator: " ").map{Int(String($0))!}
    for j in 0..<M{
        if row[j] == 2{
            goal = (i, j)
        }
    }
    nodes.append(row)
}

BFS(goal:goal)

for i in 0..<N {
    for j in 0..<M {
        if result[i][j] == Int.max {
            if nodes[i][j] == 0 {
                print(0, terminator: " ")
            } else {
                print(-1, terminator: " ")
            }
        } else {
            print(result[i][j], terminator: " ")
        }
    }
    print()
}

func BFS(goal:(Int, Int)) -> Void {
    var queue = [(Int, Int, Int)]()
    queue.append((goal.0, goal.1, 0))
    result[goal.0][goal.1] = 0
    var index = 0
    
    while queue.count > index {
        let curData = queue[index]
        let curRow = curData.0
        let curCol = curData.1
        let curCnt = curData.2
        
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            let nextCnt = curCnt + 1
            
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M || nodes[nextRow][nextCol] != 1 {
                continue
            }
            
            if result[nextRow][nextCol] > nextCnt {
                result[nextRow][nextCol] = nextCnt
                queue.append((nextRow, nextCol, nextCnt))
            }
        }
        index += 1
    }
    return
}
