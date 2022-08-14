//
//  여행경로.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/14.
//

import Foundation

struct Ticket: Hashable {
    let start: String
    let end: String
    
    init(_ start: String, _ end: String) {
        self.start = start
        self.end = end
    }
}

func solution(_ tickets:[[String]]) -> [String] {
    var ticketDict = [Ticket: [Int]]()
    var nodeDict = [String:[String]]()
    let ticketCnt = tickets.count
    var checked = Array(repeating: false, count: ticketCnt)
    var result = [String]()
    
    for item in tickets.enumerated() {
        let idx = item.offset
        let element = item.element
        let (start, end) = (element[0], element[1])
        let nodeValue = nodeDict[start] ?? []
        nodeDict[start] = nodeValue + [end]
        let ticketValue = ticketDict[Ticket(start, end)] ?? []
        ticketDict[Ticket(start, end)] = ticketValue + [idx]
    }
    
    for key in nodeDict.keys {
        var value = nodeDict[key] ?? []
        value.sort(by: <)
        nodeDict[key] = value
    }
    
    func DFS(_ curNode: String, _ path: [String]) {
        if path.count == ticketCnt + 1 {
            if result.isEmpty {
                result = path
            }
            return
        }
        
        let nextNodes = nodeDict[curNode] ?? []
        for nextNode in nextNodes {
            let nextIndices = ticketDict[Ticket(curNode, nextNode)] ?? []
            for nextIdx in nextIndices {
                if !checked[nextIdx] {
                    checked[nextIdx] = true
                    DFS(nextNode, path + [nextNode])
                    checked[nextIdx] = false
                }
            }
        }
    }
    
    let firstNode = "ICN"
    let secondNodes = nodeDict[firstNode] ?? []
    for secondNode in secondNodes {
        let nextIndices = ticketDict[Ticket(firstNode, secondNode)] ?? []
        for nextIdx in nextIndices {
            checked[nextIdx] = true
            DFS(secondNode, [firstNode, secondNode])
            if !result.isEmpty {
                return result
            }
            checked[nextIdx] = false
        }
    }
    
    return result
}
