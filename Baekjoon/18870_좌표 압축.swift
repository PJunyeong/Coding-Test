//
//  18870_좌표 압축.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/25.
//

import Foundation

let N = Int(String(readLine()!))!
var dots = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
var sortedDots = Array(Set(dots))
sortedDots.sort()
var dotsDict = [Int:Int]()
for data in sortedDots.enumerated() {
    dotsDict[data.element] = data.offset
}

for dot in dots {
    print(dotsDict[dot] ?? 0, terminator: " ")
}


