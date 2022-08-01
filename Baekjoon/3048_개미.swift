//
//  3048_개미.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/01.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N1, N2) = (input[0], input[1])
var firstAnts = Array(readLine()!).map{String($0)}
let firstAntsSet = Set(firstAnts)
firstAnts.reverse()
var secondAnts = Array(readLine()!).map{String($0)}
let secondAntsSet = Set(secondAnts)
let T = Int(String(readLine()!))!

var ants = firstAnts + secondAnts

for _ in 0..<T {
    var tmpIdx = [Int]()
    for idx in 0..<ants.count-1 {
        if firstAntsSet.contains(ants[idx]) && secondAntsSet.contains(ants[idx+1]) {
            tmpIdx.append(idx)
        }
    }
    for idx in tmpIdx {
        ants.swapAt(idx, idx+1)
    }
}
print(ants.joined())


