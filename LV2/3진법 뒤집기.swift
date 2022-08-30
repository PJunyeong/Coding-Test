//
//  3진법 뒤집기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/30.
//

import Foundation

func solution(_ n:Int) -> Int {
    let convertedNumber = getReversedKnary(n, 3)
    let decimal = calculate(convertedNumber, 3)
    return decimal
}

func calculate(_ number: String, _ K: Int) -> Int {
    var times = 1
    var total = 0
    for digit in number.reversed() {
        total += Int(String(digit))! * times
        times *= K
    }
    return total
}

func getReversedKnary(_ number: Int, _ K: Int) -> String {
    var number = number
    var convertedNumber = ""
    while number > 0 {
        let q = number / K
        let r = number % K
        number = q
        convertedNumber += String(r)
    }
    return convertedNumber
}
