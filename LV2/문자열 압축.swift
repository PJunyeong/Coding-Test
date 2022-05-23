//
//  문자열 압축.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/23.
//

import Foundation

func solution(_ s:String) -> Int {
    var minAnswer = Int.max
    if s.count == 1 {
        return 1
        // 압축할 필요 X
    }
    
    let str = Array(s)
    
    
    for i in 1..<str.count / 2 + 1{
        // 최대 압축 절반 가능
        var result = ""
        var cnt = 1
        var sPrefix = str[0..<i]
        // i번까지의 문자열 -> prefix
        for j in stride(from: i, to: str.count, by: i) {
            // i에서 시작, prefix가 몇 개 있는지 카운트
            if sPrefix == str[j..<(i+j < str.count ? i+j : str.count)] {
                // count를 넘기면 인덱스 에러가 뜨기 때문에 체크
                cnt += 1
            } else {
                // prefix가 더 이상 일치하지 않는다면 prefix를 바꿔준다.
                // 지금까지 prefix 개수를 result에 입력해두기
                if cnt != 1 {
                    result += String(cnt) + sPrefix
                    // 두 개 이상 존재한다면 몇 개 존재하는지 숫자로 표현
                } else {
                    result += sPrefix
                    // 한 번만 존재한다면 1을 붙이지 않는다
                }
                sPrefix = str[j..<(i+j < str.count ? i+j : str.count)]
                cnt = 1
                // prefix 및 prefix가 나온 개수 cnt 초기화
            }
        }
        if cnt != 1 {
            result += String(cnt) + sPrefix
        } else {
            result += sPrefix
        }
        // for문 끝난 뒤 남아 있는 prefix 카운트 반영
        minAnswer = min(minAnswer, result.count)
    }
    return minAnswer
}
