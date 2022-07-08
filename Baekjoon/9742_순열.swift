//
//  9742_순열.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/08.
//

import Foundation

while let input = readLine() {

    let output1 = String(input)
    let line = input.split(separator: " ")
    var word = Array(String(line[0])).map{String($0)}
    word.sort()
    let wordCnt = word.count
    let order = Int(String(line[1]))!
    var check = Array(repeating: false, count: wordCnt)
    var flag = false
    var cnt = 0
    
    func DFS(letters: [String]) -> Void {
        if letters.count == wordCnt {
            cnt += 1
            if cnt == order {
                flag = true
                let permutation = letters.joined()
                let output = output1 + " = " + permutation
                print(output)
            }
        }
        
        for idx in 0..<wordCnt {
            if !check[idx] {
                check[idx] = true
                DFS(letters: letters + [word[idx]])
                check[idx] = false
            }
        }
    }
    
    DFS(letters: [])
    if !flag {
        let output = output1 + " = " + "No permutation"
        print(output)
    }
}
    

