//
//  압축.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/23.
//

import Foundation

func solution(_ msg:String) -> [Int] {
    var wordDict = initWordDict()
    var result = [Int]()
    let letters = Array(msg).map{String($0)}
    
    func getZip() {
        var curOffset = -1
        for idx in 0..<letters.count {
            if curOffset >= idx {
                continue
            }
            var length = 1
            var word = ""
            for curLength in 1...letters.count-idx {
                let curWord = letters[idx..<idx+curLength].joined()
                if wordDict[curWord] == nil {
                    break
                } else {
                    length = curLength
                    word = curWord
                }
            }
            curOffset = idx + length - 1
            result.append(wordDict[word]!)
            print(word, wordDict[word]!, curOffset, idx)
            if idx + length < letters.count {
                let newWord = word + letters[idx+length]
                wordDict[newWord] = wordDict.count + 1
            }
        }
    }
    getZip()

    return result
}

func initWordDict() -> [String: Int] {
    let alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    var wordDict = [String:Int]()
    var letterIndex = 1
    for letter in alphabets {
        let letter = String(letter)
        wordDict[letter] = letterIndex
        letterIndex += 1
    }
    return wordDict
}
