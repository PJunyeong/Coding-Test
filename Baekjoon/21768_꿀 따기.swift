//
//  21768_꿀 따기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/16.
//

import Foundation

let N = Int(String(readLine()!))!
let honeys = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
var toRight = honeys
var toLeft = honeys
for i in 1..<N {
    toRight[i] += toRight[i-1]
    toLeft[N-i-1] += toLeft[N-i]
}

var answer = 0
// 1. 벌 - 벌 - 꿀통
let leftMostBee = toRight[N-1] - honeys[0]
for i in 1..<N-1 {
     let rightBee = toRight[N-1] - toRight[i]
    answer = max(answer, leftMostBee - honeys[i] + rightBee)
}
// 2. 벌 - 꿀통 - 벌
for i in 1..<N-1 {
    let leftMostBee = toRight[i] - honeys[0]
    let rightMostBee = toRight[N-1] - toRight[i-1] - honeys[N-1]
    answer = max(answer, leftMostBee + rightMostBee)
}

// 3. 꿀통 - 벌 - 벌
let rightMostBee = toRight[N-1] - honeys[N-1]
for i in 1..<N-1 {
    let leftMostBee = toRight[i-1]
    answer = max(answer, leftMostBee + rightMostBee - honeys[i])
}

print(answer)

