//
//  5582_공통 부분 문자열.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/29.
//

import Foundation

let str1 = Array(readLine()!.map{String($0)})
let str2 = Array(readLine()!.map{String($0)})

var numbers = Array(repeating: Array(repeating: 0, count: str2.count + 1), count: str1.count + 1)

var answer = 0

for i in 1...str1.count {
    for j in 1...str2.count {
        if str1[i-1] == str2[j-1] {
            numbers[i][j] = numbers[i-1][j-1] + 1
            answer = max(answer, numbers[i][j])
        }
    }
}

print(answer)

