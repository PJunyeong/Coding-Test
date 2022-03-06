import sys

n = int(sys.stdin.readline().rstrip())
sold = {}
for _ in range(n):
    book_name = sys.stdin.readline().rstrip()
    book_cnt = sold.get(book_name, 0)
    book_cnt += 1
    sold[book_name] = book_cnt

sold = [[val, key] for key, val in sold.items()]
sold.sort(key=lambda x:(-x[0], x[1]))
print(sold[0][1])