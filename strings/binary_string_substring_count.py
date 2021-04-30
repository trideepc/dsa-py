"""
This is a practice for strings.
Given a binary string, count number of substrings that start and end with 1.
"""


class StrCount(object):
    def __init__(self):
        pass

    @staticmethod
    def count_substring(input_string):
        """
        Complexity o(n2)
        :param input_string:
        :return:
        """
        count = 0
        for i in range(0, len(input_string)):
            if int(input_string[i]) == 1:
                for j in range(i + 1, len(input_string)):
                    if int(input_string[j]) == 1:
                        count = count + 1
        return count

    """
        int l = 0, r = s.length - 1;

        while (l < r){
    
        if (s.charAt(l) == '1' & & s.charAt(r) == '1' {
        list.add(s.substirng(l, r);
        l++;r--;
        continue;
        }
        if (s.charAt(l) == '0') l++;
        if (s.charAt(r) == '0') r--;
    
        }
    """


    @staticmethod
    def count_sub_str(st):
        """
        Complexity o(n)
        :param st:
        :return:
        """
        n = len(st)
        # Count of 1's in input string
        m = 0

        # Traverse input string and
        # count of 1's in it
        for i in range(0, n):
            if st[i] == '1':
                m = m + 1

        # Return count of possible
        # pairs among m 1's
        return m * (m - 1) // 2


if __name__ == '__main__':
    count = StrCount.count_substring('00100101')
    print("Substring count: ", count)

    count = StrCount.count_sub_str('00100101')
    print("Substring count: ", count)

    count = StrCount.count_sub_str('1000100100100101')
    print("Substring count: ", count)
