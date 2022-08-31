//
//  멀리 뛰기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/31.
//

import Foundation

func solution(_ n:Int) -> Int {
    var dp = Array(repeating: 0, count: n+1)
    if n == 1 {
        return 1
    } else if n == 2 {
        return 2
    }
    
    dp[1] = 1
    dp[2] = 2
    for i in 3..<dp.count {
        dp[i] = (dp[i-1] + dp[i-2]) % 1234567
    }
    return dp[n]
}
