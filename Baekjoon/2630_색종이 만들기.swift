//
//  2630_색종이 만들기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/25.
//

import Foundation

let N = Int(String(readLine()!))!
var nodes = [[Int]]()
for _ in 0..<N {
    let row = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
    nodes.append(row)
}
var white = 0
var blue = 0


func check(startRow: Int, endRow: Int, startCol: Int, endCol: Int) -> Bool {
    let firstBox = nodes[startRow][startCol]
    for row in startRow..<endRow {
        for col in startCol..<endCol {
            if firstBox != nodes[row][col] {
                return false
            }
        }
    }
    if firstBox == 0 {
        white += 1
    } else {
        blue += 1
    }
    return true
}

func DFS(length: Int, startRow: Int, endRow: Int, startCol: Int, endCol: Int) {
    if length == 0 {
        return
    }
    if !check(startRow: startRow, endRow: endRow, startCol: startCol, endCol: endCol) {
        let nextLength = length / 2
        DFS(length: nextLength, startRow: startRow, endRow: startRow + nextLength, startCol: startCol, endCol: startCol + nextLength)
        DFS(length: nextLength, startRow: startRow, endRow: startRow + nextLength, startCol: startCol + nextLength, endCol: endCol)
        DFS(length: nextLength, startRow: startRow + nextLength, endRow: endRow, startCol: startCol, endCol: startCol + nextLength)
        DFS(length: nextLength, startRow: startRow + nextLength, endRow: endRow, startCol: startCol + nextLength, endCol: endCol)
    }
}

DFS(length: N, startRow: 0, endRow: N, startCol: 0, endCol: N)
print(white)
print(blue)
