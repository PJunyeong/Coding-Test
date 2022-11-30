//
//  삼총사.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/30.
//

import Foundation

func solution(_ number:[Int]) -> Int {
    var answer = 0
    
    func depthFirstSearch(_ index: Int, _ sum: Int, _ count: Int) {
        if count == 3 {
            if sum == 0 {
                answer += 1
            }
            return
        }
        
        for nextIndex in (index+1)..<number.count {
            depthFirstSearch(nextIndex, sum + number[nextIndex], count + 1)
        }
    }
    
    for firstIndex in 0..<number.count {
        depthFirstSearch(firstIndex, number[firstIndex], 1)
    }
    return answer
}
