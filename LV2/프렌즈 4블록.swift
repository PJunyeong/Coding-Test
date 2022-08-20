//
//  프렌즈 4블록.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/21.
//
import Foundation

struct Position: Hashable {
    let row: Int
    let col: Int
}

func solution(_ m:Int, _ n:Int, _ board:[String]) -> Int {
    var nodes = makeNodes(board)
    
    func downBoxes() {
        var tmpRow = [String]()
        var tmpIndex = 0
        for i in 0..<n {
            tmpRow = []
            tmpIndex = 0
            for j in stride(from: m-1, to: -1, by: -1) {
                if nodes[j][i] != "" {
                    tmpRow.append(nodes[j][i])
                }
            }
            tmpRow += Array(repeating: "", count: m - tmpRow.count)
            for j in stride(from: m-1, to: -1, by: -1) {
                nodes[j][i] = tmpRow[tmpIndex]
                tmpIndex += 1
            }
        }
    }
    
    func matchBoxes() -> Int {
        var blockPositions = Set<Position>()
        for i in 0..<m-1 {
            for j in 0..<n-1 {
                let first = nodes[i][j]
                let second = nodes[i][j+1]
                let third = nodes[i+1][j]
                let fourth = nodes[i+1][j+1]
                if first == "" || second == "" || third == "" || fourth == "" {
                    continue
                }
                if first == second && second == third && third == fourth {
                    blockPositions.insert(Position(row: i, col: j))
                    blockPositions.insert(Position(row: i, col: j + 1))
                    blockPositions.insert(Position(row: i + 1, col: j))
                    blockPositions.insert(Position(row: i + 1, col: j + 1))
                }
            }
        }
        for position in blockPositions {
            let row = position.row
            let col = position.col
            nodes[row][col] = ""
        }
        
        return blockPositions.count
    }
    
    var total = 0
    
    while true {
        let blockCount = matchBoxes()
        if blockCount == 0 {
            break
        } else {
            total += blockCount
        }
        downBoxes()
    }
    print(total)
    return total
}

func makeNodes(_ board: [String]) -> [[String]] {
    var nodes = [[String]]()
    for row in board {
        let row = Array(row).map{String($0)}
        nodes.append(row)
    }
    return nodes
}
