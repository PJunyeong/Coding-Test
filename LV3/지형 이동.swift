//
//  지형 이동.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/09/22.
//

import Foundation

func solution(_ land:[[Int]], _ height:Int) -> Int {
    let length = land.count
    var visited = Array(repeating: Array(repeating: -1, count: length), count: length)
    let dx = [0, 0, 1, -1]
    let dy = [1, -1, 0, 0]
    var pq = [(Int, Int, Int)]()
    // cost, node1, node2
    
    func depthFirstSearch() -> Int {
        var componentIndex = 0
        for i in 0..<length {
            for j in 0..<length {
                if visited[i][j] == -1 {
                    var queue = [(Int, Int)]()
                    var index = 0
                    visited[i][j] = componentIndex
                    queue.append((i, j))
                    while queue.count > index {
                        let curData = queue[index]
                        let curRow = curData.0
                        let curCol = curData.1
                        
                        for i in 0..<4 {
                            let nextRow = curRow + dy[i]
                            let nextCol = curCol + dx[i]
                            
                            if nextRow < 0 || nextCol < 0 || nextRow >= length || nextCol >= length {
                                continue
                            }
                            
                            if visited[nextRow][nextCol] != -1 && visited[nextRow][nextCol] != visited[curRow][curCol] && abs(land[curRow][curCol] - land[nextRow][nextCol]) > height {
                                pq.append((visited[nextRow][nextCol], visited[curRow][curCol], abs(land[curRow][curCol] - land[nextRow][nextCol])))
                            }
                            
                            if visited[nextRow][nextCol] == -1 && abs(land[curRow][curCol] - land[nextRow][nextCol]) <= height {
                                visited[nextRow][nextCol] = componentIndex
                                queue.append((nextRow, nextCol))
                            }
                        }
                        index += 1
                    }
                    componentIndex += 1
                }
            }
        }
        
        return componentIndex
    }
    
    let componentCount = depthFirstSearch()
    var parents = [Int]()
    for i in 0..<componentCount {
        parents.append(i)
    }
    
    func find(node: Int) -> Int {
        if parents[node] == node {
            return node
        } else {
            parents[node] = find(node: parents[node])
            return parents[node]
        }
    }
    
    func union(node1: Int, node2: Int) -> Bool {
        let root1 = find(node: node1)
        let root2 = find(node: node2)
        
        if root1 == root2 {
            return false
        } else {
            parents[root2] = root1
            return true
        }
    }
    
    func kruskal(pq: [(Int, Int, Int)], compoentCount: Int) -> Int {
        var pq = pq.sorted(by: {$0.2 < $1.2})
        var total = 0
        var curEdge = 0
        for data in pq {
            let node1 = data.0
            let node2 = data.1
            let cost = data.2
            
            if union(node1: node1, node2: node2) {
                total += cost
                curEdge += 1
            }
        }
        return total
    }
    
    let answer = kruskal(pq: pq, compoentCount: componentCount)
    return answer
}
