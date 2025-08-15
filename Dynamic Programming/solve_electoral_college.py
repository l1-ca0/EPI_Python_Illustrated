def solve_electoral_college(states, required_ev):
    """
    Finds the minimum popular votes to win the Electoral College
    
    Args:
        states: A list of tuples, where each is (electoral_votes, popular_votes_to_win)
    """
    # Find the total possible electoral votes
    total_ev = sum(s[0] for s in states)
    
    # dp[e] = min popular votes to get exactly `e` electoral votes
    dp = [float('inf')] * (total_ev + 1)
    dp[0] = 0 # Base case: 0 EV costs 0 votes
    
    for ev, pop_votes in states:
        # Iterate backwards to ensure each state is used only once
        for e in range(total_ev, ev - 1, -1):
            dp[e] = min(dp[e], pop_votes + dp[e - ev])
    
    # Find the minimum popular votes for any outcome >= required_ev
    min_popular_votes = min(dp[e] for e in range(required_ev, total_ev + 1))
    
    return min_popular_votes

# Example Data (simplified)
states = [(55, 4000), (38, 3000), (29, 2000), (29, 1500)] # (EV, Pop Votes)
required_ev = 70
# To get 70+ EV: (55, 29, 29 is not possible)
# (55, 29) -> 84 EV, 5500 pop
# (38, 29, 29) -> 96 EV, 6500 pop

