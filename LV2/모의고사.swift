//
//  모의고사.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/16.
//

import Foundation

func solution(_ answers:[Int]) -> [Int] {
    let methods = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    var scores = [(Int, Int)]()
    for student in 1..<4 {
        let score = (0, student)
        scores.append(score)
    }
    
    for idx in 0..<answers.count {
        let answer = answers[idx]
        for student in 0..<3 {
            let studentIdx = idx % methods[student].count
            let studentAnswer = methods[student][studentIdx]
            if studentAnswer == answer {
                scores[student].0 += 1
            }
        }
    }
    
    let maxScore = scores.map{$0.0}.max()!
    let firstScores = scores.filter{$0.0 == maxScore}.map{$0.1}
    
    return firstScores
}
