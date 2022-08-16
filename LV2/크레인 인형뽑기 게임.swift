//
//  크레인 인형뽑기 게임.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/16.
//

import Foundation

func solution(_ board:[[Int]], _ moves:[Int]) -> Int {
    var board = board
    var total = 0
    var stack = [Int]()
    
    func getDoll(_ position: Int) -> Int? {
        let position = position - 1
        for idx in 0..<board.count {
            if board[idx][position] != 0 {
                let doll = board[idx][position]
                board[idx][position] = 0
                return doll
            }
        }
        return nil
    }
    
    for move in moves {
        guard let doll = getDoll(move) else { continue }
        if !stack.isEmpty {
            if stack.last! == doll {
                stack.removeLast()
                total += 2
            } else {
                stack.append(doll)
            }
        } else {
            stack.append(doll)
        }
    }
    
    return total
}
