//
//  방문 길이.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/10.
//

import Foundation

struct Position: Hashable {
    var row: Int
    var col: Int
}

struct Positions: Hashable {
    let position1: Position
    let position2: Position
}

func solution(_ dirs:String) -> Int {
    var positionSet = Set<Positions>()
    var curPos = Position(row: 0, col: 0)
    
    for dir in dirs {
        var nextRow = curPos.row
        var nextCol = curPos.col
        switch dir {
            case "U":
                nextRow += 1
            case "D":
                nextRow -= 1
            case "R":
                nextCol += 1
            case "L":
                nextCol -= 1
            default:
                continue
        }
        if nextRow < -5 || nextRow > 5 || nextCol < -5 || nextCol > 5 {
            continue
        } else {
            let nextPos = Position(row: nextRow, col: nextCol)
            let route1 = Positions(position1: curPos, position2: nextPos)
            let route2 = Positions(position1: nextPos, position2: curPos)
            positionSet.insert(route1)
            positionSet.insert(route2)
            curPos = nextPos
        }
    }
        
    return positionSet.count / 2
}
