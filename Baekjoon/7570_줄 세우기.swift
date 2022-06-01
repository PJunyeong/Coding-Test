//
//  7570_줄 세우기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/01.
//

import Foundation

let N = Int(String(readLine()!))!
let kids = [0] + Array(readLine()!.split(separator: " ").map{Int(String($0))!})
var indices = Array(repeating: 0, count: N+1)
for idx in 1..<N+1 {
    indices[kids[idx]] = idx
}

var cnt = 0
var answer = 0

for idx in 1..<N {
    if indices[idx] < indices[idx+1] {
        cnt += 1
        answer = max(cnt, answer)
    } else {
        cnt = 0
    }
}

print(N-answer-1)
