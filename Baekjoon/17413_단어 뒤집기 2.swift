//
//  17413_단어 뒤집기 2.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/08.
//

import Foundation

let sentence = Array(readLine()!).map{String($0)}
var result = ""
var stack = [String]()
var isTag = false

for letter in sentence {
    if letter == "<" {
        if !stack.isEmpty {
            let reversedWord = stack.reversed()
            result += reversedWord.joined()
            stack.removeAll()
        }
        isTag = true
        result += letter
    } else if letter == ">" {
        result += letter
        isTag = false
    } else {
        if isTag {
            result += letter
        } else {
            if letter == " " {
                let reversedWord = stack.reversed()
                result += reversedWord.joined()
                result += letter
                stack.removeAll()
            } else {
                stack.append(letter)
            }
        }
    }
}

if !stack.isEmpty {
    let reversedWord = stack.reversed()
    result += reversedWord.joined()
    stack.removeAll()
}

print(result)
