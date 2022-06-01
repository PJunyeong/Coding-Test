//
//  11509_풍선 맞추기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/01.
//

import Foundation

let N = Int(String(readLine()!))!
var balloons = Array(readLine()!.split(separator: " ").map{Int(String($0))!})

var cnt = 0
let maxHeight = balloons.max()!
var arrows = Array(repeating: 0, count: maxHeight + 1)
// 화살 높이는 0 ~ 최대 풍선 높이
for idx in 0..<N {
    if arrows[balloons[idx]] == 0 {
        // 이 풍선 높이에 해당하는 화살이 없다면 화살을 쏜다
        cnt += 1
        // 화살 카운트
        arrows[balloons[idx]-1] += 1
        // 풍선을 맞고 높이 1 감소한 화살. arrows에 해당 높이 화살 개수를 카운트
    } else {
        // 이 풍선 높이에 해당하는 화살이 존재
        arrows[balloons[idx]] -= 1
        // 풍선을 맞혔으므로 화살 높이 1 감소
        arrows[balloons[idx]-1] += 1
        // 높이 1 감소한 화살의 높이를 이 높이에 해당하는 화살 개수에 카운트
    }
}

print(cnt)
