//
//  방금그곡.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/22.
//
import Foundation

func solution(_ m:String, _ musicinfos:[String]) -> String {
    let musicDict = ["C#" : "c", "D#" : "d", "F#" : "f",  "G#" : "g", "A#" : "a", "E#": "e"]
    var candidates = [(Int, Int, String)]()
    // 재생시간, 입력 순서, 노래 제목
    
    func convertMusicToString(_ info: String) -> String {
        var music = ""
        let info = Array(info).map{String($0)}
        for idx in 0..<info.count {
            let letter = info[idx]
            if letter == "#" {
                continue
            }
            if idx + 1 < info.count && info[idx + 1] == "#" {
                music += musicDict[letter + "#"]!
            } else {
                music += letter
            }
        }
        return music
    }
    
    func convertTime(_ start: String, _ end: String) -> Int {
        let start = start.split(separator: ":").map{Int(String($0))!}
        let end = end.split(separator:":").map{Int(String($0))!}
        let startTime = (start[0] * 60 + start[1])
        let endTime = (end[0] * 60 + end[1])
        return endTime - startTime
    }
        
    func playMusic(_ musicInfo: String, _ order: Int) {
        let musicInfo = musicInfo.split(separator: ",").map{String($0)}
        let (start, end, name, music) = (musicInfo[0], musicInfo[1], musicInfo[2], musicInfo[3])
        let time = convertTime(start, end)

        let convertedMusic = convertMusicToString(music)
        let q = time / convertedMusic.count
        let r = time % convertedMusic.count
        var playedMusic = ""
        
        for _ in 0..<q {
            playedMusic += convertedMusic
        }
        
        var idx = 0
        for letter in convertedMusic {
            if idx == r {
                break
            }
            playedMusic += String(letter)
            idx += 1
        }
        
        let playedMusicArray = Array(playedMusic).map{String($0)}
        if playedMusic.count >= targetMusic.count {
            for idx in 0..<(playedMusic.count - targetMusic.count + 1) {
                let curMusic = Array(playedMusicArray[idx..<idx+targetMusic.count]).joined()
                if curMusic == targetMusic {
                    let candidate = (time, order, name)
                    candidates.append(candidate)
                    return
                }
            }
        }
    }
    
    let targetMusic = convertMusicToString(m)
    
    for idx in 0..<musicinfos.count {
        let musicInfo = musicinfos[idx]
        playMusic(musicInfo, idx)
    }
            
    candidates.sort(by: { (first, second) in
        if first.0 > second.0 {
            return true
        } else if first.0 == second.0 {
            return first.1 <= second.1
        } else {
            return false
        }
    })
    if candidates.isEmpty {
        return "(None)"
    } else {
        let candidate = candidates[0]
        let music = candidate.2
        return music
    }
}
