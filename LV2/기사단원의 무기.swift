//
//  기사단원의 무기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/29.
//

import Foundation

func solution(_ number:Int, _ limit:Int, _ power:Int) -> Int {
    let primes = eratos(number: number)
    var answer = 0
    
    func getDivisorsNum(_ number: Int) -> Int {
        var result = 1
        var number = number
        for prime in primes {
            if number < prime {
                break
            }
            var count = 0
            while number % prime == 0 {
                number /= prime
                count += 1
            }
            if count > 0 {
                result *= (count + 1)
            }
        }
        return result
    }
    
    for num in 1...number {
        let divisorsNum = getDivisorsNum(num)
        let plused = divisorsNum > limit ? power : divisorsNum
        answer += plused
    }
    return answer
}

func eratos(number: Int) -> [Int] {
    var numbers = Array(repeating: true, count: number + 1)
    numbers[0] = false
    numbers[1] = false
    for idx in 2..<numbers.count {
        if numbers[idx] {
            if idx * 2 < numbers.count {
                for idx2 in stride(from: idx * 2, to: numbers.count, by: idx) {
                    numbers[idx2] = false
                }
            }
        }
    }
    let primes = numbers.enumerated().filter({$0.element}).map({$0.offset})
    return primes
}
