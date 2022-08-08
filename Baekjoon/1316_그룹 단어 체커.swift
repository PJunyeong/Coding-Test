//
//  1316_그룹 단어 체커.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/08.
//

import Foundation

let N = Int(String(readLine()!))!
var words = [String]()
var total = 0
for _ in 0..<N {
    let word = String(readLine()!)
    if isGroupWord(word: word) {
        total += 1
    }
}

print(total)

func isGroupWord(word: String) -> Bool {
    var wordDict = [String:Int]()
    // 해당 알파벳 -> word 내 최근 인덱스 값
    let wordArray = Array(word).map{String($0)}
    for idx in 0..<wordArray.count {
        let letter = wordArray[idx]
        let letterCnt = wordDict[letter] ?? -1
        if letterCnt == -1 {
            wordDict[letter] = idx
        } else {
            if idx - letterCnt == 1 {
                wordDict[letter] = idx
            } else {
                return false
            }
        }
    }
    return true
}




