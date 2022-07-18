//
//  2839_설탕 배달.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/18.
//

import Foundation

let N = Int(String(readLine()!))!

func makeSugar(sugar: Int) -> Int {
    var sugar = sugar
    var total = 0
    while sugar >= 0 {
        if sugar % 5 == 0 {
            total += sugar / 5
            return total
        }
        sugar -= 3
        total += 1
    }
    return -1
}
let answer = makeSugar(sugar: N)
print(answer)
