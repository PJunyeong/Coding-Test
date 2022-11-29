//
//  할인 행사.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/29.
//

import Foundation

func solution(_ want:[String], _ number:[Int], _ discount:[String]) -> Int {
    var dict = [String:Int]()
    var discountDict = [String:Int]()
    for index in 0..<10 {
        let item = discount[index]
        let number = discountDict[item] ?? 0
        discountDict[item] = number + 1
    }
    for index in 0..<want.count {
        let wantItem = want[index]
        let wantNumber = number[index]
        dict[wantItem] = wantNumber
    }
    
    func isDiscountable() -> Bool {
        for item in dict {
            let key = item.key
            let value = item.value
            let discountValue = discountDict[key] ?? 0
            if discountValue < value {
                return false
            }
        }
        return true
    }
    var answer = 0
    
    if isDiscountable() {
        answer += 1
    }
    for index in 10..<discount.count {
        let removed = discount[index-10]
        let added = discount[index]
        discountDict[removed] = (discountDict[removed] ?? 0) - 1
        discountDict[added] = (discountDict[added] ?? 0) + 1
        if isDiscountable() {
            answer += 1
        }
    }
    
    return answer
}
