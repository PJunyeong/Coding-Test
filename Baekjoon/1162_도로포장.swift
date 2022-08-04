//
//  1162_도로포장.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/04.
//

import Foundation

struct PQ<T> {
    var nodes = [T]()
    let sort:(T, T) -> Bool
    init(sort: @escaping (T, T) -> Bool) {
        self.sort = sort
    }
    
    var isEmpty: Bool {
        return nodes.isEmpty
    }
    var count: Int {
        return nodes.count
    }
    func leftChild(of parentIndex: Int) -> Int {
        return parentIndex * 2 + 1
    }
    func rightChild(of parentIndex: Int) -> Int {
        return parentIndex * 2 + 2
    }
    func parentIndex(of childIndex: Int) -> Int {
        return (childIndex - 1) / 2
    }
    mutating func shiftDown(from index: Int) {
        var parent = index
        while true {
            let left = leftChild(of: parent)
            let right = rightChild(of: parent)
            var candidate = parent
            if left < count && sort(nodes[left], nodes[candidate]) {
                candidate = left
            }
            if right < count && sort(nodes[right], nodes[candidate]) {
                candidate = right
            }
            if candidate == parent {
                return
            }
            nodes.swapAt(parent, candidate)
            parent = candidate
        }
        
    }
    mutating func shiftUp(from index: Int) {
        var child = index
        var parent = parentIndex(of: child)
        while child > 0 && sort(nodes[child], nodes[parent]) {
            nodes.swapAt(child, parent)
            child = parent
            parent = parentIndex(of: child)
        }
        
    }
    mutating func pop() -> T? {
        guard !isEmpty else { return nil }
        nodes.swapAt(0, count-1)
        defer {
            shiftDown(from: 0)
        }
        return nodes.removeLast()
    }
    mutating func push(_ element: T) {
        nodes.append(element)
        shiftUp(from: count-1)
    }
}

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M, K) = (input[0], input[1], input[2])
var nodes = Array(repeating: [(Int, Int)](), count: N+1)
let INF = Int.max

for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (node1, node2, cost) = (input[0], input[1], input[2])
    nodes[node1].append((node2, cost))
    nodes[node2].append((node1, cost))
}

let distances = Dijkstra(start: 1)
if let answer = distances[N].min() {
    print(answer)
}



func Dijkstra(start: Int) -> [[Int]] {
    var distances = Array(repeating: Array(repeating: INF, count: K+1), count: N+1)
    distances[start][0] = 0
    var pq = PQ<(Int, Int, Int)>(sort: {$0.0 < $1.0})
    pq.push((0, start, 0))
    
    while !pq.isEmpty {
        guard let curData = pq.pop() else { break }
        
        let curCost = curData.0
        let curNode = curData.1
        let curNum = curData.2
        if distances[curNode][curNum] < curCost {
            continue
        }
        
        for nextData in nodes[curNode] {
            let nextNode = nextData.0
            let nextCost = nextData.1
            if distances[nextNode][curNum] > nextCost + curCost {
                distances[nextNode][curNum] = nextCost + curCost
                pq.push((nextCost + curCost, nextNode, curNum))
            }
            // 포장 도로를 설치하지 않을 때
            if curNum < K {
                if distances[nextNode][curNum+1] > curCost {
                    distances[nextNode][curNum+1] = curCost
                    pq.push((curCost, nextNode, curNum + 1))
                }
            }
            // 포장 도로 설치 가능 + 이득이 있을 때
        }
    }
    return distances
}
