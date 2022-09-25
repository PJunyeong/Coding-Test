//
//  괄호 회전하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/25.
//

import Foundation

func solution(_ s:String) -> Int {
    var total = 0
    
    for idx in 0..<s.count {
        let first = s.index(s.startIndex, offsetBy: idx)
        let firstString = s[s.startIndex..<first]
        let secondString = s[first..<s.endIndex]

        let targetString = secondString + firstString
        if isRightBrachet(word: String(targetString)) {
            total += 1
        }
    }
    
    return total
}

func isRightBrachet(word: String) -> Bool {
    var stack = [Character]()
    var brachetPair:[Character:Character] = [")" : "(", "]" : "[", "}" : "{"]
    for letter in word {
        if let pair = brachetPair[letter] {
            if let last = stack.last {
                if last == pair {
                    stack.removeLast()
                } else {
                    stack.append(letter)
                }
            } else {
                stack.append(letter)
            }
        } else {
            stack.append(letter)
        }
    }
    return stack.isEmpty
}

let s = "}]()[{"
solution(s)
