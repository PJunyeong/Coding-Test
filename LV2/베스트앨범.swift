//
//  베스트앨범.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/14.
//

import Foundation

func solution(_ genres:[String], _ plays:[Int]) -> [Int] {
    var genreDict = [String:[(Int, Int)]]()
    for idx in 0..<genres.count {
        let genre = genres[idx]
        let play = plays[idx]
        var genreValue = genreDict[genre] ?? []
        genreValue.append((play, idx))
        genreDict[genre] = genreValue
    }
    var values = Array(genreDict.values)
    values.sort(by: {$0.map{$0.0}.reduce(0, +) > $1.map{$0.0}.reduce(0, +)})
    var result = [Int]()
    for value in values {
        let value = value.sorted(by: {$0.0 > $1.0})
        let indices = value.map{$0.1}
        if indices.count < 2 {
            result += indices
        } else {
            result += indices[0..<2]
        }
    }
    return result
}
