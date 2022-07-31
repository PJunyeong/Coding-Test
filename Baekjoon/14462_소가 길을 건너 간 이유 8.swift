//
//  14462_소가 길을 건너 간 이유 8.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/31.
//

import Foundation

let N = Int(String(readLine()!))!
var leftCows = [0]
var rightCows = [0]
for _ in 0..<N {
    let cow = Int(String(readLine()!))!
    leftCows.append(cow)
}
for _ in 0..<N {
    let cow = Int(String(readLine()!))!
    rightCows.append(cow)
}

var dp = Array(repeating: Array(repeating: 0, count: N+1), count: N+1)

for i in 1..<N+1 {
    for j in 1..<N+1 {
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        if abs(leftCows[i] - rightCows[j]) <= 4 {
            dp[i][j] = dp[i-1][j-1] + 1
        }
    }
}

print(dp[N][N])

