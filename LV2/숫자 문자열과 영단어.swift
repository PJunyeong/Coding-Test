//
//  숫자 문자열과 영단어.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/15.
//

import Foundation

func solution(_ s:String) -> Int {
    let numberDict = ["zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"]
    var answer = ""
    let s = Array(s).map{String($0)}
    
    func DFS(_ startIdx: Int, _ endIdx: Int) {
        if startIdx == s.count {
            return
        }
        
        if startIdx == endIdx && Character(s[startIdx]).isNumber {
            answer += s[startIdx]
            DFS(endIdx + 1, endIdx + 1)
        } else {
            let possibleWord = s[startIdx...endIdx].joined()
            if let number = numberDict[possibleWord] {
                answer += number
                DFS(endIdx + 1, endIdx + 1)
            } else {
                DFS(startIdx, endIdx + 1)
            }
        }
    }
    
    DFS(0, 0)
    return Int(answer)!
}

