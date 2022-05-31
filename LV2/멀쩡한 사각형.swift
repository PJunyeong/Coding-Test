//
//  멀쩡한 사각형.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/31.
//

import Foundation

func solution(_ w:Int, _ h:Int) -> Int64{
    var answer:Int64 = 0
    let w = Int64(w)
    let h = Int64(h)
    
    func getGCD(A:Int64, B: Int64) -> Int64{
        if B == 0 {
            return A
        } else {
            return getGCD(A: B, B: A % B)
        }
    }
    
    answer = w * h - (w + h) - getGCD(A: w, B: h)
    return answer
}
