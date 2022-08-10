//
//  피로도.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/10.
//

import Foundation

var total = 0
var checked = [Bool]()

func solution(_ k:Int, _ dungeons:[[Int]]) -> Int {
    checked = Array(repeating: false, count: dungeons.count)
    DFS(k, 0, dungeons, [])
    return total
}

func DFS(_ curK: Int, _ curCount: Int, _ dungeons: [[Int]], _ curRoute: [Int]) {
    if curK >= 0 {
        total = max(total, curCount)
    }
    
    for idx in 0..<dungeons.count {
        if !checked[idx] && curK >= dungeons[idx][0] {
            checked[idx] = true
            DFS(curK - dungeons[idx][1], curCount + 1, dungeons, curRoute + [idx])
            checked[idx] = false
        }
    }
}
