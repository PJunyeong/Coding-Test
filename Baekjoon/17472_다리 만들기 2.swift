//
//  17472_다리 만들기 2.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/22.
//

import Foundation

let dx = [0, 0, 1, -1]
let dy = [1, -1, 0, 0]
let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, M) = (input[0], input[1])
var nodes = [[Int]]()
for _ in 0..<N{
    let line = readLine()!.split(separator: " ").map{Int(String($0))!}
    nodes.append(line)
}
var islands = [[(Int, Int)]]()
var num = 2
for i in 0..<N{
    for j in 0..<M{
        if nodes[i][j] == 1{
            let island = BFS(curRow:i, curCol:j, num:num)
            islands.append(island)
            num += 1
        }
    }
}

var pq = [(Int, Int, Int)]()
var edgeCheck = Array(repeating: Array(repeating: false, count: islands.count+2), count: islands.count+2)
var nodeNum = 2
for island in islands{
    makeEdge(startNodes:island, nodeNum:nodeNum)
    nodeNum += 1
}
pq.sort(by: {$0.0 < $1.0})
var parents:[Int] = []
for i in 0..<(islands.count + 2){
    parents.append(i)
}
let answer = Kruskal()
print(answer)

func BFS(curRow:Int, curCol:Int, num:Int)-> [(Int, Int)]{
    var queue = [(Int, Int)]()
    queue.append((curRow, curCol))
    nodes[curRow][curCol] = num
    var index = 0
    while queue.count > index{
        let curRow = queue[index].0
        let curCol = queue[index].1
        
        for i in 0..<4{
            let nextRow = curRow + dy[i]
            let nextCol = curCol + dx[i]
            if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
                continue
            }
            if nodes[nextRow][nextCol] == 1{
                nodes[nextRow][nextCol] = num
                queue.append((nextRow, nextCol))
            }
        }
        index += 1
    }
    return queue
}

func makeEdge(startNodes:[(Int, Int)], nodeNum:Int)->Void{
    var queue = [(Int, Int, Int, Int)]()
    for startNode in startNodes{
        queue.append((startNode.0, startNode.1, 0, 0))
        queue.append((startNode.0, startNode.1, 1, 0))
        queue.append((startNode.0, startNode.1, 2, 0))
        queue.append((startNode.0, startNode.1, 3, 0))
    }
    let node1 = nodeNum
    edgeCheck[node1][node1] = true
    while queue.isEmpty == false{
        let curData = queue.removeFirst()
        let curRow = curData.0
        let curCol = curData.1
        let curDir = curData.2
        let curCost = curData.3
        let nextRow = curRow + dy[curDir]
        let nextCol = curCol + dx[curDir]
        if nextRow < 0 || nextCol < 0 || nextRow >= N || nextCol >= M{
            continue
        }
            
        if nodes[nextRow][nextCol] == 0{
            queue.append((nextRow, nextCol, curDir, curCost+1))
        } else if nodes[nextRow][nextCol] != node1 && nodes[nextRow][nextCol] > 1 && edgeCheck[node1][nodes[nextRow][nextCol]] == false && curCost > 1{
            let node2 = nodes[nextRow][nextCol]
            edgeCheck[node1][node2] = true
            edgeCheck[node2][node1] = true
            pq.append((curCost, node1, node2))
        }
    }
}


func find(node:Int)->Int{
    if parents[node] == node{
        return node
    } else {
        parents[node] = find(node:parents[node])
        return parents[node]
    }
}

func union(node1: Int, node2: Int) -> Bool{
    let root1 = find(node:node1)
    let root2 = find(node:node2)
    if root1 == root2{
        return false
    } else {
        parents[root2] = root1
        return true
    }
}

func Kruskal() -> Int{
    var total = 0
    var edgeCnt = 0
    for curData in pq{
        let curCost = curData.0
        let node1 = curData.1
        let node2 = curData.2
        if union(node1: node1, node2: node2){
            total += curCost
            edgeCnt += 1
            if edgeCnt == islands.count-1{
                return total
            }
        }
    }
    return -1
}
