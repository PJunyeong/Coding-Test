//
//  2606_바이러스.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/19.
//

import Foundation
let N:Int = Int(readLine()!)!
let M:Int = Int(readLine()!)!
var nodes: [[Int]] = Array(repeating: [], count: N+1)
for _ in 0..<M{
    let input = readLine()!.split(separator:" ").map{Int(String($0))!}
    let (node1, node2) = (input[0], input[1])
    nodes[node1].append(node2)
    nodes[node2].append(node1)
//  연결 그래프 생성
}

let answer = BFS(startNode:1)
print(answer)

func BFS(startNode:Int)->Int{
    var visited = Array(repeating: false, count: N+1)
    visited[startNode] = true
    var queue = [startNode]
    var total = -1
//  원본 컴퓨터는 제외해야 한다.
    
    while queue.isEmpty == false{
        let curNode = queue.removeFirst()
        total += 1
        
        for nextNode in nodes[curNode]{
            if visited[nextNode] == false{
                visited[nextNode] = true
                queue.append(nextNode)
            }
        }
    }
    return total
}
