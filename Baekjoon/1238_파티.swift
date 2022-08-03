//
//  1238_파티.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/03.
//

import Foundation

struct PriorityQueue<T> {
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
    func peek() -> T? {
        return nodes.first
    }
    func leftChildIndex(ofParentAt index: Int) -> Int {
        return 2 * index + 1
    }
    func rightChildIndex(ofParentAt index: Int) -> Int {
        return 2 * index + 2
    }
    func parentIndex(ofChildAt index: Int) -> Int {
        return (index - 1) / 2
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
            let left = leftChildIndex(ofParentAt: parent)
            let right = rightChildIndex(ofParentAt: parent)
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
    mutating func push(_ element: T) {
        nodes.append(element)
        shiftUp(from: nodes.count - 1)
    }
    mutating func shiftUp(from index: Int) {
        var child = index
        var parent = parentIndex(ofChildAt: child)
        while child > 0 && sort(nodes[child], nodes[parent]) {
            nodes.swapAt(child, parent)
            child = parent
            parent = parentIndex(ofChildAt: child)
        }
    }
}


let INF = Int.max
let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M, X) = (input[0], input[1], input[2])
var nodes = Array(repeating: [(Int, Int)](), count: N+1)
for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (start, end, cost) = (input[0], input[1], input[2])
    nodes[start].append((cost, end))
}

func Dijkstra(start: Int) -> [Int] {
    var distances = Array(repeating: INF, count: N+1)
    distances[start] = 0
    var pq = PriorityQueue<(Int, Int)>(sort: {$0.0 < $1.0})
    pq.push((0, start))
    
    while !pq.isEmpty {
        guard let curData = pq.pop() else { break }
        let curCost = curData.0
        let curNode = curData.1
        
        if distances[curNode] < curCost {
            continue
        }
        
        for nextData in nodes[curNode] {
            let nextCost = nextData.0
            let nextNode = nextData.1
            
            let totalCost = curCost + nextCost
            
            if distances[nextNode] > totalCost {
                distances[nextNode] = totalCost
                pq.push((totalCost, nextNode))
            }
        }
    }
    return distances
}

var distancesX = Dijkstra(start: X)

for idx in 1..<N+1 {
    if idx == X {
        continue
    }
    let distances = Dijkstra(start: idx)
    distancesX[idx] += distances[X]
}

if let answer = distancesX[1...].max() {
    print(answer)
}
