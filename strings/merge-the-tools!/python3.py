# Method-1 (Without using List Comprehension)
def merge_the_tools(string, k):
    # your code goes here
    for i in range(0, len(string), k):
        s = ""
        for j in string[i : i + k]:
            if j not in s:
                s += j          
        print(s)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


# Method-2 (Using List Comprehension)
def merge_the_tool(string, k):
    for i in range(0, len(string), k):
        u = []
        print(''.join([j for j in string[i:i+k] if not (j in u or u.append(j))]))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tool(string, k)