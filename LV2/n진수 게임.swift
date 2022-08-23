//
//  n진수 게임.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/23.
//

func solution(_ n:Int, _ t:Int, _ m:Int, _ p:Int) -> String {
    var curCount = 0
    var answer = ""
    var numbersList = getNumbers(to: t * m, with: n)
    for idx in stride(from: p-1, to: numbersList.count, by: m) {
        answer += numbersList[idx]
        curCount += 1
        if curCount == t || idx + m >= numbersList.count {
            break
        }
    }
    return answer
}

func getNumbers(to number: Int, with k: Int) -> [String] {
    var result = ["0"]
    for num in 1...number {
        let convertedNumber = convertNumber(num, k)
        result += convertedNumber
    }
    return result
}

func convertNumber(_ number: Int, _ k: Int) -> [String] {
    let numberDict = [10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"]
    var number = number
    var tmp = [String]()
    
    while number > 0 {
        let q = number / k
        let r = number % k
        number = q
        if let r = numberDict[r] {
            tmp.append(r)
        } else {
            tmp.append(String(r))
        }
    }
    
    let convertedNumber = Array(tmp.reversed())
    return convertedNumber
}
