//
//  괄호 변환.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/11.
//

import Foundation

func solution(_ p:String) -> String {
    if p.isEmpty || isRight(p) {
        return p
    }
    var u = ""
    var v = ""
    (u, v) = splitBracket(p)
    if isRight(u) {
        return u + solution(v)
    } else {
        var result = "(" + solution(v) + ")"
        let uArray = Array(u).map{String($0)}
        for idx in 1..<uArray.count-1 {
            if uArray[idx] == "(" {
                result += ")"
            } else {
                result += "("
            }
        }
        return result
    }
}

func isBalanced(_ bracket: String) -> Bool {
    let bracket = Array(bracket)
    let rightBracket = bracket.filter{$0 == "("}.count
    let leftBracket = bracket.filter{$0 == ")"}.count
    if leftBracket == rightBracket {
        return true
    } else {
        return false
    }
}

func isRight(_ bracket: String) -> Bool {
    var stack = [String]()
    let bracket = Array(bracket).map{String($0)}
    for letter in bracket {
        if letter == "(" {
            stack.append(letter)
        } else {
            if !stack.isEmpty {
                stack.removeLast()
            } else {
                return false
            }
        }
    }
    return true
}

func splitBracket(_ bracket: String) -> (String, String) {
    let bracket = Array(bracket).map{String($0)}
    var u = ""
    var v = ""
    var left = 0
    var right = 0
    
    for idx in 0..<bracket.count {
        let letter = bracket[idx]
        if letter == "(" {
            left += 1
            u += letter
        } else {
            right += 1
            u += letter
        }
        if left == right && left != 0 {
            v = bracket[idx+1..<bracket.count].joined()
            return (u, v)
        }
    }
    return (u, v)
}
