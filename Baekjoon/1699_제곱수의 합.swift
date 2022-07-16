//
//  1699_제곱수의 합.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/16.
//

import Foundation

let N = Int(String(readLine()!))!

func getNumber(num: Int) -> Int {
    var dp = Array(repeating: 0, count: num+1)
    if num <= 3 {
        return num
    } else {
        var powered = [Int]()
        powered.append(0)
        let sqrtLimit = Int(sqrt(Double(num)))
        for i in 1..<(sqrtLimit+1) {
            powered.append(i * i)
        }
        // powered[index] = index * index
        dp[1] = 1
        dp[2] = 2
        dp[3] = 3
        var cursor = 2
        // cursor는 제곱했을 때 현재 수보다 작은 수 중 가장 큰 수
        for i in 4..<(num+1) {
            if (cursor + 1) * (cursor + 1) == i {
                cursor += 1
            }
            if cursor * cursor == i {
                dp[i] = 1
                // 현재 인덱스 자체가 제곱수일 때 체크
            } else {
                var curMin = Int.max
                for j in 1..<(cursor + 1) {
                    curMin = min(1 + dp[i - powered[j]], curMin)
                }
                dp[i] = curMin
                // j(cursor...1)까지 제곱수를 현재 수에서 뺀 수 인덱싱
                // -> 1 + dp[x] 개를 통해 현재 수 i를 표현 가능 보장
                // i를 표현 가능한 수 중 최소 개수 dp에 기록하기
            }
        }
        return dp[num]
    }
}

let answer = getNumber(num: N)
print(answer)
