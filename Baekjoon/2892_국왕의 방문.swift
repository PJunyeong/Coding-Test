//
//  2892_국왕의 방문.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/05.
//

import Foundation

struct PQ<T> {
    var nodes = [T]()
    let sort:(T, T) -> Bool
    init(sort:@escaping(T, T) -> Bool) {
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
    mutating func shiftDown(from index: Int) {
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
    mutating func shiftUp(from index: Int) {
        var child = index
        var parent = parentIndex(from: child)
        while child > 0 && sort(nodes[child], nodes[parent]) {
            nodes.swapAt(child, parent)
            child = parent
            parent = parentIndex(from: child)
        }
    }
    mutating func pop() -> T? {
        guard !isEmpty else { return nil}
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

let INF = Int.max
var input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var nodes = Array(repeating: [(Int, Int)](), count: N+1)
input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (A, B, K, G) = (input[0], input[1], input[2], input[3])
let intersections = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
var intersectionDict = [Int:Int]()
var intersectionIdx = 0
for intersection in intersections {
    intersectionDict[intersection] = intersectionIdx
    intersectionIdx += 1
}
var intersectionTimes = Array(repeating: 0, count: G-1)
for _ in 0..<M {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (node1, node2, cost) = (input[0], input[1], input[2])
    nodes[node1].append((node2, cost))
    nodes[node2].append((node1, cost))
    if let idx1 = intersectionDict[node1], let idx2 = intersectionDict[node2], abs(idx1-idx2) == 1 {
        if idx1 < idx2 {
            intersectionTimes[idx1] = cost
        } else {
            intersectionTimes[idx2] = cost
        }
    }
}

for i in 1..<G-1 {
    intersectionTimes[i] += intersectionTimes[i-1]
}

let distances = Dijkstra(start: A, K: K)
let answer = distances[B] - K
print(answer)

func getIntersectionData(curCost: Int) -> (Int, Int, Int) {
    for i in 0..<G-1 {
        if curCost < intersectionTimes[i] {
            return (intersections[i], intersections[i+1], intersectionTimes[i])
        }
    }
    return (-1, -1, -1)
}

func Dijkstra(start: Int, K: Int) -> [Int] {
    var distances = Array(repeating: INF, count: N+1)
    distances[start] = K
    var pq = PQ<(Int, Int)>(sort: {$0.0 < $1.0})
    pq.push((K, start))
    
    while !pq.isEmpty {
        guard let curData = pq.pop() else { break }
        let curCost = curData.0
        let curNode = curData.1
        
        if distances[curNode] < curCost {
            continue
        }
        
        let intersectionData = getIntersectionData(curCost: curCost)
        let interNode1 = intersectionData.0
        let interNode2 = intersectionData.1
        let interCost = intersectionData.2
        
        for nextData in nodes[curNode] {
            let nextNode = nextData.0
            let nextCost = nextData.1
            
            var waitCost = 0
            if (interNode1 == curNode && interNode2 == nextNode) || (interNode1 == nextNode && interNode2 == curNode) {
                waitCost = interCost - curCost
            }
            let totalCost = waitCost + curCost + nextCost
            
            if distances[nextNode] > totalCost {
                distances[nextNode] = totalCost
                pq.push((totalCost, nextNode))
            }
        }
    }
    return distances
}
