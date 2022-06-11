//
//  거리두기 확인하기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/11.
//

import Foundation

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]

func solution(_ places:[[String]]) -> [Int] {
    var result = [Int]()
    for place in places {
        result.append(BFS(place:place))
    }
    return result
}

func BFS(place: [String]) -> Int {
    var nodes = [[String]]()
    for p in place {
        let line = Array(p.map{String($0)})
        nodes.append(line)
    }
    
    let people = getInfo(nodes: nodes)
    
    for person in people {
        let (row, col) = (person.0, person.1)
        var queue = [(Int, Int, Int)]()
        queue.append((row, col, 0))
        var index = 0
        var visited = Array(repeating: Array(repeating: false, count: 5), count: 5)
        visited[row][col] = true
        
        while queue.count > index {
            let curData = queue[index]
            let curRow = curData.0
            let curCol = curData.1
            let curCost = curData.2
            
            for idx in 0..<4 {
                let nextRow = curRow + dy[idx]
                let nextCol = curCol + dx[idx]
                
                if nextRow < 0 || nextCol < 0 || nextRow >= 5 || nextCol >= 5 {
                    continue
                }
                
                if nodes[nextRow][nextCol] != "X" && visited[nextRow][nextCol] == false {
                    
                    if nodes[nextRow][nextCol] == "P" && curCost + 1 <= 2 {
                        return 0
                    }
                    
                    visited[nextRow][nextCol] = true
                    queue.append((nextRow, nextCol, curCost + 1))
                }
            }
            index += 1
        }
    }
    return 1
}

func getInfo(nodes: [[String]]) -> [(Int, Int)] {
    var people = [(Int, Int)]()
    
    for i in 0..<nodes.count {
        let line = nodes[i]
        for j in 0..<line.count {
            if nodes[i][j] == "P" {
                people.append((i, j))
            }
        }
    }
    return people
}
