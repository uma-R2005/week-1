def calculate_mean(scores):
    return sum(scores) / len(scores)

def calculate_median(scores):
    sorted_scores = sorted(scores)
    n = len(scores)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        return sorted_scores[mid]

def calculate_mode(scores):
    frequency = {}
    for score in scores:
        frequency[score] = frequency.get(score, 0) + 1

    max_freq = max(frequency.values())
    modes = [key for key, value in frequency.items() if value == max_freq]
    
    if len(modes) == len(frequency):
        return None  # No mode if all values appear equally
    return modes

# Example usage:
scores = [10, 20, 15, 10, 25, 30, 15]

print("Mean:", calculate_mean(scores))
print("Median:", calculate_median(scores))
print("Mode:", calculate_mode(scores))
