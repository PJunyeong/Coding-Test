//
//  1065_한수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/04.
//

import Foundation

func isArithmeticSequence(number: [String]) -> Bool {
    if number.count <= 2 {
        return true
    }
    
    let left = Int(number[0])!
    let right = Int(number[1])!
    let offset = left - right
    
    for idx in 1..<number.count-1 {
        let left = Int(number[idx])!
        let right = Int(number[idx+1])!
        let newOffset = left - right
        if offset != newOffset {
            return false
        }
    }
    return true
}


let N = Int(String(readLine()!))!
var total = 0
for number in 1...N {
    let newNumber = Array(String(number)).map{String($0)}
    if isArithmeticSequence(number: newNumber) {
        total += 1
    }
}

print(total)
