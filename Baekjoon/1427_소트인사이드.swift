//
//  1427_소트인사이드.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/04.
//

import Foundation

var number = Array(readLine()!.map{String($0)})
number.sort(by: >)
let sortedNumber = Int(number.joined())!
print(sortedNumber)
