//
//  호텔 방 배정.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/20.
//

import Foundation

func solution(_ k:Int64, _ room_number:[Int64]) -> [Int64] {
    var result = [Int64]()
    var rooms = [Int64:Int64]()
    
    func find(node: Int64) -> Int64 {
        guard let value = rooms[node] else {
            rooms[node] = node + 1
            return node
        }
        let room = find(node: value)
        rooms[node] = room + 1
        return room
    }
    
    for requested in room_number {
        let room = find(node: requested)
        result.append(room)
    }
    return result
}
