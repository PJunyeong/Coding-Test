//
//  1751_수 정렬하기 2.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/27.
//

import Foundation

let N = Int(String(readLine()!))!
var numbers = [Int]()
for _ in 0..<N {
    let number = Int(String(readLine()!))!
    numbers.append(number)
}

numbers.sort(by: <)

for number in numbers {
    print(number)
}
