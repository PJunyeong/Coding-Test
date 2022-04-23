//
//  9935_문자열 폭발.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/22.
//

import Foundation

let s = String(readLine()!)
let ex = Array(String(readLine()!))
var stack = Array<Character>()
for letter in s{
    stack.append(letter)
    if stack.count >= ex.count{
        if stack[stack.endIndex-ex.count..<stack.endIndex] == ex[0..<ex.endIndex]{
            for _ in 0..<ex.count{
                stack.popLast()
            }
        }
    }
}

if stack.isEmpty == true{
    print("FRULA")
} else {
    for letter in stack{
        print(letter, terminator: "")
    }
}

