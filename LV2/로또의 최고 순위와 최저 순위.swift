//
//  로또의 최고 순위와 최저 순위.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/16.
//

import Foundation

func solution(_ lottos:[Int], _ win_nums:[Int]) -> [Int] {
    var zeroCnt = lottos.filter{$0 == 0}.count
    var intersectionCnt = Set(lottos).intersection(Set(win_nums)).count
    var (minCnt, maxCnt) = (intersectionCnt, intersectionCnt + zeroCnt)
    minCnt = minCnt == 0 ? 6 : 7 - minCnt
    maxCnt = maxCnt == 0 ? 6 : 7 - maxCnt
    return [maxCnt, minCnt]
}
