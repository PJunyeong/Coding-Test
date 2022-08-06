//
//  16499_동일한 단어 그룹화하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/06.
//

import Foundation

let N = Int(String(readLine()!))!
var wordSet = Set<[String]>()
for _ in 0..<N {
    var word = Array(readLine()!).map{String($0)}
    word.sort()
    wordSet.insert(word)
}

print(wordSet.count)
