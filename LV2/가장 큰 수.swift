//
//  가장 큰 수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/09.
//

import Foundation

func solution(_ numbers:[Int]) -> String {
    var numbers = numbers.map{String($0)}
    numbers.sort { a, b in
        let number1 = Int(a + b)!
        let number2 = Int(b + a)!
        if number1 >= number2 {
            return true
        } else {
            return false
        }
    }
    if numbers[0] == "0" {
        return "0"
    } else {
        return numbers.joined()
    }
}
