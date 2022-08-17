//
//  양궁대회.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/18.
//

import Foundation

func solution(_ n:Int, _ info:[Int]) -> [Int] {
    let info = Array(info.reversed())
    var scoreDiff = 0
    var lionArrows = [-1]
    
    func depthFirstSearch(_ curLionArrowCount: Int, _ curLionArrows: [Int], _ curArrowIndex: Int, _ curLionScore: Int, _ curApeachScore: Int) {
        if curArrowIndex == info.count {
            let curDiff = curLionScore - curApeachScore
            if curLionArrowCount == 0 && scoreDiff <= curDiff {
                scoreDiff = curDiff
                lionArrows = curLionArrows
            }
            return
        }
        
        for arrow in 0...curLionArrowCount {
            let nextScores: (Int, Int)
            if info[curArrowIndex] == 0 && arrow == 0 {
                nextScores = (0, 0)
            } else if info[curArrowIndex] >= arrow {
                nextScores = (0, curArrowIndex)
            } else {
                nextScores = (curArrowIndex, 0)
            }
            let nextLionScore = curLionScore + nextScores.0
            let nextApeachScore = curApeachScore + nextScores.1
            depthFirstSearch(curLionArrowCount - arrow, curLionArrows + [arrow], curArrowIndex + 1, nextLionScore, nextApeachScore)
        }
    }
    depthFirstSearch(n, [], 0, 0, 0)
    let answers = scoreDiff == 0 ? [-1] : Array(lionArrows.reversed())
    return answers
}

