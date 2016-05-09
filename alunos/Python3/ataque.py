def main():
    term1, term2 = [0] * 2048, [0] * 2048
    for _ in range(int(input())):
        x, y = map(int, input().split())
        term1[x + y] += 1
        term2[x - y] += 1
    print(sum(sum(t * (t - 1) for t in filter(None, term)) for term in (term1, term2)) // 2)


if __name__ == '__main__':
    main()
