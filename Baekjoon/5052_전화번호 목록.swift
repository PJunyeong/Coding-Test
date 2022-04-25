//
//  5052_전화번호 목록.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/25.
//

import Foundation

let T = Int(readLine()!)!
for _ in 0..<T{
    let N = Int(readLine()!)!
    var nums = [String]()
    for _ in 0..<N{
        let num = String(readLine()!)
        nums.append(num)
    }
    nums.sort()
//  첫 번째 숫자 기준 정렬
    if validCheck(nums:nums) == true{
        print("YES")
    } else {
        print("NO")
    }
}

func validCheck(nums:[String])->Bool{
    for i in 0..<nums.count-1{
        if nums[i+1].hasPrefix(nums[i]){
            return false
        }
    }
    return true
}
