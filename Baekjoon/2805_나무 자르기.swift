//
//  2805_나무 자르기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/17.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var trees = readLine()!.split(separator: " ").map{Int(String($0))!}
trees.sort(by: >)
var left = 0
var right = trees[0]
var answer = 0

while left <= right {
    let mid = (left + right) / 2
    var total = 0
    
    for tree in trees {
        if tree >= mid {
            total += (tree - mid)
        } else {
            break
        }
    }

    if total >= M {
        answer = max(answer, mid)
        left = mid + 1
    } else {
        right = mid - 1
    }
}

print(answer)

