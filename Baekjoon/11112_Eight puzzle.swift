//
//  11112_Eight puzzle.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/23.
//

import Foundation

var answerNote:[String:Int] = [:]
let answer:[String] = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
let dx = [0, 0, 1, -1]
let dy = [1, -1, 0, 0]
func BFS()->Void{
    var queue = [([String], Int, Int)]()
    queue.append((answer, 0, 8))
    answerNote[answer.joined()] = 0
    var index = 0
    while queue.count > index{
        let curData = queue[index]
        let curState = curData.0
        let curCnt = curData.1
        let curPos = curData.2
        let curRow = curPos / 3
        let curCol = curPos % 3
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            if nextRow < 0 || nextCol < 0 || nextRow >= 3 || nextCol >= 3{
                continue
            }
            let nextPos = nextRow * 3 + nextCol
            var nextState = curState
            let tmp = curState[nextPos]
            nextState[nextPos] = "9"
            nextState[curPos] = tmp
            let nextStateString = nextState.joined()
            let nextCnt = answerNote[nextStateString, default: -1]
            if nextCnt == -1{
                answerNote[nextStateString] = curCnt + 1
                queue.append((nextState, curCnt+1, nextPos))
            }
        }
        index += 1
    }
}

let N = Int(readLine()!)!
BFS()
for _ in 0..<N{
    let _ = readLine()!
    var states = [String]()
    for _ in 0..<3{
        let row = readLine()!
        for letter in row{
            if String(letter) == "#"{
                states.append("9")
            } else {
                states.append(String(letter))
            }
        }
    }
    let curState = states.joined()
    let curCnt = answerNote[curState, default: -1]
    if curCnt == -1{
        print("impossible")
    } else{
        print(curCnt)
    }
}
