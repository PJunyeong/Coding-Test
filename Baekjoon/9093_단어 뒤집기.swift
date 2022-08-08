//
//  9093_단어 뒤집기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/08.
//

import Foundation

let T = Int(String(readLine()!))!
for _ in 0..<T {
    let sentence = Array(readLine()!.split(separator: " ")).map{String($0)}
    makeReverseSentence(sentence: sentence)
    
}

func makeReverseSentence(sentence: [String]) {
    for word in sentence {
        let wordArray = Array(word).map{String($0)}
        let reversedWord = wordArray.reversed().joined()
        print(reversedWord, terminator: " ")
    }
}
