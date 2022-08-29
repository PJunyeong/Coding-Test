//
//  15965_K번째 소수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/29.
//

import Foundation

let K = Int(String(readLine()!))!
var boxes = Array(repeating: true, count: 10_000_000)
boxes[0] = false
boxes[1] = false
for idx in 2..<boxes.count {
    if boxes[idx] {
        if idx * 2 < boxes.count {
            for idx2 in stride(from: idx * 2, to: boxes.count, by: idx) {
                boxes[idx2] = false
            }
        }
    }
}

let filteredBoxes = boxes.enumerated().filter{$0.element}.map{$0.offset}
print(filteredBoxes[K-1])
