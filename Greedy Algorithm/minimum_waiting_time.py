def minimum_total_waiting_time(service_times):
    """
    Calculates the minimum total waiting time for a set of queries to be executed

    The key insight is a greedy approach: serving the shortest query next always
    minimizes the total waiting time. This is because each query's service time
    contributes to the waiting period of all subsequent queries. By processing
    shorter queries first, we minimize this compounding effect.

    Args:
        service_times: A list of numbers representing the service time for each query

    Returns:
        An integer representing the minimum possible total waiting time
    """
    # Sort service times in non-decreasing order to apply the greedy strategy
    # The overall time complexity is dominated by this sort: O(n log n)
    service_times.sort()

    total_waiting_time = 0
    # Iterate through the sorted service times to calculate the total wait time
    for i, service_time in enumerate(service_times):
        # The current query's service time adds to the waiting time of all
        # queries that are still remaining in the queue
        num_remaining_queries = len(service_times) - (i + 1)

        # The total waiting time *caused by this specific query* is its own
        # service time multiplied by the number of other queries that have to
        # wait for it to complete
        total_waiting_time += service_time * num_remaining_queries

    return total_waiting_time

# --- Example Usage ---

# Example from the text
queries = [2, 5, 1, 3]
min_wait = minimum_total_waiting_time(queries)

# The sorted list will be [1, 2, 3, 5]
# The calculation proceeds as follows:
# - Query 1 (time 1) makes 3 other queries wait -> 1 * 3 = 3
# - Query 2 (time 2) makes 2 other queries wait -> 2 * 2 = 4
# - Query 3 (time 3) makes 1 other query wait  -> 3 * 1 = 3
# - Query 4 (time 5) makes 0 other queries wait  -> 5 * 0 = 0
# Total = 3 + 4 + 3 + 0 = 10

print(f"Initial service times: {queries}")
print(f"Minimum total waiting time: {min_wait}") # Expected output: 10