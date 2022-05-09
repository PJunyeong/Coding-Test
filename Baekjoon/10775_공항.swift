//
//  10775_공힝.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/09.
//

import Foundation

let G = Int(readLine()!)!
let P = Int(readLine()!)!

var parents = [Int]()
for i in 0..<G+1{
    parents.append(i)
//    i번 게이트로 들어오는 비행기는 1..i번 게이트 중 도킹 가능 (총 i번)
}
var gates = [Int]()
for _ in 0..<P{
    let g = Int(readLine()!)!
    gates.append(g)
}

var total = 0

for gate in gates{
    let root = find(node: gate)
    if root == 0{
//      도킹 가능한 게이트가 더 이상 없다는 뜻.
        break
    }
    parents[root] -= 1
//  paretns[root]는 이 비행기가 도킹 가능한 게이트의 개수
    total += 1
}

print(total)

func find(node:Int)->Int{
    if parents[node] == node{
        return node
    } else{
        parents[node] = find(node:parents[node])
        return parents[node]
    }
}
