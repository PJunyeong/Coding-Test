//
//  스킬트리.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/08/18.
//

import Foundation

func solution(_ skill:String, _ skill_trees:[String]) -> Int {
    let skillSet = Set(Array(skill))
    var skillDict = [Character:Int]()
    var skillOrder = 0
    for letter in skill {
        skillDict[letter] = skillOrder
        skillOrder += 1
    }
    
    func isRightSkillTree(_ skillTree: String) -> Bool {
        let filteredSkills = Array(skillTree).filter{skillSet.contains($0)}
        var skillOrder = 0
        for letter in filteredSkills {
            if skillOrder == skillDict[letter]! {
                skillOrder += 1
            } else {
                return false
            }
        }
        return true
    }
    
    var total = 0
    for skillTree in skill_trees {
        if isRightSkillTree(skillTree) {
            total += 1
        }
    }
    
    return total
}
