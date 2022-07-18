//
//  13305_주유소.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/18.
//

import Foundation

let N = Int(String(readLine()!))!
let cities = readLine()!.split(separator: " ").map{Int(String($0))!}
let prices = readLine()!.split(separator: " ").map{Int(String($0))!}

var total = 0
var localPrice = prices[0]

for i in 0..<N-1 {
    if prices[i] < localPrice {
        localPrice = prices[i]
    }
    total += localPrice * cities[i]
}

print(total)
