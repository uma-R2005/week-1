def calculate_mean(scores):
    total = 0
    for score in scores:
        total += score
    return total / len(scores)


def calculate_median(scores):
    sorted_scores = sorted(scores)
    n = len(sorted_scores)
    mid = n // 2

    if n % 2 == 0:
        return (sorted_scores[mid - 1] + sorted_scores[mid]) / 2
    else:
        return sorted_scores[mid]


def calculate_mode(scores):
    frequency = {}
    max_freq = 0
    mode_list = []

    for score in scores:
        if score in frequency:
            frequency[score] += 1
        else:
            frequency[score] = 1

        if frequency[score] > max_freq:
            max_freq = frequency[score]

    # Collect all scores that appear max_freq times
    for score, freq in frequency.items():
        if freq == max_freq:
            mode_list.append(score)

    if len(mode_list) == len(frequency):
        return "No mode"  # All scores appear equally
    return mode_list


# Example usage
scores = [75, 80, 90, 90, 70, 85, 90, 70]

mean = calculate_mean(scores)
median = calculate_median(scores)
mode = calculate_mode(scores)

print("Scores:", scores)
print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)
