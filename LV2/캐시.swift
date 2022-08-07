//
//  캐시.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/07.
//
import Foundation

func solution(_ cacheSize:Int, _ cities:[String]) -> Int {
    var total = 0
    var cache = Set<String>()
    var cacheArray = [String]()
    
    for city in cities {
        if cache.contains(city) {
            total += 1
            guard let idx = cacheArray.firstIndex(of: city) else { continue }
            cacheArray.remove(at: idx)
            cacheArray.append(city)
        } else {
            total += 5
            if cache.count < cacheSize {
                cache.insert(city)
                cacheArray.append(city)
            } else if !cache.isEmpty {
                let removedItem = cacheArray.removeFirst()
                cache.remove(removedItem)
                cache.insert(city)
                cacheArray.append(city)
            }
        }
    }
    return total
}

