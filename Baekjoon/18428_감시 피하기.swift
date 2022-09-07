//
//  18428_감시 피하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/07.
//

import Foundation

let N = Int(String(readLine()!))!
var nodes = [[String]]()
var teachers = [(Int, Int)]()
var students = [(Int, Int)]()
var blanks = [(Int, Int)]()
let dx = [0, 0, 1, -1]
let dy = [1, -1, 0, 0]
for i in 0..<N {
    let row = Array(readLine()!.split(separator: " ")).map{String($0)}
    for j in 0..<N {
        if row[j] == "T" {
            teachers.append((i, j))
        } else if row[j] == "S" {
            students.append((i, j))
        } else {
            blanks.append((i, j))
        }
    }
    nodes.append(row)
}
var checked = Array(repeating: false, count: blanks.count)
var answer = false
depthFirstSearch(0, 0)
print(answer ? "YES" : "NO")

func depthFirstSearch(_ startIndex: Int, _ count: Int) {
    if count == 3 {
        if isHidable() && !answer {
            answer = true
        }
        return
    }
    
    for idx in startIndex..<blanks.count {
        if !checked[idx] {
            let pos = blanks[idx]
            let row = pos.0
            let col = pos.1
            checked[idx] = true
            nodes[row][col] = "O"
            depthFirstSearch(idx, count + 1)
            checked[idx] = false
            nodes[row][col] = "X"
        }
    }
}

func isHidable() -> Bool {
    for teacher in teachers {
        for dir in 0..<4 {
            var curRow = teacher.0
            var curCol = teacher.1
            while true {
                let nextRow = curRow + dy[dir]
                let nextCol = curCol + dx[dir]
                if nextRow < 0 || nextRow >= N || nextCol < 0 || nextCol >= N {
                    break
                } else {
                    if nodes[nextRow][nextCol] == "O" {
                        break
                    } else if nodes[nextRow][nextCol] == "S" {
                        return false
                    } else {
                        curRow = nextRow
                        curCol = nextCol
                    }
                }
            }
        }
    }
    return true
}



