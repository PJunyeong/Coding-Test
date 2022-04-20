//
//  1753_최단경로.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/20.
//

import Foundation

struct PriorityQueue<T> {
  var array = [T]()
  let sort: (T, T) -> Bool

  init(sort: @escaping (T, T) -> Bool) {
    self.sort = sort
  }

  var isEmpty: Bool {
    return array.isEmpty
  }

  var count: Int {
    return array.count
  }

  func peek() -> T? {
    return array.first
  }

  func leftChildIndex(ofParentAt index: Int) -> Int {
    return (2 * index) + 1
  }

  func rightChildIndex(ofParentAt index: Int) -> Int {
    return (2 * index) + 2
  }

  func parentIndex(ofChildAt index: Int) -> Int {
    return (index - 1) / 2
  }

  // MARK:- remove operation
  mutating func pop() -> T? {
    guard !isEmpty else {
      return nil
    }

    array.swapAt(0, count - 1)
    defer {
      siftDown(from: 0)
    }
    return array.removeLast()
  }

  mutating func siftDown(from index: Int) {
    var parent = index
    while true {
      let left = leftChildIndex(ofParentAt: parent)
      let right = rightChildIndex(ofParentAt: parent)
      var candidate = parent

      if left < count && sort(array[left], array[candidate]) {
        candidate = left
      }
      if right < count && sort(array[right], array[candidate]) {
        candidate = right
      }
      if candidate == parent {
        return
      }
      array.swapAt(parent, candidate)
      parent = candidate
    }
  }

  // MARK:- insert operation
  mutating func push(_ element: T) {
    array.append(element)
    siftUp(from: array.count - 1)
  }

  mutating func siftUp(from index: Int) {
    var child = index
    var parent = parentIndex(ofChildAt: child)
    while child > 0 && sort(array[child], array[parent]) {
      array.swapAt(child, parent)
      child = parent
      parent = parentIndex(ofChildAt: child)
    }
  }
}

let input = readLine()!.split(separator:" ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
let K = Int(readLine()!)!
var nodes = Array(repeating: Array<(Int, Int)>(), count: N+1)
for _ in 0..<M{
    let input = readLine()!.split(separator:" ").map{Int(String($0))!}
    let (node1, node2, cost) = (input[0], input[1], input[2])
    nodes[node1].append((node2, cost))
}

Dijkstra(startNode: K)

func Dijkstra(startNode: Int) -> Void{
    let INF = Int.max
    var distances = Array(repeating: INF, count: N+1)
    distances[startNode] = 0
    var pq = PriorityQueue<(Int, Int)>(sort: {$0.0 < $1.0})
    pq.push((0, startNode))
    
    while pq.isEmpty == false{
        let curData = pq.pop()!
        let curCost = curData.0
        let curNode = curData.1
        if distances[curNode] < curCost{
            continue
        }
        
        for nextData in nodes[curNode]{
            let nextNode = nextData.0
            let nextCost = nextData.1
            if distances[nextNode] > nextCost + curCost{
                distances[nextNode] = nextCost + curCost
                pq.push((nextCost+curCost, nextNode))
            }
        }
    }
    
    for idx in 1..<distances.count{
        if distances[idx] == INF{
            print("INF")
        } else {
            print(distances[idx])
        }
    }
}
