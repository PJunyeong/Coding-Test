//
//  프린터.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/07.
//

import Foundation

func solution(_ priorities:[Int], _ location:Int) -> Int {
    var priorityDict = getPriorityDict(priorities)
    var priorities = priorities
    var location = location
    var order = 0
    guard var curMaxPriority = priorityDict.keys.max() else { return 0 }
    print(priorityDict, curMaxPriority)
    
    while true {
        if location == 0 {
            let priority = priorities[0]
            if priority == curMaxPriority {
                return order + 1
            } else {
                priorities.removeFirst()
                priorities.append(priority)
                location = priorities.count - 1
            }
            
        } else {
            if priorities[0] == curMaxPriority {
                priorities.removeFirst()
                order += 1
                let curMaxCnt = priorityDict[curMaxPriority] ?? 0
                priorityDict[curMaxPriority] = curMaxCnt - 1
                if curMaxCnt - 1 == 0 {
                    curMaxPriority = priorityDict.filter{$0.value > 0}.map{$0.key}.max()!
                }
                
            } else {
                let item = priorities.removeFirst()
                priorities.append(item)
            }
            location -= 1
        }
    }
    
    return 0
}

func getPriorityDict(_ priorities: [Int]) -> [Int:Int] {
    var priorityDict = [Int:Int]()
    for priority in priorities {
        let cnt = priorityDict[priority] ?? 0
        priorityDict[priority] = cnt + 1
    }
    return priorityDict
}
