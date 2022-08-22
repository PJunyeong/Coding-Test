//
//  1302_베스트셀러.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/22.
//

import Foundation

let N = Int(String(readLine()!))!
var bookCount = [String:Int]()
for _ in 0..<N {
    let book = String(readLine()!)
    let count = bookCount[book] ?? 0
    bookCount[book] = count + 1
}

let max = bookCount.sorted(by: {$0.value > $1.value}).first!.value
let answer = bookCount.filter{$0.value == max}.sorted(by: {$0.key < $1.key}).first!.key
print(answer)

