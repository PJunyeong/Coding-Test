//
//  9375_패션왕 신해빈.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/22.
//

import Foundation

let clothCount = Int(String(readLine()!))!
var clothDict = [String:[String]]()
var answer = 1

for _ in 0..<clothCount {
    clothDict = [:]
    let N = Int(String(readLine()!))!
    for _ in 0..<N {
        let input = readLine()!.split(separator: " ").map{String($0)}
        let (name, cloth) = (input[0], input[1])
        var clothes = clothDict[cloth] ?? []
        clothes.append(name)
        clothDict[cloth] = clothes
    }
    
    answer = 1

    for key in clothDict.keys {
        let count = clothDict[key]!.count + 1
        answer *= count
    }

    print(answer - 1)
}

