//
//  등산코스 정하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/03.
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
    
    func leftChild(from parentIndex: Int) -> Int {
        return parentIndex * 2 + 1
    }
    
    func rightChild(from parentIndex: Int) -> Int {
        return parentIndex * 2 + 2
    }
    
    func parentIndex(from child: Int) -> Int {
        return (child - 1) / 2
    }
    
    mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = leftChild(from: parent)
            let right = rightChild(from: parent)
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
    
    mutating func siftUp(from index: Int) {
        var child = index
        var parent = parentIndex(from: child)
        while child > 0 && sort(nodes[child], nodes[parent]) {
            nodes.swapAt(child, parent)
            child = parent
            parent = parentIndex(from: child)
        }
    }
    
    mutating func pop() -> T? {
        guard !isEmpty else { return nil }
        nodes.swapAt(0, count-1)
        defer {
            siftUp(from: 0)
        }
        return nodes.removeLast()
    }
    
    mutating func push(_ element: T) {
        nodes.append(element)
        siftUp(from: count - 1)
    }
}

func solution(_ n:Int, _ paths:[[Int]], _ gates:[Int], _ summits:[Int]) -> [Int] {
    var nodes = Array(repeating: [(Int, Int)](), count: n+1)
    let summitsSet = Set(summits)
    for path in paths {
        let (node1, node2, cost) = (path[0], path[1], path[2])
        nodes[node1].append((node2, cost))
        nodes[node2].append((node1, cost))
    }
    
    func Dijkstra() -> [Int] {
        var pq = PQ<(Int, Int)>(sort: {$0.0 < $1.0})
        let INF = Int.max
        var distances = Array(repeating: INF, count: n+1)
        for gate in gates {
            pq.push((0, gate))
            distances[gate] = 0
        }
        
        while !pq.isEmpty {
            guard let curData = pq.pop() else { break }
            let curCost = curData.0
            let curNode = curData.1
            
            if summitsSet.contains(curNode) || distances[curNode] < curCost {
                continue
            }
            
            for nextData in nodes[curNode] {
                let nextNode = nextData.0
                let nextCost = nextData.1
                
                let totalCost = max(curCost, nextCost)
                if distances[nextNode] > totalCost {
                    distances[nextNode] = totalCost
                    pq.push((totalCost, nextNode))
                }
            }
        }
        return distances
    }
    let distances = Dijkstra()
    let answer = summits.map{[$0, distances[$0]]}.min { node1, node2 in
        if node1[1] < node2[1] {
            return true
        } else if node1[1] == node2[1] {
            return node1[0] <= node2[0]
        } else {
            return false
        }
    }!
    
    return answer
}

let n = 7
let paths = [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]]
let gates = [1]
let summits = [2, 3, 4]

solution(n, paths, gates, summits)
