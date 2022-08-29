//
//  1644_소수의 연속합.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/29.
//

import Foundation

let N = Int(String(readLine()!))!
let primes = eratos(N)
var accumulatedPrimes = getAccumulatedPrimes(primes)

var total = 0

for idx1 in 0..<accumulatedPrimes.count {
    let first = accumulatedPrimes[idx1]
    for idx2 in idx1..<accumulatedPrimes.count {
        let second = accumulatedPrimes[idx2]
        if second - first == N {
            total += 1
            break
        } else if second - first > N {
            break
        }
    }
}

print(total)

func getAccumulatedPrimes(_ primes: [Int]) -> [Int] {
    if primes.isEmpty {
        return []
    }
    var tmp = [Int]()
    tmp.append(primes[0])
    for idx in 1..<primes.count {
        guard let last = tmp.last else { break }
        let newValue = last + primes[idx]
        tmp.append(newValue)
    }
    return [0] + tmp
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
    let filteredNumbers = numbers.enumerated().filter{$0.element}.map{$0.offset}
    return filteredNumbers
}
