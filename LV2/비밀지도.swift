//
//  비밀지도.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/16.
//

import Foundation

func solution(_ n:Int, _ arr1:[Int], _ arr2:[Int]) -> [String] {
    let arr1 = arr1.map{makeRow(n , $0)}
    let arr2 = arr2.map{makeRow(n, $0)}
    let maze = makeMaze(n, arr1, arr2)
    return maze
}

func makeRow(_ digit: Int, _ number: Int) -> String {
    var row = ""
    var number = number
    for pos in 1...digit {
        let curDigit = digit - pos
        let curNumber = Int(pow(2.0, Double(curDigit)))
        if number >= curNumber {
            number -= curNumber
            row += "#"
        } else {
            row += " "
        }
    }
    return row
}

func makeMaze(_ digit: Int, _ arr1: [String], _ arr2: [String]) -> [String] {
    var maze = Array(repeating: Array(repeating: " ", count: digit), count: digit)
    for i in 0..<digit {
        for j in 0..<digit {
            let arr1Idx = arr1[i].index(arr1[i].startIndex, offsetBy: j)
            let arr1Letter = arr1[i][arr1Idx]
            let arr2Idx = arr2[i].index(arr2[i].startIndex, offsetBy: j)
            let arr2Letter = arr2[i][arr2Idx]
            
            if arr1Letter == "#" || arr2Letter == "#" {
                maze[i][j] = "#"
            }
        }
    }
    let mazeArray = maze.map{$0.joined()}
    return mazeArray
}
