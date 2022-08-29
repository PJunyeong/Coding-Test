//
//  6219_소수의 자격.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/29.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (A, B, D) = (input[0], input[1], input[2])
var boxes = Array(repeating: true, count: B+1)
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

let filteredBoxes = boxes.enumerated().filter{$0.element && $0.offset >= A}.map{$0.offset}
var total = 0
for number in filteredBoxes {
    if isInPrime(number, D) {
        total += 1
    }
}

print(total)

func isInPrime(_ prime: Int, _ number: Int) -> Bool {
    
    let prime = Array(String(prime)).map{String($0)}
    let numCount = Array(String(number)).count
    let number = String(number)
    
    for idx in 0..<prime.count-numCount+1 {
        let checkedNumber = Array(prime[idx..<idx+numCount]).joined()
        if checkedNumber == number {
            return true
        }
    }
    return false
}
