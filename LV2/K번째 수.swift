//
//  K번째 수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/16.
//

import Foundation

func solution(_ array:[Int], _ commands:[[Int]]) -> [Int] {
    var answers = [Int]()
    for command in commands {
        let (i, j, k) = (command[0]-1, command[1]-1, command[2]-1)
        let splitedArray = Array(array[i...j]).sorted()
        let answer = splitedArray[k]
        answers.append(answer)
    }
    return answers
}
