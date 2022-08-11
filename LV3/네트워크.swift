//
//  네트워크.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/11.
//

import Foundation

func solution(_ n:Int, _ computers:[[Int]]) -> Int {
    var nodes = Array(repeating: [Int](), count: n)
    var checked = [Int]()
    for i in 0..<n {
        checked.append(i)
    }
    
    for i in 0..<n {
        for j in i+1..<n {
            if i == j {
                continue
            } else if computers[i][j] == 1 {
                nodes[i].append(j)
                nodes[j].append(i)
            }
        }
    }
    
    var total = 0
    
    while !checked.isEmpty {
        let startNode = checked.removeFirst()
        var queue = [Int]()
        queue.append(startNode)
        var index = 0
        
        while queue.count > index {
            let curNode = queue[index]
            
            for nextNode in nodes[curNode] {
                if checked.contains(nextNode) {
                    queue.append(nextNode)
                    let checkedIdx = checked.firstIndex(of: nextNode)!
                    checked.remove(at: checkedIdx)
                }
            }
            index += 1
        }
        total += 1
    }
    return total
}
