//
//  16234_인구 이동.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/25.
//

import Foundation

let input = readLine()!.split(separator: " ").map({Int(String($0))!})
let (N, L, R) = (input[0], input[1], input[2])
var nodes = [[Int]]()
for _ in 0..<N{
    let row = readLine()!.split(separator: " ").map({Int(String($0))!})
    nodes.append(Array(row))
}
let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]
var day = 0
while true{
    var fedralDict:[Int:[(Int, Int)]] = [:]
    var fedralCnt = 1
    var visited = Array(repeating: Array(repeating: false, count: N), count: N)
    for i in 0..<N{
        for j in 0..<N{
//            방문하지 않은 국가에서 시작, BFS를 통해 인구 이동 가능한 연합 구성
            if visited[i][j] == false{
                var queue = [(Int, Int)]()
                queue.append((i, j))
                visited[i][j] = true
                var index = 0
                while queue.count > index{
                    let curData = queue[index]
                    let curRow = curData.0
                    let curCol = curData.1
                    let curCost = nodes[curRow][curCol]
                    fedralDict[fedralCnt, default: []].append(curData)
                    
                    for i in 0..<4{
                        let nextRow = curRow + dy[i]
                        let nextCol = curCol + dx[i]
                        if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= N{
                            continue
                        }
                        let nextCost = nodes[nextRow][nextCol]
                        if visited[nextRow][nextCol] == false && L <= abs(curCost-nextCost) && abs(curCost-nextCost) <= R{
                            visited[nextRow][nextCol] = true
                            queue.append((nextRow, nextCol))
                        }
                    }
                    index += 1
//                  fedralCnt번째 연합 구성 완료
                }
                fedralCnt += 1
            }
        }
    }
    var isFedralPossible = false
    for fedralCnt in fedralDict.keys{
        let fedralNum = fedralDict[fedralCnt]!.count
        if fedralNum == 1{
            continue
//          연합 X
        }
        isFedralPossible = true
        var fedralPeople = 0
        for fedralNation in fedralDict[fedralCnt]!{
            let curRow = fedralNation.0
            let curCol = fedralNation.1
            fedralPeople += nodes[curRow][curCol]
//          연합 구성 국가의 총 인구 수 합
        }
        let fedralAvg = fedralPeople / fedralNum
        for fedralNation in fedralDict[fedralCnt]!{
            let curRow = fedralNation.0
            let curCol = fedralNation.1
            nodes[curRow][curCol] = fedralAvg
//          평균으로 분배
        }
    }
    if isFedralPossible == false{
        break
//          인구 이동 일어나지 않을 때 종료
    }
    day += 1
}

print(day)
