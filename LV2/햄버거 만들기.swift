//
//  햄버거 만들기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/29.
//

import Foundation

func solution(_ ingredient:[Int]) -> Int {
    var stack = [Int]()
    var answer = 0
    for food in ingredient {
        stack.append(food)
        answer += isBurger(stack: &stack)
    }
    return answer
}

func isBurger( stack: inout [Int]) -> Int {
    guard stack.count >= 4 else { return 0 }
    let lastIndex = stack.count - 1
    if stack[lastIndex] == 1 && stack[lastIndex-1] == 3 && stack[lastIndex-2] == 2 && stack[lastIndex-3] == 1 {
        for _ in 0..<4 {
            stack.popLast()
        }
        return 1
    } else {
        return 0
    }
}

let ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
solution(ingredient)
