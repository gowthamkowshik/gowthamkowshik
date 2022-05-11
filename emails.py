n= int(input())
names_ids = [input().split() for _ in range(n)]
emails = {k: v for k,v in names_ids}
while True:
    try:
        name = input()
        if name in emails:
            print('%s=%s' % (name, emails[name]))
        else:
            print('Not found')
    except:
        break
