//
//  옹알이 (2).swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/30.
//

import Foundation

func solution(_ babbling:[String]) -> Int {
    var answer = 0
    for babble in babbling {
        if isSpeakable(word: babble) {
            answer += 1
        }
    }
    
    return answer
}

enum Words: String, CaseIterable {
    case aya
    case ye
    case woo
    case ma
    
    var arrayString: [String] {
        return rawValue.map({String($0)})
    }
}

func isSpeakable(word: String) -> Bool {
    var word = word.map({String($0)})
    var currentWord: Words?
    while !word.isEmpty {
        guard let letter = word.first else { break }
        switch letter {
        case "a":
            if word.count >= 3 && word[0..<3].map({$0}) == Words.aya.arrayString && currentWord != .aya {
                for _ in 0..<3 {
                    word.removeFirst()
                }
                currentWord = .aya
            } else {
                return false
            }
        case "y":
            if word.count >= 2 && word[0..<2].map({$0}) == Words.ye.arrayString && currentWord != .ye {
                for _ in 0..<2 {
                    word.removeFirst()
                }
                currentWord = .ye
            } else {
                return false
            }
        case "w":
            if word.count >= 3 && word[0..<3].map({$0}) == Words.woo.arrayString && currentWord != .woo {
                for _ in 0..<3 {
                    word.removeFirst()
                }
                currentWord = .woo
            } else {
                return false
            }
        case "m":
            if word.count >= 2 && word[0..<2].map({$0}) == Words.ma.arrayString && currentWord != .ma {
                for _ in 0..<2 {
                    word.removeFirst()
                }
                currentWord = .ma
            } else {
                return false
            }
        default: return false
        }
    }
    return true
}
