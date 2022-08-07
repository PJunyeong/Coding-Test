//
//  다트 게임.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/07.
//

import Foundation

func solution(_ dartResult:String) -> Int {
    let dartArray = Array(dartResult).map{String($0)}
    var tmp = ""
    var scoreDict = [Int:Int]()
    var scoreIdx = 1
    for letter in dartArray {
        if Character(letter).isNumber {
            tmp += letter
        } else {
            let score = tmp.isEmpty ? 0 : Int(tmp)!
            tmp = ""
            if letter == "S" {
                scoreDict[scoreIdx] = score
                scoreIdx += 1
            } else if letter == "D" {
                scoreDict[scoreIdx] = score * score
                scoreIdx += 1
            } else if letter == "T" {
                scoreDict[scoreIdx] = score * score * score
                scoreIdx += 1
            } else if letter == "*" {
                if scoreIdx - 2 > 0 {
                    let score = scoreDict[scoreIdx - 2] ?? 0
                    scoreDict[scoreIdx - 2] = score * 2
                }
                let score = scoreDict[scoreIdx - 1] ?? 0
                scoreDict[scoreIdx - 1] = score * 2
            } else {
                let score = scoreDict[scoreIdx - 1] ?? 0
                scoreDict[scoreIdx - 1] = score * -1
            }
        }
    }
    let answer = scoreDict.values.reduce(0, +)
    return answer
}
