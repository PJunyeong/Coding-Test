//
//  파일명 정렬.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/23.
//

struct File {
    let head: String
    let number: String
    let tail: String
    let order: Int
    
    var original: String {
        return head + number + tail
    }
}

func solution(_ files:[String]) -> [String] {
    var results = [File]()
    for item in files.enumerated() {
        let index = item.offset
        let file = item.element
        let result = convertFile(file, index)
        results.append(result)
    }
    results.sort(by: { first, second in
        if first.head.lowercased() < second.head.lowercased() {
            return true
        } else if first.head.lowercased() == second.head.lowercased() {
            if Int(first.number)! < Int(second.number)! {
                return true
            } else if Int(first.number)! == Int(second.number)! {
                return first.order <= second.order
            } else {
                return false
            }
        } else {
            return false
        }
    })
    let sortedResults = results.map{$0.original}
    return sortedResults
}

func convertFile(_ file: String, _ order: Int) -> File {
    var tmp = ""
    var curPart = 0
    var head: String = ""
    var number: String = ""
    var tail: String = ""
    
    for letter in file {
        switch curPart {
            case 0:
                if !letter.isNumber {
                    tmp += String(letter)
                } else {
                    head = tmp
                    tmp = String(letter)
                    curPart += 1
                }
            case 1:
                if tmp.count < 5 {
                    if letter.isNumber {
                        tmp += String(letter)
                    } else {
                        number = tmp
                        tmp = String(letter)
                        curPart += 1
                    }
                } else {
                    number = tmp
                    tmp = String(letter)
                    curPart += 1
                }
            case 2:
                tmp += String(letter)
            default: continue
        }
    }
    if curPart == 1 {
        number = tmp
    } else {
        tail = tmp
    }
    let result = File(head: head, number: number, tail: tail, order: order)
    return result
}
