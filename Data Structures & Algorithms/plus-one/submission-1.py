class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits

            digits[i] = 0

        return [1] + digits


    #  Brute force
    # def plusOne(self, digits: List[int]) -> List[int]:
    #     carry = 1

    #     for i in range(len(digits) - 1, -1, -1):
    #         s = digits[i] + carry

    #         if s == 10:
    #             digits[i] = 0
    #             carry = 1
    #         else:
    #             digits[i] = s
    #             carry = 0
    #             break

    #     return [1] + digits if carry else digits