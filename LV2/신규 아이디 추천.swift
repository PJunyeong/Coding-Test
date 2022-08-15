//
//  신규 아이디 추천.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/15.
//

import Foundation

func solution(_ new_id:String) -> String {
    let newId = makeNewId(new_id)
    return newId
}

func makeNewId(_ id: String) -> String {
    var id = id.lowercased()
    var tmp = ""
    for letter in id {
        if letter.isLetter || letter.isNumber || letter == "-" || letter == "_" || letter == "." {
            tmp += String(letter)
        }
    }
    id = tmp
    var idArray = Array(id).map{String($0)}
    var tmpIdx = -2
    var dotIndices = [Int]()
    for idx in 0..<idArray.count {
        let letter = idArray[idx]
        if letter == "." {
            if idx - tmpIdx == 1 {
                dotIndices.append(idx)
            }
            tmpIdx = idx
        }
    }
    tmpIdx = 0
    for idx in dotIndices {
        idArray.remove(at: idx - tmpIdx)
        tmpIdx += 1
    }
    if let first = idArray.first, first == "." {
        idArray.removeFirst()
    }
    if let last = idArray.last, last == "." {
        idArray.removeLast()
    }
    if idArray.isEmpty {
        idArray.append("a")
    }
    if idArray.count >= 16 {
        idArray = Array(idArray[0..<15])
    }
    if let last = idArray.last, last == "." {
        idArray.removeLast()
    }
    if idArray.count <= 2 {
        let lastString = idArray.last!
        while idArray.count != 3 {
            idArray.append(lastString)
        }
    }
    let newId = idArray.joined()
    return newId
}
