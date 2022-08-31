//
//  최댓값과 최솟값.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/31.
//

func solution(_ s:String) -> String {
    let numbers = s.split(separator: " ").map{Int(String($0))!}
    let max = numbers.max()!
    let min = numbers.min()!
    return "\(min) \(max)"
}
