//
//  9656_돌 게임2.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/01.
//
import Foundation

let N = Int(String(readLine()!))!
let dpCnt = N < 4 ? 4 : N+1
var dp = Array(repeating: 0, count: dpCnt)
// 1 상근 0 창영

dp[1] = 0
dp[2] = 1
dp[3] = 0

for i in 4..<dpCnt {
    if dp[i-1] == 0 || dp[i-3] == 0 {
        dp[i] = 1
    } else {
        dp[i] = 0
    }
}


if dp[N] == 1 {
    print("SK")
} else {
    print("CY")
}
