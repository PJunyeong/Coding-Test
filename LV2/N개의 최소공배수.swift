//
//  N개의 최소공배수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/31.
//
import Foundation

func solution(_ arr:[Int]) -> Int {
    var lcd = arr[0]
    if arr.count > 1 {
        for idx in 1..<arr.count {
            let gcd = getGCD(lcd, arr[idx])
            lcd = lcd * arr[idx] / gcd
        }
    }
    return lcd
}

func getGCD(_ num1: Int, _ num2: Int) -> Int {
    if num1 > 0 && num2 > 0 && abs(num1 - num2) > 0 {
        return getGCD(abs(num1 - num2), min(num1, num2))
    } else {
        return min(num1 ,num2)
    }
}
