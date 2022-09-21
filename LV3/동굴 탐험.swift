//
//  동굴 탐험.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/21.
//

import Foundation

func solution(_ n:Int, _ path:[[Int]], _ order:[[Int]]) -> Bool {
    var nodes = Array(repeating: [Int](), count: n)
    for edge in path {
        let (node1, node2) = (edge[0], edge[1])
        nodes[node1].append(node2)
        nodes[node2].append(node1)
    }
    var visited = Array(repeating: false, count: n)
    var before = [Int:Int]()
    var after = [Int:Int]()
    // check order (after - before) as dict
    var stack = [Int]()
    order.map{before[$0[1]] = $0[0]}
    
    stack.append(0)
    // start
    while !stack.isEmpty {
        guard let curNode = stack.popLast() else { continue }
        
        if let nextNode = before[curNode], !visited[nextNode] {
            // curNode -> nextNode, unvisited at this moment
            after[nextNode] = curNode
            continue
        }
        visited[curNode] = true
        for nextNode in nodes[curNode] {
            // if not visited yet, append at stack
            if !visited[nextNode] {
                stack.append(nextNode)
            }
        }
        
        guard let beforeNode = after[curNode] else { continue }
        // if latter node, back to before one
        stack.append(beforeNode)
    }
    
    for check in visited {
        if !check {
            return false
        }
    }
    // check all of nodes visited or not
    return true
}
