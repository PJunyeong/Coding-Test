//
//  1786_찾기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/29.
//

import Foundation

let T = Array(readLine()!.map{String($0)})
let P = Array(readLine()!.map{String($0)})

func KMP(source:[String], target:[String]) -> [Int] {
    let sourceCnt = source.count
    let targetCnt = target.count
    var answers = [Int]()
    
    var LPS = Array(repeating: 0, count: targetCnt)
    LPS = LPScompute(target:target, LPS:LPS)
    
    var sourceIdx = 0
    var targetIdx = 0
    
    while (sourceIdx < sourceCnt) {
        if target[targetIdx] == source[sourceIdx] {
            sourceIdx += 1
            targetIdx += 1
        } else {
            if targetIdx == 0 {
                sourceIdx += 1
            } else {
                targetIdx = LPS[targetIdx - 1]
            }
        }
        if targetIdx == targetCnt {
            targetIdx = LPS[targetIdx - 1]
            answers.append(sourceIdx - targetCnt + 1)
        }
    }
    return answers
}

func LPScompute(target:[String], LPS:[Int]) -> [Int] {
    var length = 0
    var idx = 1
    var LPS = LPS
    while (idx < target.count) {
        if target[idx] == target[length] {
            length += 1
            LPS[idx] = length
            idx += 1
        } else {
            if length == 0 {
                LPS[idx] = 0
                idx += 1
            } else {
                length = LPS[length - 1]
            }
        }
    }
    return LPS
}

let answers = KMP(source: T, target: P)
print(answers.count)
for answer in answers {
    print(answer, separator: " ")
}
