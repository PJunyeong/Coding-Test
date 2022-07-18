//
//  1026_보물.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/18.
//

import Foundation

let N = Int(String(readLine()!))!
var numbers1 = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
var numbers2 = Array(readLine()!.split(separator: " ").map{Int(String($0))!})

numbers1.sort()
numbers2.sort(by: >)

var total = 0

for i in 0..<N {
    let num = numbers1[i] * numbers2[i]
    total += num
}

print(total)
