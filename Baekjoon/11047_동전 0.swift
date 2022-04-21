//
//  11047_동전 0.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/21.
//

import Foundation

let input = readLine()!.split(separator: " ").map{Int(String($0))!}
var (N, K) = (input[0], input[1])
var coins:[Int] = []
for _ in 0..<N{
    let coin = Int(readLine()!)!
    if coin > K{
        continue
    } else {
        coins.append(coin)
    }
}
coins.sort(by:>)
// 내림차순 정렬
var cnt = 0

while K != 0{
    let coin = coins.removeFirst()
    let q = K/coin
    let r = K%coin
    cnt += q
    K = r
//  현 시점 가장 큰 동전으로 값을 계산할 수 있는 한 계산하자.
}
print(cnt)

