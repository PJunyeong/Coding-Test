//
//  1461_도서관.swift
//  CodingTest
//
//  Created by Junyeong Park on 2022/04/26.
//

import Foundation

let input = readLine()!.split(separator: " ").map({Int(String($0))!})
let (N, M) = (input[0], input[1])
var books = Array(readLine()!.split(separator: " ").map({Int(String($0))!}))
var positive = [Int]()
var negative = [Int]()
for book in books{
    if book > 0{
        positive.append(book)
    } else {
        negative.append(book)
    }
}
positive.sort(by: >)
negative.sort(by: <)
var cursor = 0
var answers = [Int]()
answers += getAnswers(books:positive)
answers += getAnswers(books:negative)
answers.sort(by: <)
var answer = answers.popLast()!
answer += 2 * answers.reduce(0, +)
print(answer)

func getAnswers(books:[Int]) -> [Int]{
    var answers = [Int]()
    
    if books.count % M != 0 {
        answers.append(abs(books[(books.count/M)*M]))
    }
    var cursor = 0
    for _ in 0..<books.count/M{
        answers.append(abs(books[cursor]))
        cursor += M
    }
    return answers
}
