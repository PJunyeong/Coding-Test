//
//  메뉴 리뉴얼.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/08.
//

import Foundation

var orderDict = [String:(Int, Int)]()
var checked = Array(repeating: false, count: 10)
var orderArray = [String]()

func solution(_ orders:[String], _ course:[Int]) -> [String] {
    var result = [String]()
    
    for order in orders {
        orderArray = Array(order).map{String($0)}
        for count in course {
            if orderArray.count < count {
                continue
            }
            DFS(startIdx: 0, orders: [], count: count)
            checked = Array(repeating: false, count: 10)
        }
    }
    
    for count in course {
        guard let max = orderDict.filter{$0.value.0 == count && $0.value.1 >= 2}.map{$0.value.1}.max() else { continue }
        let maxOrders = orderDict.filter{$0.value.0 == count && $0.value.1 == max}.map{$0.key}
        result += maxOrders
    }
    result.sort()
    
    return result
}

func DFS(startIdx: Int, orders: [String], count: Int) {
        if orders.count == count {
            let combination = orders.sorted().joined()
            var orderDictValue = orderDict[combination] ?? (count, 0)
            orderDictValue.1 += 1
            orderDict[combination] = orderDictValue
            return
        }
        for idx in startIdx..<orderArray.count {
            if !checked[idx] {
                checked[idx] = true
                DFS(startIdx: idx, orders: orders + [orderArray[idx]], count: count)
                checked[idx] = false
            }
        }
}
