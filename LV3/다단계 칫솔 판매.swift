//
//  다단계 칫솔 판매.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/14.
//

import Foundation

func solution(_ enroll:[String], _ referral:[String], _ seller:[String], _ amount:[Int]) -> [Int] {
    var nameDict = [String: Int]()
    nameDict["-"] = 0
    let peopleCnt = enroll.count + 1
    var nodes = Array(repeating: 0, count: peopleCnt)
    var moneys = Array(repeating: 0, count: peopleCnt)

    for idx in 1..<enroll.count+1 {
        let name = enroll[idx-1]
        nameDict[name] = idx
        let refer = referral[idx-1]
        let referIdx = nameDict[refer] ?? 0
        nodes[idx] = referIdx
    }
    
    func BFS(_ start: String, _ money: Int) {
        var curIdx = nameDict[start]!
        var curMoney = money
        
        while curIdx != 0 && curMoney > 0 {
            let nextIdx = nodes[curIdx]
            let yourMoney = Int(Double(curMoney) * 0.1)
            moneys[curIdx] += curMoney - yourMoney
            curMoney = yourMoney
            curIdx = nextIdx
        }
    }
    
    for idx in 0..<seller.count {
        let sellerName = seller[idx]
        let money = amount[idx] * 100
        BFS(sellerName, money)
    }
    
    moneys.removeFirst()
    return moneys
}
