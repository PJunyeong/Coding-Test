//
//  순위.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/12.
//

import Foundation

func solution(_ n:Int, _ results:[[Int]]) -> Int {
    var nodes = Array(repeating: [Int](), count: n+1)
    var nodesReverse = Array(repeating: [Int](), count: n+1)
    for result in results {
        let (parent, child) = (result[0], result[1])
        nodes[parent].append(child)
        nodesReverse[child].append(parent)
    }
    
    var nodesCnt = Array(repeating: 0, count: n+1)
    
    for idx in 1..<n+1 {
        var queue = [Int]()
        var visited = Array(repeating: false, count: n+1)
        queue.append(idx)
        visited[idx] = true
        var index = 0
        var total = 0
        
        while queue.count > index {
            let curNode = queue[index]
            
            for nextNode in nodes[curNode] {
                if !visited[nextNode] {
                    visited[nextNode] = true
                    queue.append(nextNode)
                    total += 1
                }
            }
            index += 1
        }
        
        queue = [idx]
        visited = Array(repeating: false, count: n+1)
        visited[idx] = true
        index = 0
        
        while queue.count > index {
            let curNode = queue[index]
            
            for nextNode in nodesReverse[curNode] {
                if !visited[nextNode] {
                    visited[nextNode] = true
                    queue.append(nextNode)
                    total += 1
                }
            }
            index += 1
        }
        
        nodesCnt[idx] = total + 1
    }
    
    let answer = nodesCnt.filter{$0 == n}.count
    return answer
}
