//
//  두 개 뽑아서 더하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/30.
//

import Foundation

func solution(_ numbers:[Int]) -> [Int] {
    var result = Set<Int>()
    for idx1 in 0..<numbers.count {
        let first = numbers[idx1]
        for idx2 in idx1+1..<numbers.count {
            let second = numbers[idx2]
            result.insert(first + second)
        }
    }
    let sortedResult = Array(result).sorted(by: <)
    return sortedResult
}
