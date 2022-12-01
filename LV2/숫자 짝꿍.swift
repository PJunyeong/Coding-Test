//
//  숫자 짝꿍.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/12/01.
//

import Foundation

func solution(_ X:String, _ Y:String) -> String {
    var leftDict = [Character: Int]()
    var rightDict = [Character: Int]()
    for number in X {
        let count = leftDict[number] ?? 0
        leftDict[number] = count + 1
    }
    for number in Y {
        let count = rightDict[number] ?? 0
        rightDict[number] = count + 1
    }
    var answer = ""
    for number in "9876543210" {
        let minCount = min(leftDict[number] ?? 0, rightDict[number] ?? 0)
        for _ in 0..<minCount {
            answer.append(number)
        }
    }
    
    if answer.isEmpty {
        return "-1"
    } else if answer.first == "0" {
        return "0"
    } else {
        return answer
    }
}
