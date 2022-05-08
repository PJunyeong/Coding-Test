//
//  8980_택배.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/08.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
let (N, C) = (input[0], input[1])
let M = Int(readLine()!)!
var pq = [(Int, Int, Int)]()

for _ in 0..<M{
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (start, end, weight) = (input[0], input[1], input[2])
    pq.append((end, start, weight))
}
pq.sort(by: <)
// 빨리 도착하는 택배 순서대로 오름차순
var box = Array(repeating: 0, count: N+1)
var total = 0

for data in pq{
    let end = data.0
    let start = data.1
    let weight = data.2
    var boxWeight = 0
    let boxMax:Int = box[start...end].max()!
//  boxMax는 가장 빨리 도착하는 택배 순서대로 확인했을 때 이동 범위 내애 있는 가장 무거운 택배 무게
    
    if boxMax + weight <= C{
        boxWeight = weight
//        트럭에 실을 수 있을 때: 모두 싣기 가능
    } else{
        boxWeight = C - boxMax
    }
//        트럭에 실을 수 없을 때: 최대 용량 C에서 가장 무거운 boxMax를 뺀 값을 싣는다.
    for i in start..<end{
        box[i] += boxWeight
//        boxWeight는 지금 시점에 start~end까지 싣고 갈 택배의 무게. 각 지점마다 용량을 계산할 수 있도록 넣어준다.
    }
    total += boxWeight
//        싣고 가는 용량의 총합
}

print(total)
