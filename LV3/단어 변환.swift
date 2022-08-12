//
//  단어 변환.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/12.
//

import Foundation

func solution(_ begin:String, _ target:String, _ words:[String]) -> Int {
    var wordBag = Set<String>()
    var queue = [(String, Int)]()
    queue.append((begin, 0))
    wordBag.insert(begin)
    var index = 0
    
    while queue.count > index {
        let curData = queue[index]
        let curWord = curData.0
        let curCnt = curData.1
        
        if curWord == target {
            return curCnt
        }
        
        for word in words {
            if !wordBag.contains(word) && isChangable(curWord, word) {
                wordBag.insert(word)
                queue.append((word, curCnt + 1))
            }
        }
        
        index += 1
    }
    
    
    return 0
}

func isChangable(_ word1: String, _ word2: String) -> Bool {
    if word1.count != word2.count {
        return false
    }
    var sameLetterCnt = 0
    for idx in 0..<word1.count {
        let letter1 = word1[word1.index(word1.startIndex, offsetBy: idx)]
        let letter2 = word2[word2.index(word2.startIndex, offsetBy: idx)]
        if letter1 == letter2 {
            sameLetterCnt += 1
        }
    }
    
    if sameLetterCnt == word1.count - 1 {
        return true
    } else {
        return false
    }
}
