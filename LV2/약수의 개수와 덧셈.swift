//
//  약수의 개수와 덧셈.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/30.
//

import Foundation

func solution(_ left:Int, _ right:Int) -> Int {
    let primes = eratos(right)
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
    
    for number in left...right {
        let divisorsNum = getDivisorsNum(number)
        if divisorsNum % 2 == 0 {
            answer += number
        } else {
            answer -= number
        }
    }
    
    return answer
}

func eratos(_ number: Int) -> [Int] {
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
    let primes = numbers.enumerated().filter{$0.element}.map{$0.offset}
    return primes
}
