//
//  3198_백조의 호수.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/27.
//

import Foundation

let input = readLine()!.split(separator: " ").map({Int(String($0))!})
let (R, C) = (input[0], input[1])
var waterVisited = Array(repeating: Array(repeating: false, count: C), count: R)
var swanVisited = Array(repeating: Array(repeating: false, count: C), count: R)

var nodes = [[String]]()
var waterQueue = [(Int, Int)]()
var nextWaterQueue = [(Int, Int)]()
var swanQueue = [(Int, Int)]()
var nextSwanQueue = [(Int, Int)]()

for i in 0..<R{
    let row = Array(readLine()!.map({(String($0))}))
    nodes.append(row)
    for j in 0..<C{
        if row[j] == "L"{
            nodes[i][j] = "."
            waterQueue.append((i, j))
            waterVisited[i][j] = true
            swanQueue.append((i, j))
        } else if row[j] == "."{
            waterQueue.append((i, j))
            waterVisited[i][j] = true
        }
    }
}

let swan1 = swanQueue.removeFirst()
let swanRow1 = swan1.0
let swanCol1 = swan1.1
let swan2 = swanQueue.removeFirst()
let swanRow2 = swan2.0
let swanCol2 = swan2.1
swanVisited[swanRow1][swanCol1] = true
swanQueue.append((swanRow1, swanCol1))

let dx = [1, -1, 0, 0]
let dy = [0, 0, 1, -1]

func swanBFS() -> Bool{
    var index = 0
    while swanQueue.count > index{
        let curData = swanQueue[index]
        let curRow = curData.0
        let curCol = curData.1
        
        if curRow == swanRow2 && curCol == swanCol2{
            return true
        }
        
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            
            if nextRow < 0 || nextCol < 0 || nextRow >= R || nextCol >= C{
                continue
            }
            
            if swanVisited[nextRow][nextCol] == false && nodes[nextRow][nextCol] == "."{
                swanQueue.append((nextRow, nextCol))
                swanVisited[nextRow][nextCol] = true
            } else if swanVisited[nextRow][nextCol] == false && nodes[nextRow][nextCol] == "X"{
                nextSwanQueue.append((nextRow, nextCol))
                swanVisited[nextRow][nextCol] = true
            }
        }
        index += 1
    }
    return false
}

func waterBFS()->Void{
    var index = 0
    while waterQueue.count > index{
        let curData = waterQueue[index]
        let curRow = curData.0
        let curCol = curData.1
        nodes[curRow][curCol] = "."
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            
            if nextRow < 0 || nextCol < 0 || nextRow >= R || nextCol >= C{
                continue
            }
            
            if waterVisited[nextRow][nextCol] == false && nodes[nextRow][nextCol] == "X"{
                nextWaterQueue.append((nextRow, nextCol))
                waterVisited[nextRow][nextCol] = true
            } else if waterVisited[nextRow][nextCol] == false && nodes[nextRow][nextCol] == "."{
                waterQueue.append((nextRow, nextCol))
                waterVisited[nextRow][nextCol] = true
            }
        }
        index += 1
    }
}

var day = 0

while true{
    waterBFS()
    if swanBFS() == true{
        break
    }
    waterQueue = nextWaterQueue
    nextWaterQueue = [(Int, Int)]()
    swanQueue = nextSwanQueue
    nextSwanQueue = [(Int, Int)]()
    day += 1
}

print(day)
