//
//  k진수에서 소수 개수 구하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/23.
//

import Foundation

func solution(_ n:Int, _ k:Int) -> Int {
    let convertedNumber = convertKary(n, k)
    let splitNumber = convertedNumber.split(separator: "0")
    var total = 0
    for number in splitNumber {
        if isPrime(Int(number)!) {
            total += 1
        }
    }
    return total
}

func convertKary(_ n: Int, _ k: Int) -> String {
    var result = ""
    var n = n
    while n > 0 {
        let q = n / k
        let r = n % k
        result += String(r)
        n = q
    }
    let converted = String(result.reversed())
    return converted
}

func isPrime(_ number: Int) -> Bool {
    if number < 2 {
        return false
    }
    
    let term = Int(sqrt(Double(number))) + 1
    for check in 2..<term {
        if number % check == 0 {
            return false
        }
    }
    return true
}

solution(437674, 3)
