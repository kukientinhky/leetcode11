def main():
    height = [1,8,6,2,5,4,8,3,7]
    begin = 0
    end = len(height) - 1
    ans = 0
    while (begin < end):
        ans = max(ans, min(height[begin],height[end])*(end-begin))
        if (height[begin] < height[end]):
            begin = begin + 1
        else:
            end = end - 1
    print(ans) 

if __name__ == "__main__":
    main()
