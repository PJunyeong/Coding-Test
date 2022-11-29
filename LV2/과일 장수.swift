//
//  과일 장수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/29.
//

import Foundation

func solution(_ k:Int, _ m:Int, _ score:[Int]) -> Int {
    let fruitBoxCount = score.count / m
    let score = score.sorted(by: >).prefix(fruitBoxCount * m)
    var answer = 0
    for index in stride(from: m-1, to: score.count, by: m) {
        let p = score[index]
        answer += (p * m)
    }
    return answer
}
