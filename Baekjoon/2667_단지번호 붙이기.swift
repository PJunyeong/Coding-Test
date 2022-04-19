//
//  2667_단지번호 붙이기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/19.
//

import Foundation
let N:Int = Int(readLine()!)!
let dx:[Int] = [1, -1, 0, 0]
let dy:[Int] = [0, 0, 1, -1]
var nodes: [[Int]] = Array(repeating: [], count: N)
for i in 0..<N{
    let line = Array(readLine()!).map{Int(String($0))!}
    nodes[i] = line
//  인접 행렬 구현
}
var answers:[Int] = []
var answer = 0
for i in 0..<N{
    for j in 0..<N{
        if nodes[i][j] == 1{
            answer = BFS(startRow:i, startCol:j)
            answers.append(answer)
        }
    }
}

answers.sort(by:<)
print(answers.count)
for answer in answers{
    print(answer)
}

func BFS(startRow:Int, startCol:Int)->Int {
    var queue: [[Int]] = [[startRow, startCol]]
    nodes[startRow][startCol] = 0
    var answer = 0
    while queue.isEmpty == false {
        let curNode = queue.removeFirst()
        let (curRow, curCol) = (curNode[0], curNode[1])
        answer += 1
        for i in 0..<4{
            let x = dx[i]
            let y = dy[i]
            
            let nextRow = curRow + y
            let nextCol = curCol + x
            
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= N{
                continue
            }
            
            if nodes[nextRow][nextCol] == 1{
                nodes[nextRow][nextCol] = 0
                queue.append([nextRow, nextCol])
//              1 -> 0으로 방문 확인 체크
            }
        }
    }
    return answer
}

