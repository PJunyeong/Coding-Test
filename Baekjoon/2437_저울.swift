//
//  2437_저울.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/16.
//

import Foundation

let N = Int(String(readLine()!))!
var numbers = Array(readLine()!.split(separator: " ").map{Int(String($0))!})
numbers.sort(by: <)
var sum = 0

for number in numbers {
    if sum + 1 >= number {
        sum += number
        // 누적값 sum에 1을 추가한 값보다 주어진 저울 무게가 작다면 측정 가능
        // number는 로컬 최솟값. 누적값으로 잴 수 있다면 계속해서 카운트한다.
    } else {
        break
    }
}

print(sum + 1)
