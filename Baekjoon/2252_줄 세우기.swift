//
//  2252_줄 세우기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/29.
//

import Foundation

let input = readLine()!.split(separator: " ").map({Int(String($0))!})
let (N, M) = (input[0], input[1])
var nodes = Array(repeating: [Int](), count: N+1)
var inDegree = Array(repeating: 0, count: N+1)

for _ in 0..<M{
    let input = readLine()!.split(separator: " ").map({Int(String($0))!})
    let (A, B) = (input[0], input[1])
    nodes[B].append(A)
    inDegree[A] += 1
}


var queue = [Int]()
for i in 1..<N+1{
    if inDegree[i] == 0{
        queue.append(i)
    }
}

var index = 0
var result = [Int]()
while queue.count > index{
    let curNode = queue[index]
    result.append(curNode)
    
    for nextNode in nodes[curNode]{
        inDegree[nextNode] -= 1
        if inDegree[nextNode] == 0{
            queue.append(nextNode)
        }
    }
    index += 1
}

result.reverse()
for height in result{
    print(height, terminator: " ")
}

