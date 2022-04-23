//
//  2589_보물섬.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/23.
//

import Foundation

let input = readLine()!.split(separator: " ").map({Int(String($0))!})
let (N, M) = (input[0], input[1])
let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]
var answer = 0
var map = [[String]]()
for _ in 0..<N{
    let row = Array(readLine()!.map({String($0)}))
    map.append(row)
}
for i in 0..<N{
    for j in 0..<M{
        if map[i][j] == "L"{
            answer = max(answer, BFS(row:i, col:j))
        }
    }
}
print(answer)

func BFS(row:Int, col:Int) -> Int{
    var queue = [(Int, Int, Int)]()
    queue.append((row, col, 0))
    var map = map
    map[row][col] = "W"
    var index = 0
    var total = 0
    while queue.count > index{
        let curData = queue[index]
        let curRow = curData.0
        let curCol = curData.1
        let curCnt = curData.2
        total = max(total, curCnt)
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
                continue
            }

            if map[nextRow][nextCol] == "L"{
                map[nextRow][nextCol] = "W"
                queue.append((nextRow, nextCol, curCnt + 1))
            }
        }
        index += 1
    }
    return total
}
