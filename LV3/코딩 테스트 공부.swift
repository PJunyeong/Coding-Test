import Foundation

func solution(_ alp:Int, _ cop:Int, _ problems:[[Int]]) -> Int {
    let maxAlp = problems.map{$0[0]}.max()!
    let maxCop = problems.map{$0[1]}.max()!
    let alp = min(alp, maxAlp)
    let cop = min(cop, maxCop)
    let INF = 10000
    var dp = Array(repeating: Array(repeating: INF, count: maxCop + 1), count: maxAlp + 1)
    dp[alp][cop] = 0
    
    for a in alp..<maxAlp+1 {
        for c in cop..<maxCop+1 {
            var flag = false
            
            if a + 1 <= maxAlp {
                dp[a+1][c] = min(dp[a+1][c], dp[a][c] + 1)
                flag = true
            }
            if c + 1 <= maxCop {
                dp[a][c+1] = min(dp[a][c+1], dp[a][c] + 1)
                flag = true
            }
            
            if flag {
                for problem in problems {
                    let (alp_req, cop_req, alp_rwd, cop_rwd, cost) = (problem[0], problem[1], problem[2], problem[3], problem[4])
                    
                    if a >= alp_req && c >= cop_req {
                        let totalAlp = min(maxAlp, a + alp_rwd)
                        let totalCop = min(maxCop, c + cop_rwd)
                        dp[totalAlp][totalCop] = min(dp[totalAlp][totalCop], dp[a][c] + cost)
                    }
                }
            }
        }
    }
    return dp[maxAlp][maxCop]
}
