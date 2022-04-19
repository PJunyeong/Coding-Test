//
//  14502_연구소.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/19.
//

import Foundation

let input = readLine()!.split(separator:" ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]
var nodes: [[Int]] = Array(repeating: [], count: N)
var walls: [[Int]] = []
var startNodes:[[Int]] = []
for i in 0..<N{
    let line = readLine()!.split(separator:" ").map{Int(String($0))!}
    for j in 0..<M{
        if line[j] == 2{
            startNodes.append([i, j])
        } else if line[j] == 0{
            walls.append([i, j])
        }
    }
    nodes[i] = line
//  인접 행렬 구현 및 바이러스 위치 추적
}
let wallCnt = N*M-startNodes.count-walls.count + 3
var answer = 0
for i in 0..<walls.count{
    for j in i..<walls.count{
        if i == j{
            continue
        }
        for k in j..<walls.count{
            if j == k || i == k{
                continue
            }
            var nodes = nodes
            nodes[walls[i][0]][walls[i][1]] = 1
            nodes[walls[j][0]][walls[j][1]] = 1
            nodes[walls[k][0]][walls[k][1]] = 1
            answer = max(answer, BFS(nodes:nodes))
//          벽을 세울 수 있는 조합 (i, j, k)에 벽을 세우고 BFS.
//          안전한 공간 중 최댓값 answer에 기록
        }
    }
}

print(answer)

func BFS(nodes:[[Int]]) -> Int{
    var nodes = nodes
    var queue = [(Int, Int)]()
    for start in startNodes{
        queue.append((start[0], start[1]))
    }
    
    var index = 0
    var virus = 0
    while queue.count > index{
        let input = queue[index]
//        큐 사이즈가 현재 인덱스보다 클 때 연산. 큐 기능 구현
        let (curRow, curCol) = (input.0, input.1)
        virus += 1
//      바이러스 카운트
        
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
                continue
            }
            
            if nodes[nextRow][nextCol] == 0{
                nodes[nextRow][nextCol] = 2
                queue.append((nextRow, nextCol))
            }
        }
        index += 1
    }

    let answer = N*M - virus - wallCnt
//    안전한 공간은 전체 공간 - 바이러스 - 벽 개수
    return answer
}

