//
//  11441_합 구하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/06.
//

import Foundation

let N = Int(String(readLine()!))!
let nodes = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
var summed = Array(repeating: 0, count: N+1)
for idx in 1..<N+1 {
    summed[idx] = summed[idx-1] + nodes[idx-1]
}
let M = Int(String(readLine()!))!
for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (start, end) = (input[0], input[1])
    print(summed[end] - summed[start-1])
}
