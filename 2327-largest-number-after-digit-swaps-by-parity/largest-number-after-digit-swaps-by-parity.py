class Solution:
    def largestInteger(self, num: int) -> int:

        digits = list(str(num))

        for i in range(len(digits)):
            max_index = i

            for j in range(i + 1, len(digits)):

                if int(digits[j]) % 2 == int(digits[i]) % 2:
                    if digits[j] > digits[max_index]:
                        max_index = j

            digits[i], digits[max_index] = digits[max_index], digits[i]

        return int("".join(digits))