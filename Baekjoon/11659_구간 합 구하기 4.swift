//
//  11659_구간 합 구하기 4.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/06.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
let numbers = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
var plusedNumbers = Array(repeating: 0, count: N+1)
plusedNumbers[1] = numbers[0]
for idx in 2..<N+1 {
    plusedNumbers[idx] = plusedNumbers[idx-1] + numbers[idx-1]
}
var total = 0
for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (idx1, idx2) = (input[0], input[1])
    print(plusedNumbers[idx2] - plusedNumbers[idx1-1])
}
