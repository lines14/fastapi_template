class StringValidator:
    def __init__(self, value: str):
        self.value = value

    def is_length_between(self, min_length: int, max_length: int) -> bool:
        return min_length <= len(self.value) <= max_length
    
    def is_alphanumeric(self) -> bool:
        return self.value.isalnum()
    
    def has_spaces(self) -> bool:
        return ' ' in self.value

    def __str__(self):
        return self.value