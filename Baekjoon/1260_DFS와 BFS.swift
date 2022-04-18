//
//  main.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/18.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int($0)!}
let (N, M, V) = (input[0], input[1], input[2])
var nodes: [[Int]] = Array(repeating: [], count: N+1)
var edge: [Int]
var node1: Int
var node2: Int
for _ in 0..<M {
    edge = readLine()!.split(separator: " ").map{Int($0)!}
    node1 = edge[0]
    node2 = edge[1]
    nodes[node1].append(node2)
    nodes[node2].append(node1)
//  양방향 그래프 연결
}

for curNode in 1..<N+1{
    nodes[curNode].sort(by:<)
}



var visitedDFS:[Bool] = Array(repeating: false, count: N+1)
DFS(start:V)
print()
BFS()
func DFS(start:Int) -> Void{
    print(start, terminator: " ")
    visitedDFS[start] = true
    
    for nextNode in nodes[start]{
        if visitedDFS[nextNode] == false{
            DFS(start: nextNode)
        }
    }
}

func BFS() -> Void{
    var visitedBFS:[Bool] = Array(repeating: false, count: N+1)
    var queue: [Int] = [V]
    visitedBFS[V] = true
    while queue.isEmpty == false{
        let curNode = queue.removeFirst()
        print(curNode, terminator: " ")
        
        for nextNode in nodes[curNode]{
            if visitedBFS[nextNode] == false{
                visitedBFS[nextNode] = true
                queue.append(nextNode)
            }
        }
    }
}
