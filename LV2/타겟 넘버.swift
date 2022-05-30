//
//  타겟 넘버.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/30.
//

import Foundation

func solution(_ numbers: [Int], _ target: Int) -> Int {
    var answer = 0
    var queue = [(Int, Int)]()
    queue.append((numbers[0], 0))
    queue.append((-1 * numbers[0], 0))
    var index = 0
    let numberCnt = numbers.count
    
    while queue.count > index {
        let curData = queue[index]
        let curNum = curData.0
        let curIdx = curData.1
        
        let nextIdx = curIdx + 1
        
        if nextIdx < numberCnt {
            queue.append((curNum + numbers[nextIdx], nextIdx))
            queue.append((curNum - numbers[nextIdx], nextIdx))
        } else {
            if curNum == target {
                answer += 1
            }
        }
        index += 1
    }
    return answer
}

let answer = solution([1, 1, 1, 1, 1], 3)
print(answer)

