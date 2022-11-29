//
//  롤케이크 자르기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/29.
//

import Foundation

func solution(_ topping:[Int]) -> Int {
    var left = Array(repeating: 0, count: topping.count)
    var right = Array(repeating: 0, count: topping.count)
    var toppingSet = Set<Int>()
    for index in 0..<topping.count {
        let food = topping[index]
        toppingSet.insert(food)
        left[index] = toppingSet.count
    }
    toppingSet.removeAll()
    for index in stride(from: topping.count-1, to: -1, by: -1) {
        let food = topping[index]
        toppingSet.insert(food)
        right[index] = toppingSet.count
    }
    
    var answer = 0
    for index in 0..<topping.count-1 {
        if left[index] == right[index+1] {
            answer += 1
        }
    }
    return answer
}
