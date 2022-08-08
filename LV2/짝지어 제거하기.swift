//
//  짝지어 제거하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/08.
//

import Foundation

func solution(_ s:String) -> Int{
    var stack = [Character]()
    let stringArray = Array(s)
    
    for letter in stringArray {
        if !stack.isEmpty {
            if stack.last! == letter {
                stack.removeLast()
            } else {
                stack.append(letter)
            }
        } else {
            stack.append(letter)
        }
    }
    
    if !stack.isEmpty {
        return 0
    } else {
        return 1
    }
}
