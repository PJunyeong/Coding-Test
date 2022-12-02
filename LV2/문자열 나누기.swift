//
//  문자열 나누기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/12/02.
//

import Foundation

func solution(_ s:String) -> Int {
    var count = 0
    var x: Character?
    guard let firstCharacter = s.first else { return count }
    x = firstCharacter
    var left = 0
    var right = 0
    
    for letter in s {
        if x == nil {
            x = letter
        }
        
        if letter == x {
            left += 1
        } else {
            right += 1
        }
        
        if left == right {
            count += 1
            left = 0
            right = 0
            x = nil
        }
    }
    
    if x != nil {
        count += 1
    }
    
    return count
}
