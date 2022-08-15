//
//  불량 사용자.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/15.
//

import Foundation

func solution(_ user_id:[String], _ banned_id:[String]) -> Int {
    var banLists = [[String]]()
    var banList = [String]()
    for ban in banned_id {
        banList = []
        for user in user_id {
            if isBannedId(user, ban) {
                banList.append(user)
            }
        }
        banLists.append(banList)
    }
    var banListSet = Set(banLists.flatMap{$0})
    var checked = Array(repeating: false, count: banListSet.count)
    var banDict = [String : Int]()
    var index = 0
    
    for ban in banListSet {
        banDict[ban] = index
        index += 1
    }
    
    var banListInt = [[Int]]()
    var tmp = [Int]()
    for banList in banLists {
        tmp = []
        for ban in banList {
            tmp.append(banDict[ban]!)
        }
        banListInt.append(tmp)
    }

    var totalSet = Set<String>()
    
    func DFS(_ banListIdx: Int, _ banCount: Int, _ id: [Int]) {
        if banCount == banListInt.count {
            let id = id.sorted()
            let banIdString = id.map{String($0)}.joined()
            totalSet.insert(banIdString)
            return
        }
        
        let banList = banListInt[banListIdx]
        
        for ban in banList {
            if !checked[ban] {
                checked[ban] = true
                DFS(banListIdx + 1, banCount + 1, id + [ban])
                checked[ban] = false
            }
        }
    }
    
    DFS(0, 0, [])
    
    return totalSet.count
}

func isBannedId(_ user: String, _ ban: String) -> Bool {
    if user.count != ban.count {
        return false
    }
    
    for idx in 0..<user.count {
        let userIdx = user.index(user.startIndex, offsetBy: idx)
        let userLetter = user[userIdx]
        let banIdx = ban.index(ban.startIndex, offsetBy: idx)
        let banLetter = ban[banIdx]
        
        if banLetter == "*" {
            continue
        } else if banLetter != userLetter {
            return false
        }
    }
    return true
}
