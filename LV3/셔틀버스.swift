//
//  셔틀버스.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/15.
//

func solution(_ n:Int, _ t:Int, _ m:Int, _ timetable:[String]) -> String {
    var timetable = timetable.map{convertTime($0)}.sorted(by: <)
    var start = 0
    var end = timetable.count - 1
    var busTime = convertTime("09:00") - t
    var busMembers = [[Int]]()
    var busMember = [Int]()
    var busTimetable = [Int]()
    
    for _ in 0..<n {
        busTime += t
        busTimetable.append(busTime)
        busMember = []
        if start <= end {
            for crew in start...end {
                let time = timetable[crew]
                if time <= busTime {
                    start += 1
                    busMember.append(time)
                    if busMember.count == m {
                        break
                    }
                }
            }
        }
        busMembers.append(busMember)
    }
    
    busMembers.reverse()
    busTimetable.reverse()
    
    for idx in 0..<busMembers.count {
        let bus = busMembers[idx]
        let limitTime = busTimetable[idx]
        
        if bus.count < m {
            let answer = convertTime(limitTime)
            return answer
        } else {
            let last = bus.last!
            let answer = convertTime(last - 1)
            return answer
        }
    }
        
    return ""
}

func convertTime(_ time: Int) -> String {
    let hour = time / 60
    let minute = time % 60
    let hourString = hour < 10 ? "0" + String(hour) : String(hour)
    let minuteString = minute < 10 ? "0" + String(minute) : String(minute)
    return hourString + ":" + minuteString
}


func convertTime(_ time: String) -> Int {
    let time = time.split(separator: ":").map{Int(String($0))!}
    let (hour, minute) = (time[0], time[1])
    return hour * 60 + minute
}
