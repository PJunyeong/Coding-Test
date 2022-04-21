//
//  1931_회의실 배정.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/21.
//

import Foundation

let N = Int(readLine()!)!
var meetings = [(Int, Int)]()
for _ in 0..<N{
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (start, end) = (input[0], input[1])
    meetings.append((start, end))
}
meetings.sort { (a: (Int,Int), b :(Int,Int)) -> Bool in
    if a.1 == b.1 { return a.0 < b.0
    } else { return a.1 < b.1 } }
var curStart = -1
var curEnd = -1
var cnt = 0
for curMeeting in meetings{
    let (start, end) = (curMeeting.0, curMeeting.1)
    if curEnd <= start{
        curEnd = end
        cnt += 1
//      다음 회의가 시작하는 시간보다 현재 진행 중 회의가 빨리 끝난다면 시작 가능
//      다음 회의가 끝나는 시간 keep
    }
}

print(cnt)


