//
//  1038_감소하는 수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/07.
//

import Foundation

let number = Int(String(readLine()!))!

var numbers = [String]()
for i in 0..<10 {
    numbers.append(String(i))
}
var check = Array(repeating: false, count: 10)
var answers = [Int]()
answers.append(0)

func DFS(digits: [String]) -> Void {
    if !digits.isEmpty {
        let answer = digits.joined()
        answers.append(Int(answer)!)
    }
    
    for idx in 0..<10 {
        if !check[idx] {
            if (digits.isEmpty && idx != 0) || (!digits.isEmpty && digits.last! > String(idx)) {
                check[idx] = true
                DFS(digits: digits + [numbers[idx]])
                check[idx] = false
            }
        }
    }
}

DFS(digits: [])
answers.sort()

print(number < answers.count ? answers[number] : -1)

