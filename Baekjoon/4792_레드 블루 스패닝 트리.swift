//
//  4792_레드 블루 스패닝 트리.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/23.
//

import Foundation

while true{
    let input = readLine()!.split(separator: " ").map({Int(String($0))!})
    let (N, M, K) = (input[0], input[1], input[2])
    if N == 0 && M == 0 && K == 0{
        break
    }
    var redPQ = [(Int, Int, Int, String)]()
    var bluePQ = [(Int, Int, Int, String)]()
    for _ in 0..<M{
        let input = readLine()!.split(separator: " ")
        let color = String(input[0])
        let node1 = Int(String(input[1]))!
        let node2 = Int(String(input[2]))!
        if color == "R" {
            redPQ.append((0, node1, node2, "R"))
            bluePQ.append((1, node1, node2, "R"))
        } else {
            redPQ.append((1, node1, node2, "B"))
            bluePQ.append((0, node1, node2, "B"))
        }
    }
    redPQ.sort(by: {$0.0 < $1.0})
    bluePQ.sort(by: {$0.0 < $1.0})
    
    var parents = [Int]()
    for i in 0..<N+1{
        parents.append(i)
    }
    let minBlueCnt = Kruskal(pq:redPQ)
    parents = [Int]()
    for i in 0..<N+1{
        parents.append(i)
    }
    let maxBlueCnt = Kruskal(pq:bluePQ)
    if minBlueCnt <= K && K <= maxBlueCnt{
        print(1)
    } else{
        print(0)
    }
    
    func find(node:Int) -> Int{
        if parents[node] == node{
            return node
        } else{
            parents[node] = find(node:parents[node])
            return parents[node]
        }
    }
    
    func union(node1:Int, node2:Int) -> Bool{
        let root1 = find(node:node1)
        let root2 = find(node:node2)
        if root1 == root2{
            return false
        } else{
            parents[root2] = root1
            return true
        }
    }
    
    func Kruskal(pq: [(Int, Int, Int, String)]) -> Int{
        var blueCnt = 0
        var edgeCnt = 0
        for curData in pq{
            let _ = curData.0
            let node1 = curData.1
            let node2 = curData.2
            let color = curData.3
            if union(node1: node1, node2: node2) == true{
                if color == "B"{
                    blueCnt += 1
                }
                edgeCnt += 1
                if edgeCnt == N-1{
                    return blueCnt
                }
            }
        }
        return -1
    }
}


