//
//  H-Index.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/11.
//

import Foundation

func solution(_ citations:[Int]) -> Int {
    var citations = citations.sorted(by: >)
    var hIdx = 0
    var h = citations[hIdx]
    let n = citations.count
    
    while hIdx < citations.count {
        h = citations[hIdx]
        let hCitationsCnt = citations.filter{$0 >= h}.count
        if hCitationsCnt >= h && (n - hCitationsCnt) <= h {
            return h
        }
        hIdx += 1
    }
    return 0
}
