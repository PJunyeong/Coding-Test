//
//  12919_A와 B 2.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/06.
//

import Foundation

let S = Array(readLine()!).map{String($0)}
let T = Array(readLine()!).map{String($0)}
let SCnt = S.count

func DFS(words: [String]) {
    if words.count == SCnt {
        if words == S {
            print(1)
            exit(0)
        }
        return
    }
    
    let lastString = words[words.count-1]
    if lastString == "A" {
        var tmp = words
        tmp.removeLast()
        DFS(words: tmp)
    }
    let firstString = words[0]
    if firstString == "B" {
        var tmp = words
        tmp.removeFirst()
        tmp.reverse()
        DFS(words: tmp)
    }
}

DFS(words: T)
print(0)


