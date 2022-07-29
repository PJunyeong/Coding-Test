//
//  14466_소가 길을 건너간 이유 6.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/29.
//

import Foundation


struct Position: Hashable {
    let row: Int
    let col: Int
}

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]
let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, K, R) = (input[0], input[1], input[2])
var nodes = Array(repeating: Array(repeating: 0, count: N), count: N)
var cows = [(Int, Int)]()

var roadDict = [Position: [Position]]()
for _ in 0..<R {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (row1, col1, row2, col2) = (input[0]-1, input[1]-1, input[2]-1, input[3]-1)
    let firstPos = Position(row: row1, col: col1)
    let secondPos = Position(row: row2, col: col2)
    
    var firstPosRoads = roadDict[firstPos] ?? []
    firstPosRoads.append(secondPos)
    roadDict[firstPos] = firstPosRoads
    var secondPosRoads = roadDict[secondPos] ?? []
    secondPosRoads.append(firstPos)
    roadDict[secondPos] = secondPosRoads
    // 특정 노드 <-> 특정 노드 도로 기록
}

for _ in 0..<K {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (row, col) = (input[0]-1, input[1]-1)
    nodes[row][col] = 1
    cows.append((row, col))
    // 소 위치 1로 마킹
}

func BFS(startRow: Int, startCol: Int) -> Int {
    var queue = [(Int, Int)]()
    var index = 0
    var visited = Array(repeating: Array(repeating: false, count: N), count: N)
    visited[startRow][startCol] = true
    queue.append((startRow, startCol))
    var visitedCows = [(Int, Int)]()
    
    while queue.count > index {
        let curData = queue[index]
        let curRow = curData.0
        let curCol = curData.1
        
        let possibleRoads = roadDict[Position(row: curRow, col: curCol)] ?? []
        
        for idx in 0..<4 {
            let nextRow = curRow + dy[idx]
            let nextCol = curCol + dx[idx]
            
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= N {
                continue
            }
            
            if possibleRoads.contains(Position(row: nextRow, col: nextCol)) {
                continue
            }
            
            if !visited[nextRow][nextCol] {
                visited[nextRow][nextCol] = true
                if nodes[nextRow][nextCol] == 1 {
                    visitedCows.append((nextRow, nextCol))
                }
                queue.append((nextRow, nextCol))
            }
        }
        index += 1
    }
    return visitedCows.count
}

var cowCnt = 0
for cow in cows {
    let answer = BFS(startRow: cow.0, startCol: cow.1)
    cowCnt += answer
    // 모든 소마다 BFS -> 길을 사용하지 않고 만날 수 있는 다른 소 리턴
}

cowCnt = cowCnt / 2
print(K * (K-1) / 2 - cowCnt)
// 모든 튜플 쌍 - 길을 사용하지 않고 만날 수 있는 소의 쌍 = 길을 사용해야 만날 수 있는 소의 쌍
