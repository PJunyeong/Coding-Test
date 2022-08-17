//
//  실패율.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/17.
//

import Foundation

func solution(_ N:Int, _ stages:[Int]) -> [Int] {
    var nodes = Array(repeating: 0, count: N + 1)
    var people = stages.count
    var results = [(Double, Int)]()
    for stage in stages {
        let stage = stage - 1
        nodes[stage] += 1
    }
    nodes = [0] + nodes
    
    for idx in 0..<nodes.count {
        let node = nodes[idx]
        let percent = Double(node) / Double(people)
        results.append((percent, idx))
        people -= node
    }
    results.removeFirst()
    results.removeLast()
    results.sort(by: {$0.0 > $1.0})
    let answers = results.map{$0.1}
    
    return answers
}
