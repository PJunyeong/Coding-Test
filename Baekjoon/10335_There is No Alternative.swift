//
//  10335_There is No Alternative.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/02.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var pq = [(Int, Int, Int)]()
// [(cost, node1, node2)]

for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (node1, node2, cost) = (input[0], input[1], input[2])
    pq.append((cost, node1, node2))
}

pq.sort(by:{$0.0 < $1.0})
// cost 오름차순
var pq2 = pq
var parents = Array(repeating: 0, count: N+1)
for i in 0..<N+1 {
    parents[i] = i
}


func find(node: Int) -> Int {
    if parents[node] == node {
        return node
    } else {
        parents[node] = find(node: parents[node])
        return parents[node]
    }
}

func union(node1:Int, node2: Int) -> Bool {
    let root1 = find(node: node1)
    let root2 = find(node: node2)
    
    if root1 == root2 {
        return false
    } else {
        parents[root2] = root1
        return true
    }
}

func Kruskal(MSTCheck: Bool) -> ([(Int, Int, Int)], Int) {
    if MSTCheck == true {
        var total = 0
        var edgeCnt = 0
        var edges = [(Int, Int, Int)]()
        for edge in pq2 {
            let cost = edge.0
            let node1 = edge.1
            let node2 = edge.2
            
            if union(node1: node1, node2: node2) == true {
                total += cost
                edges.append(edge)
                edgeCnt += 1
                if edgeCnt == N-1 {
                    break
                }
            }
        }
        if edgeCnt == N-1 {
            return (edges, total)
        } else {
            return (edges, -1)
        }
        // 원본 간선 -> MST 구성 간선 정보 및 비용 리턴
    } else {
        var total = 0
        var edgeCnt = 0
        for edge in pq2 {
            let cost = edge.0
            let node1 = edge.1
            let node2 = edge.2
            if union(node1: node1, node2: node2) == true {
                total += cost
                edgeCnt += 1
                if edgeCnt == N-1 {
                    break
                }
            }
        }
        if edgeCnt == N-1 {
            return ([], total)
        } else {
            return ([], -1)
        }
        // MST 구성 간선 중 특정 간선을 제외한 전체 간선으로 만든 MST 비용 리턴
    }
}

let (MSTEdges, total) = Kruskal(MSTCheck: true)
var noAlternativeCnt = 0
var noAlternativeCost = 0

for edge in MSTEdges {
    for i in 0..<N+1 {
        parents[i] = i
    }
    pq2 = pq
    // pq2를 계속 사용하기 위해 복제 (값 복사)
    for i in 0..<pq2.count {
        let data = pq2[i]
        if data == edge {
            pq2.remove(at:i)
            break
        }
    } // edge와 같은 인덱스를 찾아 pq2에서 미리 제거
    let (_, total2) = Kruskal(MSTCheck:false)
    if total2 != total {
        // 다르다면 MST의 대체 간선이 없다는 뜻이므로 no alternative edge.
        noAlternativeCnt += 1
        noAlternativeCost += edge.0
    }
}

print(noAlternativeCnt, noAlternativeCost)

