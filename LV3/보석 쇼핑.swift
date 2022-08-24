//
//  보석 쇼핑.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/24.
//

import Foundation

func solution(_ gems:[String]) -> [Int] {
    var result = [1, gems.count]
    var start = 0
    var end = 0
    var gemDict = [String:Int]()
    let gemTotalCount = Set(gems).count
    
    while end < gems.count {
        let gem = gems[end]
        let gemCount = gemDict[gem] ?? 0
        gemDict[gem] = gemCount + 1
        
        end += 1
        
        if gemDict.count == gemTotalCount {
            while start < end {
                let gem = gems[start]
                let gemCount = gemDict[gem] ?? -1
                
                if gemCount > 1 {
                    gemDict[gem] = gemCount - 1
                    start += 1
                } else {
                    if end - start <= result[1] - result[0] {
                        result = [start + 1, end]
                    }
                    break
                }
            }
        }
    }
        
    return result
}
