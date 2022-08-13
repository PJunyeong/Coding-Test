//
//  위장.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/13.
//

import Foundation

func solution(_ clothes:[[String]]) -> Int {
    var clothDict = [String:[String]]()
    for cloth in clothes {
        let (name, type) = (cloth[0], cloth[1])
        let clothValue = clothDict[type] ?? []
        clothDict[type] = clothValue + [name]
    }
    let values = clothDict.values
    var answer = 1
    
    for value in values {
        let cnt = value.count
        answer *= (cnt + 1)
    }
    answer -= 1
    return answer
}
