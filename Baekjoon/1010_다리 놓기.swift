//
//  1010_다리 놓기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/06/27.
//

import Foundation

let T = Int(String(readLine()!))!

for _ in 0..<T {
    let input = readLine()!.split(separator: " ").map{Int(String($0))!}
    let (M, N) = (input[0], input[1])
    var numDict1:[Int:Int] = [:]
    var numDict2:[Int:Int] = [:]
    
    for i in (M+1)..<(N+1) {
        numCheck(number: i, dict: true)
    }
    
    for j in 1..<(N-M+1) {
        numCheck(number: j, dict: false)
    }
        
    func numCheck(number: Int, dict: Bool) -> Void {
        var i = 2
        var number = number
        while true {
            if number == 1 {
                break
            }

            if number % i != 0 {
                i = i + 1
            }else {
                //i로 나눠질때
                if dict {
                    let check = numDict1[i] ?? 0
                    numDict1[i] = check + 1
                } else {
                    let check = numDict2[i] ?? 0
                    numDict2[i] = check + 1
                }
                number = number / i
                if number == 1 {
                    break
                }
            }
        }
    }
    
    for key1 in numDict1.keys {
        let value1 = numDict1[key1]!
        let value2 = numDict2[key1] ?? 0
        if value2 == 0 {
            continue
        } else if value1 >= value2 {
            numDict1[key1] = value1 - value2
            numDict2[key1] = 0
        } else {
            numDict1[key1] = 0
            numDict2[key1] = value2 - value1
        }
    }
    
    var first = 1
    for key in numDict1.keys {
        let value = numDict1[key] ?? 0
        if value == 0 {
            continue
        }
        var result = 1
        for _ in 0..<value {
            result *= key
        }
        first *= result
    }
    var second = 1
    for key in numDict2.keys {
        let value = numDict2[key] ?? 0
        if value == 0 {
            continue
        }
        var result = 1
        for _ in 0..<value {
            result *= key
        }
        second *= result
    }
    
    print(first/second)
}
