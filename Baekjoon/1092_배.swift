//
//  1092_배.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/08.
//

import Foundation

let N = Int(String(readLine()!))!
var weightLimits = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
let M = Int(String(readLine()!))!
var weights = Array(readLine()!.split(separator: " ").map{Int(String($0))!})

weightLimits.sort(by: >)
weights.sort(by: >)

if weightLimits[0] < weights[0] {
    print(-1)
} else {
    var total = 0
    while weights.isEmpty == false {
        for limit in weightLimits {
            for idx in 0..<weights.count {
                if limit >= weights[idx] {
                    weights.remove(at: idx)
                    break
                }
            }
        }
        total += 1
    }
    print(total)
}
