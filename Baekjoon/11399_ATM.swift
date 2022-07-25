//
//  11399_ATM.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/25.
//

import Foundation

let N = Int(String(readLine()!))!
var people = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
people.sort()
var total = 0
var waiting = 0
for person in people {
    waiting += person
    total += waiting
}

print(total)
Foundation
