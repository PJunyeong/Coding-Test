//
//  1913_달팽이.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/05.
//

import Foundation

let N = Int(String(readLine()!))!
let target = Int(String(readLine()!))!
var nodes = Array(repeating: Array(repeating: 0, count: N), count: N)
// 남 동 북 서
let dx = [0, 1, 0, -1]
let dy = [1, 0, -1, 0]
var curDir = 0
var curNumber = N * N
var curRow = 0
var curCol = 0
var answer = (1, 1)
nodes[0][0] = curNumber
curNumber -= 1

while curNumber > 0 {
    let nextRow = curRow + dy[curDir]
    let nextCol = curCol + dx[curDir]
    
    if nextRow >= 0 && nextRow < N && nextCol >= 0 && nextCol < N && nodes[nextRow][nextCol] == 0 {
        nodes[nextRow][nextCol] = curNumber
        if curNumber == target {
            answer = (nextRow+1, nextCol+1)
        }
        curNumber -= 1
        curRow = nextRow
        curCol = nextCol
    } else {
        curDir = (curDir + 1) % 4
    }
}

for i in 0..<N {
    for j in 0..<N {
        print(nodes[i][j], terminator: " ")
    }
    print()
}
print(answer.0, terminator: " ")
print(answer.1)
