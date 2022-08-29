//
//  1747_소수&팰린드롬.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/29.
//

import Foundation

let N = Int(String(readLine()!))!
var boxes = Array(repeating: true, count: 10_000_000)
boxes[0] = false
boxes[1] = false
for idx in 2..<boxes.count {
    if boxes[idx] {
        if idx * 2 < boxes.count {
            for idx2 in stride(from: idx * 2, to: boxes.count, by: idx) {
                boxes[idx2] = false
            }
        }
    }
}

let filteredBoxes = boxes.enumerated().filter{$0.element && $0.offset >= N}.map{$0.offset}


for number in filteredBoxes {
    if isPalindrome(number) {
        print(number)
        break
    }
}

func isPalindrome(_ number: Int) -> Bool {
    var number = Array(String(number)).map{String($0)}
    if number.count % 2 == 1 {
        number.remove(at: number.count / 2)
    }
    
    if number.isEmpty {
        return true
    }
    
    for idx in 0..<(number.count / 2 + 1) {
        if number[idx] != number[number.count - 1 - idx] {
            return false
        }
    }
    return true
}
