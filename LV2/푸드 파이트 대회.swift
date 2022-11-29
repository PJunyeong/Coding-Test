//
//  푸드 파이트 대회.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/29.
//

import Foundation

func solution(_ food:[Int]) -> String {
    var answer = ""
    for index in 1..<food.count {
        let foodType = food[index]
        let number = foodType / 2
        for _ in 0..<number {
            answer += "\(number)"
        }
    }
    answer = answer + "0" + answer.reversed()
    return answer
}
