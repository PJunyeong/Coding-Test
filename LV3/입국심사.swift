//
//  입국심사.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/14.
//

import Foundation

func solution(_ n:Int, _ times:[Int]) -> Int64 {
    var times = times
    times.sort(by: <)
    var left = 0
    var right = times.last! * n
    var result = 0
    
    while left <= right {
        let middle = (left + right) / 2
        var people = 0
        for time in times {
            people += middle / time
            if people >= n {
                break
            }
        }
        if people >= n {
            right = middle - 1
            result = middle
        } else {
            left = middle + 1
        }
    }
    return Int64(result)
}
