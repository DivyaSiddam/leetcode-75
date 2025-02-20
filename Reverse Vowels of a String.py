#https://leetcode.com/problems/reverse-vowels-of-a-string/?envType=study-plan-v2&envId=leetcode-75
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")  # Set for quick lookup
        s = list(s)  # Convert string to a mutable list
        
        left, right = 0, len(s) - 1  # Two-pointer initialization
        
        while left < right:
            while left < right and s[left] not in vowels:
                left += 1  # Move left pointer until a vowel is found
            while left < right and s[right] not in vowels:
                right -= 1  # Move right pointer until a vowel is found

            # Swap vowels
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        return "".join(s)  # Convert list back to string

# Example usage:
solution = Solution()
s1 = "IceCreAm"
s2 = "leetcode"

output1 = solution.reverseVowels(s1)
output2 = solution.reverseVowels(s2)

print(f"Input: {s1}  → Output: {output1}")  # Expected Output: "AceCreIm"
print(f"Input: {s2}  → Output: {output2}")  # Expected Output: "leotcede"
