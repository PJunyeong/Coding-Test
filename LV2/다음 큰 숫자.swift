//
//  다음 큰 숫자.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/31.
//

import Foundation

func solution(_ n:Int) -> Int {
    let binary = String(n, radix:2)
    let originalCount = binary.filter{$0 == "1"}.count
    var curNum = n + 1
    while true {
        if String(curNum, radix:2).filter{$0 == "1"}.count == originalCount {
            break
        } else {
            curNum += 1
        }
    }
    return curNum
}

