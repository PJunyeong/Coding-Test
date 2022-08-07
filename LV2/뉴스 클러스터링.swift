//
//  뉴스 클러스터링.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/07.
//

import Foundation

func solution(_ str1:String, _ str2:String) -> Int {
    let firstArray = cutLetters(string: str1)
    let secondArray = cutLetters(string: str2)
    let firstDict = getWordDict(stringArray: firstArray)
    let secondDict = getWordDict(stringArray: secondArray)
    let answer = getZakardo(firstDict, secondDict)
    return answer
}

func cutLetters(string: String) -> [String] {
    var stringArray = Array(string).map{String($0)}
    var result = [String]()
    for idx in 0..<stringArray.count-1 {
        let firstChar = Character(stringArray[idx])
        let secondChar = Character(stringArray[idx+1])
        if firstChar.isLetter && secondChar.isLetter {
            let element = stringArray[idx].lowercased() + stringArray[idx+1].lowercased()
            result.append(element)
        }
    }
    return result
}

func getWordDict(stringArray: [String]) -> [String:Int] {
    var stringDict = [String:Int]()
    for word in stringArray {
        let wordCnt = stringDict[word] ?? 0
        stringDict[word] = wordCnt + 1
    }
    return stringDict
}

func getZakardo(_ firstDict: [String:Int], _ secondDict: [String:Int]) -> Int {
    let keys = Set(firstDict.keys).union(Set(secondDict.keys))
    var intersection = 0
    var union = 0
    
    for key in keys {
        let firstValue = firstDict[key] ?? -1
        let secondValue = secondDict[key] ?? -1
        
        if firstValue != -1 && secondValue != -1 {
            intersection += min(firstValue, secondValue)
            union += max(firstValue, secondValue)
        } else if firstValue != -1 && secondValue == -1 {
            union += firstValue
        } else {
            union += secondValue
        }
    }
    
    if intersection == 0 && union == 0 {
        return 65536
    } else {
        var result = Double(intersection) / Double(union)
        result *= 65536.0
        return Int(result)
    }
}
