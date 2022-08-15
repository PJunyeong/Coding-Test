//
//  신고 결과 받기.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/15.
//

import Foundation

func solution(_ id_list:[String], _ report:[String], _ k:Int) -> [Int] {
    var nameDict = [String:Int]()
    for item in id_list.enumerated() {
        nameDict[item.element] = item.offset
    }
    var reportInfo = Array(repeating: Set<Int>(), count: id_list.count)
    
    for r in report {
        let r = r.split(separator: " ").map{String($0)}
        let (reporter, reported) = (nameDict[r[0]]!, nameDict[r[1]]!)
        reportInfo[reporter].insert(reported)
    }
    var reportList = Array(repeating: 0, count: id_list.count)
    for report in reportInfo {
        for id in report {
            reportList[id] += 1
        }
    }
    var reportResult = Set<Int>()
    for idx in 0..<reportList.count {
        let reportCnt = reportList[idx]
        if reportCnt >= k {
            reportResult.insert(idx)
        }
    }
    var answers = [Int]()
    
    for report in reportInfo {
        let cnt = report.intersection(reportResult).count
        answers.append(cnt)
    }
    return answers
}
