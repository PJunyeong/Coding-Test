//
//  2644_촌수계산.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/07/11.
//

import Foundation

let N = Int(String(readLine()!))!
let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (person1, person2) = (input[0], input[1])
let M = Int(String(readLine()!))!
var nodes = Array(repeating: [Int](), count: N+1)

for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (parent, child) = (input[0], input[1])
    nodes[parent].append(child)
    nodes[child].append(parent)
}

func BFS(start: Int, goal: Int) -> Int {
    var queue = [(Int, Int)]()
    var visited = Array(repeating: false, count: N+1)
    queue.append((start, 0))
    visited[start] = true
    var index = 0
    
    while queue.count > index {
        let curData = queue[index]
        let curNode = curData.0
        let curCost = curData.1
        
        if curNode == goal {
            return curCost
        }
        
        for nextNode in nodes[curNode] {
            if !visited[nextNode] {
                visited[nextNode] = true
                queue.append((nextNode, curCost + 1))
            }
        }
        index += 1
    }
    return -1
}

let goal = BFS(start: person1, goal: person2)

print(goal)
