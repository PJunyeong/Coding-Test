//
//  1504_특정한 최단 경로.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/04.
//

import Foundation

struct PQ<T> {
    var nodes = [T]()
    let sort: (T, T) -> Bool
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
    mutating func pop() -> T? {
        guard !isEmpty else { return nil }
        nodes.swapAt(0, count-1)
        defer {
            shiftDown(from: 0)
        }
        return nodes.removeLast()
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
    mutating func push(_ element: T) {
        nodes.append(element)
        shiftUp(from: count-1)
    }
}

let INF = Int.max
let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var nodes = Array(repeating: [(Int, Int)](), count: N+1)
for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (a, b, c) = (input[0], input[1], input[2])
    nodes[a].append((b, c))
    nodes[b].append((a, c))
}
let input2 = readLine()!.split(separator: " ").map{Int(String($0))!}
let (nodeNum1, nodeNum2) = (input2[0], input2[1])
let zeroDist = Dijkstra(start: 1)
let firstDist = Dijkstra(start: nodeNum1)
let secondDist = Dijkstra(start: nodeNum2)

var answerNums = [Int]()
if zeroDist[nodeNum1] == INF || firstDist[nodeNum2] == INF || secondDist[N] == INF {
    
} else {
    answerNums.append(zeroDist[nodeNum1] + firstDist[nodeNum2] + secondDist[N])
}

if zeroDist[nodeNum2] == INF || secondDist[nodeNum1] == INF || firstDist[N] == INF {
    
} else {
    answerNums.append(zeroDist[nodeNum2] + firstDist[N] + secondDist[nodeNum1])
}

if answerNums.isEmpty {
    print(-1)
} else {
    if let minAnswer = answerNums.min() {
        print(minAnswer)
    }
}
func Dijkstra(start: Int) -> [Int] {
    var distances = Array(repeating: INF, count: N+1)
    distances[start] = 0
    var pq = PQ<(Int, Int)>(sort: {$0.0 < $1.0})
    pq.push((0, start))
    
    while !pq.isEmpty {
        guard let curData = pq.pop() else { break }
        let curCost = curData.0
        let curNode = curData.1
        if distances[curNode] < curCost {
            continue
        }
        
        for nextData in nodes[curNode] {
            let nextNode = nextData.0
            let nextCost = nextData.1
            
            let totalCost = curCost + nextCost
            if distances[nextNode] > totalCost {
                distances[nextNode] = totalCost
                pq.push((totalCost, nextNode))
            }
        }
    }
    return distances
}
