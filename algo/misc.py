def hanoi(s, t, m, k):
    """Recursion."""
    if k == 1:
        return [(s, t)]
    step1 = hanoi(s, m, t, k - 1)
    step2 = [(s, t)]
    step3 = hanoi(m, t, s, k - 1)
    return step1 + step2 + step3
