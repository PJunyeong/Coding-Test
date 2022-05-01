//
//  1744_수 묶기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/01.
//

import Foundation

let N = Int(String(readLine()!))!
var positive = [Int]()
var zeros = [Int]()
var negative = [Int]()
for _ in 0..<N{
    let num = Int(String(readLine()!))!
    if num > 0{
        positive.append(num)
    } else if num == 0{
        zeros.append(num)
    } else{
        negative.append(num)
    }
}

var total = 0

positive.sort(by: <)

while true{
    if positive.isEmpty == false && positive[0] == 1{
        total += positive.removeFirst()
    } else{
        break
    }
}

if positive.count % 2 == 1{
    total += positive.removeFirst()
}

var cursor = 0
for _ in 0..<positive.count/2{
    let times = positive[cursor] * positive[cursor+1]
    total += times
    cursor += 2
}

negative.sort(by: >)
if negative.count % 2 == 1 && zeros.count > 1{
    negative.removeFirst()
} else if negative.count % 2 == 1 && zeros.count < 1{
    total += negative.removeFirst()
}

cursor = 0
for _ in 0..<negative.count/2{
    let times = negative[cursor] * negative[cursor+1]
    total += times
    cursor += 2
}

print(total)
