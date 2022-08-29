//
//  1153_네 개의 소수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/29.
//

import Foundation

var N = Int(String(readLine()!))!
var boxes = Array(repeating: true, count: N+1)
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

let prefix: [Int]
var answer = [Int]()
if N % 2 == 0 {
    N -= 4
    prefix = [2, 2]
} else {
    N -= 5
    prefix = [2, 3]
}

func depthFirstSearch(_ count: Int, _ numbers: [Int], _ sum: Int) {
    if !answer.isEmpty {
        return
    }
    
    if count == 2 {
        if sum == N && answer.isEmpty {
            answer = numbers
        }
        return
    }
    
    for idx in 0..<filteredBoxes.count {
        let number = filteredBoxes[idx]
        if number + sum <= N {
            depthFirstSearch(count + 1, numbers + [number], sum + number)
        }
    }
}

depthFirstSearch(0, [], 0)
if answer.isEmpty {
    print(-1)
} else {
    answer = prefix + answer
    for number in answer {
        print(number, terminator: " ")
    }
}
