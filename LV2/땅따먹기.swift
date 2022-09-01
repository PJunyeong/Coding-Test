//
//  땅따먹기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/01.
//

import Foundation

func solution(_ land:[[Int]]) -> Int {
    var land = land
    let rowCount = land.count
    
    for row in 1..<rowCount {
        land[row][0] = max(land[row-1][1], land[row-1][2], land[row-1][3]) + land[row][0]
        land[row][1] = max(land[row-1][0], land[row-1][2], land[row-1][3]) + land[row][1]
        land[row][2] = max(land[row-1][0], land[row-1][1], land[row-1][3]) + land[row][2]
        land[row][3] = max(land[row-1][0], land[row-1][1], land[row-1][2]) + land[row][3]
    }
    let answer = land.last!.max()!
    return answer
}
