//
//  10723_판게아 1.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/04.
//

import Foundation

let T = Int(String(readLine()!))!
for _ in 0..<T {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (N, M) = (input[0], input[1])
    var pq = [(Int, Int, Int)]()
    for node1 in 1..<N {
        let input = readLine()!.split(separator: " ").map{Int(String($0))!}
        let (node2, cost) = (input[0], input[1])
        pq.append((cost, node1, node2))
    }
    var parents = Array(repeating: 0, count: N)
    var answers = [Int]()
    for _ in 0..<M {
        let input = readLine()!.split(separator: " ").map{Int(String($0))!}
        let (node1, node2, cost) = (input[0], input[1], input[2])
        pq.append((cost, node1, node2))
        pq.sort(by: {$0.0 < $1.0})
        for i in 0..<N {
            parents[i] = i
        }
        // Union-Find 위해 parents 변수 초기화
        let answer = Kruskal()
        // 새로운 간선 추가될 때마다 크루스칼 알고리즘 -> MST 비용 구하기
        answers.append(answer)
    }
    
    var answer = answers[0]
    for idx in 1..<answers.count {
        answer = answer^answers[idx]
        // 추가된 간선마다 구해놓은 MST 비용을 통해 전체 XOR 값
    }
    
    print(answer)
    
    func find(node: Int) -> Int {
        if parents[node] == node {
            return node
        } else {
            parents[node] = find(node: parents[node])
            return parents[node]
        }
    }
    
    func union(node1: Int, node2: Int) -> Bool {
        let root1 = find(node: node1)
        let root2 = find(node: node2)
        
        if root1 == root2 {
            return false
        } else {
            parents[root2] = root1
            return true
        }
    }
    
    func Kruskal() -> Int {
        var total = 0
        var edgeCnt = 0
        
        for data in pq {
            let cost = data.0
            let node1 = data.1
            let node2 = data.2
            
            if union(node1:node1, node2: node2) == true {
                total += cost
                edgeCnt += 1
                if edgeCnt == N-1 {
                    return total
                }
            }
        }
        return -1
    }
}
