//
//  기능개발.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/05/23.
//

import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var answers = [Int]()
    var progresses = progresses
    var speeds = speeds
    while progresses.isEmpty == false {
        // 작업이 존재하는 동안 반복
        var newProgresses = [Int]()
        for data in zip(progresses, speeds) {
            let pro = data.0
            let speed = data.1
            newProgresses.append(pro + speed)
            // 현 시점 개발 진도 업데이트
        }
        var done = 0
        progresses = newProgresses
        for pro in progresses {
            if pro >= 100 {
                done += 1
            } else {
                break
                // 배포 불가능하다면 break.
            }
            // 앞에서부터 완료가 된 기능까지만 배포 가능
        }
        
        if done != 0 {
            progresses = Array(progresses[done..<progresses.count])
            speeds = Array(speeds[done..<speeds.count])
            answers.append(done)
            // 배포한 기능은 제외, 남아 있는 기능으로 progresses 및 speeds 구성
        }
    }
    return answers
}
