//
//  2992_크면서 작은 수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/07.
//

import Foundation

let number = String(readLine()!)
let numCnt = number.count
let numberArray = Array(number).map{String($0)}
var check = Array(repeating: false, count: number.count)
let INF = Int.max
var answer = INF

func DFS(cnt: Int, num: [String]) -> Void {
    if cnt == numCnt {
        let num = num.joined()
        if num > number && Int(num)! <= answer {
            answer = Int(num)!
        }
        return
    }
    
    for idx in 0..<numCnt {
        if !check[idx] {
            check[idx] = true
            DFS(cnt: cnt + 1, num: num + [numberArray[idx]])
            check[idx] = false
        }
    }
}

DFS(cnt: 0, num: [])

if answer == INF {
    print(0)
} else {
    print(answer)
}
