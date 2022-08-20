//
//  주차 요금 계산.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/20.
//

import Foundation

func solution(_ fees:[Int], _ records:[String]) -> [Int] {
    var carsDict = [String:Int]()
    var carsCheck = [String:Bool]()
    
    let (defaultTime, defaultPrice, unitTime, unitPrice) = (fees[0], fees[1], fees[2], fees[3])
    
    func getPrice(_ time: Int) -> Int {
        if time <= defaultTime {
            return defaultPrice
        } else {
            var total = defaultPrice
            let q: Int
            if (time - defaultTime) % unitTime == 0 {
                q = (time - defaultTime) / unitTime
            } else {
                q = (time - defaultTime) / unitTime + 1
            }
            return defaultPrice + q * unitPrice
        }
    }
    
    for record in records {
        let record = record.split(separator: " ").map{String($0)}
        let (timeString, car, carCheck) = (record[0], record[1], record[2])
        let time = convertTime(timeString)
        let carTime = carsDict[car] ?? 0
        if carCheck == "IN" {
            carsDict[car] = carTime - time
            carsCheck[car] = false
        } else {
            carsDict[car] = carTime + time
            carsCheck[car] = true
        }
    }
    
    let lastTime = convertTime("23:59")
    for car in carsCheck.keys {
        guard let value = carsCheck[car] else { continue }
        if !value {
            let carTime = carsDict[car] ?? 0
            carsDict[car] = carTime + lastTime
            carsCheck[car] = true
        }
    }
    
    var prices = [Int]()
    let sortedCarNames = carsDict.keys.sorted(by: <)
    for car in sortedCarNames {
        let time = carsDict[car] ?? 0
        let price = getPrice(time)
        prices.append(price)
    }
    
    return prices
}

func convertTime(_ time: String) -> Int {
    let time = time.split(separator: ":").map{Int(String($0))!}
    let (hour, minute) = (time[0], time[1])
    return hour * 60 + minute
}
