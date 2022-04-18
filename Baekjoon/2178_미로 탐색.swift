//
//  main.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/18.
//

import Foundation
let input:[Int] = readLine()!.split(separator: " ").map{Int($0)!}
let (N, M) = (input[0], input[1])
let dx:[Int] = [1, -1, 0, 0]
let dy:[Int] = [0, 0, 1, -1]
var nodes: [[Int]] = Array(repeating: [], count: N)
for i in 0..<N{
    let line = Array(readLine()!).map{Int(String($0))!}
    nodes[i] = line
//  인접 행렬 구현
}

let answer = BFS()
print(answer)

func BFS()->Int {
    var queue: [[Int]] = [[0, 0, 1]]
    nodes[0][0] = 0
    var answer: Int = 0
    while queue.isEmpty == false {
        let curNode = queue.removeFirst()
        let (curRow, curCol, curCost) = (curNode[0], curNode[1], curNode[2])
        
        if curRow == N-1 && curCol == M-1{
            answer = curCost
            break
//          도착지 방문 시 비용 리턴
        }
        
        for i in 0..<4{
            let x = dx[i]
            let y = dy[i]
            
            let nextRow = curRow + y
            let nextCol = curCol + x
            
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
                continue
            }
            
            if nodes[nextRow][nextCol] == 1{
                nodes[nextRow][nextCol] = 0
                queue.append([nextRow, nextCol, curCost+1])
//              1 -> 0으로 방문 확인 체크
            }
        }
    }
    return answer
}

