//
// x 카펫.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/31.
//

import Foundation

func solution(_ brown:Int, _ yellow:Int) -> [Int] {
    var brown = (brown + 4) / 2
    var answer = [Int]()
    for row in 1...(brown / 2) {
        let col = brown - row
        let boxCount = row * col
        if boxCount - (row * 2) - (col * 2) + 4 == yellow {
            answer = [col, row]
            break
        }
    }
    return answer
}

