//
//  24524_아름다운 문자열.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/15.
//

import Foundation

let S = Array(String(readLine()!))
let T = Array(String(readLine()!))
var Tbox = Array(repeating: 0, count: T.count)
var cnt = 0

for i in 0..<S.count {
    for j in 0..<T.count {
        if S[i] == T[j] {
            if j == 0 {
                Tbox[j] += 1
            } else if Tbox[j-1] > Tbox[j] {
                Tbox[j] += 1
            }
        }
    }
}

print(Tbox[T.count-1])
