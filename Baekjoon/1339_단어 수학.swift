//
//  1339_단어 수학.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/22.
//

import Foundation

let N = Int(readLine()!)!
var letterCnts:[String:Int] = [:]
for _ in 0..<N{
    let input = readLine()!.map({String($0)})
    var base = 1
    for letter in input.reversed(){
        letterCnts[letter, default:0] += 1 * base
        base *= 10
    }
}
var num = 9
var total = 0
for letterCnt in letterCnts.values.sorted(by: >){
    total += num * letterCnt
    num -= 1
}
print(total)
