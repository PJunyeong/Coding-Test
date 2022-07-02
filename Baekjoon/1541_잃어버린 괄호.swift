//
//  1541_잃어버린 괄호.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/02.
//

import Foundation

let expression = String(readLine()!)

func solution(expression: String) -> Int {
    var total = 0
    var tmp = ""
    var minus = false

    for digit in expression {
        if digit.isNumber {
            tmp += String(digit)
        } else {
            if !minus && digit == "+" {
                total += Int(tmp)!
                tmp = ""
            } else if !minus && digit == "-" {
                minus = true
                total += Int(tmp)!
                tmp = ""
            } else if minus {
                total -= Int(tmp)!
                tmp = ""
            }
        }
    }

    if minus {
        total -= Int(tmp)!
    } else {
        total += Int(tmp)!
    }
    return total
}

let total = solution(expression: expression)
print(total)
