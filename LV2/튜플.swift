//
//  튜플.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/18.
//

import Foundation

func solution(_ s:String) -> [Int] {
    var string = Array(s.map{String($0)})
    string.removeFirst()
    string.removeLast()
    // {} 제거
    var data = [[Int]]()
    
    let brackets = string.split(separator: "{")
    
    for bracket in brackets {
        var element = [Int]()
        var number = ""
        for digit in bracket {
            if Character(digit).isNumber {
                number += String(digit)
            } else {
                if !number.isEmpty {
                    element.append(Int(number)!)
                    number = ""
                }
            }
        }
        data.append(element)
    }
    
    
    var answer = [Int]()
    data.sort(by: {
        $0.count < $1.count
    })
    for element in data {
        for num in element {
            if !answer.contains(num) {
                answer.append(num)
            }
        }
    }
    return answer
}

let answer = solution("{{20,111},{111}}")
print(answer)
