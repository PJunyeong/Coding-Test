//
//  추석 트래픽.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/14.
//

import Foundation

func solution(_ lines:[String]) -> Int {
    var records = [(Int, Int)]()
    for line in lines {
        let line = line.split(separator: " ").map{String($0)}
        let S = line[1]
        var T = line[2]
        T.removeLast()
        let replyTime = convertTime(S)
        let taskTime = Int(Double(T)! * 1000.0)
        
        let end = replyTime
        let start = replyTime - taskTime + 1
        let record = (start, end)
        records.append(record)
    }
    
    var maxCount = 0
    
    for record in records {
        let start = record.0
        let end = record.1
        
        let startCount = getCount(start, records)
        let endCount = getCount(end, records)
        maxCount = max(maxCount, startCount, endCount)
    }
    return maxCount
}

func getCount(_ point: Int, _ records: [(Int, Int)]) -> Int {
    var count = 0
    for record in records {
        let start = record.0
        let end = record.1
        if start < point + 1000 && point <= end {
            count += 1
        }
    }
    return count
}

func convertTime(_ time: String) -> Int {
    let time = time.split(separator: ":")
    var times:Double = 3600000.0
    var total:Double = 0.0
    
    for t in time {
        total += times * Double(t)!
        times /= 60.0
    }
    return Int(total)
}
