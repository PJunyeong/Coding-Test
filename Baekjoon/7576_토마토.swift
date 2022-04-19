//
//  7576_토마토.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/19.
//

import Foundation

struct Queue<T: Equatable> {
    var enqueue: [T] = []
    var dequeue: [T] = []
    
    init() {}
    
    init(_ queue: [T]) {
        enqueue = queue
    }
    
    mutating func push(_ element: T) {
        enqueue.append(element)
    }
    
    mutating func pop() -> T? {
        if dequeue.isEmpty {
            dequeue = enqueue.reversed()
            enqueue.removeAll()
        }
        return dequeue.popLast()
    }
    
    mutating func remove() {
        enqueue.removeAll()
        dequeue.removeAll()
    }
    
    var isEmpty: Bool {
        return enqueue.isEmpty && dequeue.isEmpty
    }
    
    var firstIndex: T? {
        if dequeue.isEmpty {
            return enqueue.first
        } else {
            return dequeue.last
        }
    }
    
    var lastIndex: T? {
        if enqueue.isEmpty {
            return dequeue.first
        } else {
            return enqueue.last
        }
    }
    
    var count: Int {
        return enqueue.count + dequeue.count
    }
    
    func contains(_ element: T) -> Bool {
        return enqueue.contains(element) || dequeue.contains(element)
    }
}

let input = readLine()!.split(separator:" ").map{Int(String($0))!}
let (M, N) = (input[0], input[1])
let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]
var nodes: [[Int]] = Array(repeating: [], count: N)
for i in 0..<N{
    let line = readLine()!.split(separator:" ").map{Int(String($0))!}
    nodes[i] = line
//  인접 행렬 구현
}

var startNodes:[[Int]] = []
for i in 0..<N{
    for j in 0..<M{
        if nodes[i][j] == 1{
            startNodes.append([i, j, 0])
        }
    }
}

var answer = BFS(startNodes:startNodes)

for i in 0..<N{
    if nodes[i].contains(0){
        answer = -1
        break
    }
}

print(answer)


func BFS(startNodes:[[Int]]) -> Int{
    var queue: Queue = Queue(startNodes)
    var total = 0
    while queue.isEmpty == false{
        let input = queue.pop()!
//      removeAtFirst를 사용하며 시간 초과 -> 배열 두 개를 통한 큐 구현
        let (curRow, curCol, curCnt) = (input[0], input[1], input[2])
        total = max(total, curCnt)
        
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
                continue
            }
            
            if nodes[nextRow][nextCol] == 0{
                nodes[nextRow][nextCol] = 1
                queue.push([nextRow, nextCol, curCnt+1])
            }
        }
    }
    return total
}

