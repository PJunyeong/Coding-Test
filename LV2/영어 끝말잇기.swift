//
//  영어 끝말잇기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/13.
//

import Foundation

func solution(_ n:Int, _ words:[String]) -> [Int] {
    var wordSet = Set<String>()
    var wordDict = [Int:Int]()
    var lastCharacter = words[0].first
    for idx in 0..<words.count {
        let word = words[idx]
        let peopleOrder = idx % n + 1
        let peopleCount = wordDict[peopleOrder] ?? 0
        
        if lastCharacter == word.first {
            lastCharacter = word.last
        } else {
            return [peopleOrder, peopleCount + 1]
        }
        
        if !wordSet.contains(word) {
            wordSet.insert(word)
        } else {
            return [peopleOrder, peopleCount + 1]
        }
        
        wordDict[peopleOrder] = peopleCount + 1
    }
    return [0, 0]
}
