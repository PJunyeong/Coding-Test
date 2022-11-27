//
//  귤 고르기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/27.
//

import Foundation

func solution(_ k:Int, _ tangerine:[Int]) -> Int {
    var numberDict = [Int:Int]()
    for t in tangerine {
        let number = numberDict[t] ?? 0
        numberDict[t] = number + 1
    }
    let sortedNumbers = numberDict.values.sorted(by: >)
    var number = 0
    var answer = 0
    for item in sortedNumbers.enumerated() {
        let index = item.offset
        let element = item.element
        
        if number + element >= k {
            answer = index + 1
            break
        }
        number += element
    }
    return answer
}
