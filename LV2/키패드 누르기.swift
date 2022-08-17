//
//  키패드 누르기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/17.
//

import Foundation

func solution(_ numbers:[Int], _ hand:String) -> String {
    var keypads = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -2]]
    var keypadsDict = [Int:(Int, Int)]()
    for i in 0..<4 {
        for j in 0..<3 {
            let keypad = keypads[i][j]
            keypadsDict[keypad] = (i, j)
        }
    }
    
    var curLeft = (3, 0)
    var curRight = (3, 2)
    
    var moves = ""
    
    for number in numbers {
        if number == 1 || number == 4 || number == 7 {
            moves.append("L")
            curLeft = keypadsDict[number]!
        } else if number == 3 || number == 6 || number == 9 {
            moves.append("R")
            curRight = keypadsDict[number]!
        } else {
            let numberPos = keypadsDict[number]!
            let leftDist = abs(numberPos.0 - curLeft.0) + abs(numberPos.1 - curLeft.1)
            let rightDist = abs(numberPos.0 - curRight.0) + abs(numberPos.1 - curRight.1)
            if leftDist < rightDist {
                moves.append("L")
                curLeft = numberPos
            } else if leftDist > rightDist {
                moves.append("R")
                curRight = numberPos
            } else {
                if hand == "right" {
                    moves.append("R")
                    curRight = numberPos
                } else {
                    moves.append("L")
                    curLeft = numberPos
                }
            }
        }
    }
    
    return moves
}
