//
//  1764_듣보잡.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/25.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var unheard = Set<String>()
var result = [String]()

for _ in 0..<N {
    let name = String(readLine()!)
    unheard.insert(name)
}

for _ in 0..<M {
    let name = String(readLine()!)
    if unheard.contains(name) {
        result.append(name)
    }
}

result.sort()
print(result.count)
for name in result {
    print(name)
}
