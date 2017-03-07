''' A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


from commonLibs.timer import Timer


@profile
def solution(num):
    threshold = 0
    while num:
        for i in range(num, 1, -1):
            p = str(num * i)
            if p == p[::-1]:
                if int(p) > threshold:
                    threshold = int(p)
                    break
        num -= 1
    return threshold


if __name__ == "__main__":
    print solution(999)
