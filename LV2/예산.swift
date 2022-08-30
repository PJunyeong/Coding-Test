//
//  예산.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/30.
//

import Foundation

func solution(_ d:[Int], _ budget:Int) -> Int {
    var d = d.sorted(by: <)
    var budget = budget
    var total = 0
    for item in d {
        if budget >= item {
            budget -= item
            total += 1
        } else {
            break
        }
    }
    return total
}
