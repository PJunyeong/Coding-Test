//
//  JadenCase 문자열 만들기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/01.
//

func solution(_ s:String) -> String {
    var answer = ""
    var tmp = ""
    for letter in s {
        var letter = String(letter)
        if letter == " " {
            answer += tmp
            tmp = ""
            answer += letter
        } else {
            if tmp == "" {
                tmp += letter.uppercased()
            } else {
                tmp += letter.lowercased()
            }
        }
    }
    answer += tmp
    return answer
}
