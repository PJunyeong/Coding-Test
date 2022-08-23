//
//  후보키.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/23.
//

import Foundation

func solution(_ relation:[[String]]) -> Int {
    let columnCount = relation[0].count
    var candidates = [[Int]]()
    
    func depthFirstSearch(_ startIndex: Int, _ curIndices: [Int]) {
        if !curIndices.isEmpty {
            candidates.append(curIndices)
        }
        
        for idx in startIndex..<columnCount {
            depthFirstSearch(idx + 1, curIndices + [idx])
        }
    }
    depthFirstSearch(0, [])
    candidates.sort(by: {$0.count < $1.count})
    
    var candidateKeys = [[Int]]()
    let relationCount = relation.count
    for candidate in candidates {
        if !isCandidateMinimal(candidateKeys, candidate) {
            continue
        }
        
        var relationSet = Set<String>()
        for tuple in relation {
            let convertedTuple = convertTuple(tuple, candidate)
            relationSet.insert(convertedTuple)
        }
        if relationSet.count == relationCount {
            candidateKeys.append(candidate)
        }
    }
    
    return candidateKeys.count
}

func isCandidateMinimal(_ candidateKeys: [[Int]], _ candidate: [Int]) -> Bool {
    for candidateKey in candidateKeys {
        if Set(candidate).isSuperset(of: Set(candidateKey)) {
            return false
        }
    }
    return true
}

func convertTuple(_ tuple: [String], _ indices: [Int]) -> String {
    var tmp = ""
    let indices = indices.sorted(by: <)
    for index in indices {
        tmp += tuple[index]
    }
    return tmp
}
