//
//  19949_영재의 시험.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/11.
//

import Foundation

let answers = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
var check = Array(repeating: false, count: answers.count)
var answerCnt = 0

func DFS(cnt: Int, score: Int, answer: [Int]) -> Void {
    if cnt == answers.count {
        if score >= 5 {
            answerCnt += 1
        }
        return
    }
    
    var flag = false
    
    if answer.count >= 2 {
        let lastIdx = answer.count - 1
        let lastFirst = answer[lastIdx]
        let lastSecond = answer[lastIdx-1]
        if lastFirst == lastSecond {
            flag = true
        }
    }
    
    let newAnswer = answer.isEmpty ? [] : [answer[answer.count-1]]
    for ans in 1..<6 {
        
        if flag && answer[answer.count-1] == ans {
            continue
        }
        
        let nextScore = ans == answers[cnt] ? score + 1 : score
        DFS(cnt: cnt + 1, score: nextScore, answer: newAnswer + [ans])
    }
}

DFS(cnt: 0, score: 0, answer: [])
print(answerCnt)


