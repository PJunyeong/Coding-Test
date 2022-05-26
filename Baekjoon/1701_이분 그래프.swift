//
//  1701_이분 그래프.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/27.
//

import Foundation

let K = Int(String(readLine()!))!
var nodes:[[Int]] = [[]]
var flag:Bool = true
var visited:[Bool] = []
var colors:[Int] = []
for _ in 0..<K {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (V, E) = (input[0], input[1])
    nodes = Array(repeating: [Int](), count: V+1)
    for _ in 0..<E {
        let input = readLine()!.split(separator: " ").map{Int(String($0))!}
        let (U, V) = (input[0], input[1])
        nodes[U].append(V)
        nodes[V].append(U)
    }
    
    
    flag = true
    visited = Array(repeating: false, count: V+1)
    colors = Array(repeating: -1, count: V+1)
    
    for i in 1...V {
        if visited[i] == false {
            DFS(node:i, color:1)
        }
        if flag == false {
            break
        }
    }
    
    if flag == true {
        print("YES")
    } else {
        print("NO")
    }
}

func DFS(node:Int, color:Int) -> Void {
    visited[node] = true
    colors[node] = color
    
    for nextNode in nodes[node] {
        if visited[nextNode] == false {
            DFS(node:nextNode, color: abs(1-color))
        } else {
            if colors[nextNode] == color {
                flag = false
            }
        }
    }
}
