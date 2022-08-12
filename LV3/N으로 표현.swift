//
//  N으로 표현.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/13.
//

import Foundation

func solution(_ N:Int, _ number:Int) -> Int {
    var dp = Array(repeating: [Int](), count: 9)
    for cnt in 1..<9 {
        var curNumbers = Set<Int>()
        var base = ""
        for _ in 0..<cnt {
            base += "\(N)"
        }
        curNumbers.insert(Int(base)!)
        
        for i in 1..<cnt {
            for j in dp[i] {
                for k in dp[cnt-i] {
                    let numbers = Set(makeNumber(j, k))
                    numbers.map{curNumbers.insert($0)}
                }
            }
        }
        if curNumbers.contains(number) {
            return cnt
        }
        dp[cnt] = Array(curNumbers)
    }
    return -1
}

func makeNumber(_ number1: Int, _ number2: Int) -> [Int] {
    var numbers = [Int]()
    numbers.append(number1 + number2)
    numbers.append(number2 - number1)
    numbers.append(number1 - number2)
    numbers.append(number1 * number2)
    if number1 != 0 {
        numbers.append(number2 / number1)
    }
    if number2 != 0 {
        numbers.append(number1 / number2)
    }
    return numbers
}

