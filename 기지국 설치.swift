//
//  기지국 설치.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/12.
//

import Foundation

func solution(_ n:Int, _ stations:[Int], _ w:Int) -> Int {
    var total = 0
    let range = 2 * w + 1
    var cursor = 1
    for station in stations {
        if station - w <= cursor {
            cursor = station + w + 1
            continue
        }
        let coverage = station - w - cursor
        let q = coverage / range
        let r = coverage % range
        total += r == 0 ? q : (q + 1)
        cursor = station + w + 1
    }
    
    if cursor <= n {
        print(cursor)
        let coverage = n - cursor + 1
        let q = coverage / range
        let r = coverage % range
        total += r == 0 ? q : (q + 1)
    }
    return total
}
