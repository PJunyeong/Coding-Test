//
//  올바른 괄호.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/11.
//

import Foundation

func solution(_ s:String) -> Bool {
    return isRight(s)
}

func isRight(_ bracket: String) -> Bool {
    let brackets = Array(bracket)
    var stack = [Character]()
    for letter in brackets {
        if letter == "(" {
            stack.append(letter)
        } else {
            if !stack.isEmpty {
                stack.removeLast()
            } else {
                return false
            }
        }
    }
    return stack.isEmpty ? true: false
}
