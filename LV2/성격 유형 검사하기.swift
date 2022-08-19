//
//  성격 유형 검사하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/19.
//

import Foundation

func solution(_ survey:[String], _ choices:[Int]) -> String {
    var characterDict = ["R": (0, 0), "T": (0, 1), "C": (1, 0), "F": (1, 1), "J": (2, 0), "M": (2, 1), "A": (3, 0), "N": (3, 1)]
    var characterDictReversed = [0: ["R", "T"], 1:["C", "F"], 2:["J", "M"], 3:["A", "N"]]
    var characters = Array(repeating: (0, 0), count:4)
    for idx in 0..<survey.count {
        let s = survey[idx]
        let choice = choices[idx]
        let (disagree, agree) = (String(s.first!), String(s.last!))
        let score: Int
        let characterIdx: (Int, Int)
        let characterOrder: Int
        let characterOrder2: Int
        if choice == 4 {
            continue
        } else if choice > 4 {
            score = choice - 4
            characterIdx = characterDict[agree]!
            characterOrder = characterIdx.0
            characterOrder2 = characterIdx.1
        } else {
            score = 4 - choice
            characterIdx = characterDict[disagree]!
            characterOrder = characterIdx.0
            characterOrder2 = characterIdx.1
        }
        
        if characterOrder2 == 0 {
            characters[characterOrder].0 += score
        } else {
            characters[characterOrder].1 += score
        }
    }
    var result = ""
    for idx in 0..<4 {
        let possibleLetters = characterDictReversed[idx]!
        let (former, latter) = (possibleLetters[0], possibleLetters[1])
        let characterResult = characters[idx]
        let (formerResult, latterResult) = (characterResult.0, characterResult.1)
        if formerResult >= latterResult {
            result += former
        } else {
            result += latter
        }
    }
    
    return result
}
