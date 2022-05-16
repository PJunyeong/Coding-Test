//
//  오픈채팅방.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/17.
//

import Foundation

func solution(_ record:[String]) -> [String] {
    var result = [(String, String)]()
    var idName = [String:String]()
    
    for rec in record {
        let input = rec.split(separator: " ").map{String($0)}
        let move = input[0]
        let userId = input[1]
        result.append((userId, move))
        // 입력받은 아이디 별 move 기록
        
        if move == "Enter" || move == "Change" {
            idName[userId] = input[2]
            // Leave 제외 모두 닉네임을 가지고 있음
        }
    }
        
    var answer = [String]()
    
    for rec in result {
        let (userId, move) = (rec.0, rec.1)
        if move == "Enter" {
            answer.append("\(idName[userId]!)님이 들어왔습니다.")
        } else if move == "Leave" {
            answer.append("\(idName[userId]!)님이 나갔습니다.")
        }
        // 마지막으로 변경된 닉네임을 딕셔너리에서 꺼내 적용
        
    }
    return answer
}


