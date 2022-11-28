//
//  명예의 전당 (1).swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/11/28.
//

import Foundation

struct PQ<T> {
    var nodes = [T]()
    let sort:(T, T) -> Bool
    let limitedCount: Int
    
    init(sort: @escaping (T, T) -> Bool, limitedCount: Int) {
        self.sort = sort
        self.limitedCount = limitedCount
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
    
    func rightChid(from parentIndex: Int) -> Int {
        return parentIndex * 2 + 2
    }
    
    func parentIndex(from child: Int) -> Int {
        return (child - 1) / 2
    }
    
    mutating func siftDown(from index: Int) {
        var parent = index
        while true {
            let left = leftChild(from: parent)
            let right = rightChid(from: parent)
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
            siftDown(from: 0)
        }
        return nodes.removeLast()
    }
    
    mutating func push(_ element: T) {
        nodes.append(element)
        siftUp(from: count - 1)
        while count > limitedCount {
            pop()
        }
    }
    
    func peek() -> T? {
        guard !isEmpty else { return nil }
        return nodes[0]
    }
}

func solution(_ k:Int, _ score:[Int]) -> [Int] {
    var result = [Int]()
    var pq = PQ<Int>(sort: <, limitedCount: k)
    for number in score {
        pq.push(number)
        if let curMin = pq.peek() {
            result.append(curMin)
        }
    }
    return result
}
