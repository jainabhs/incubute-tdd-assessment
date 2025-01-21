class StringCalculator:
    @staticmethod
    def add(numbers: str) -> int:
        if not numbers:
            return 0
        delimiters = [',', '\n', '//',';']
        for delimiter in delimiters:
            numbers = numbers.replace(delimiter, "$$")
        numbers = numbers.replace("$", ",")
        _nums = [int(i.strip()) for i in numbers.split(",") if i != '']
        _sum = 0
        _negatives = []
        for _num in _nums:
            if _num > 0:
                _sum = _sum + _num
            else:
                _negatives.append(_num)
        
        if len(_negatives) != 0:
            raise ValueError(f"Negative numbers not allowed: {','.join(map(str, _negatives))}")
        return _sum
        
print(StringCalculator.add("")) # Output: 0
print(StringCalculator.add("1")) # Output: 1
print(StringCalculator.add("1,5")) # Output: 6
print(StringCalculator.add("//;\n1;2")) # Output: 3
print(StringCalculator.add("1,-2\n-5")) # Output : Error
