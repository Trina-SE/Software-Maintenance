"""
Data Processing Module - Contains code duplication and poor error handling
"""

class DataProcessor:
    """Processes data"""
    
    def process_numbers(self, data):
        """Process a list of numbers"""
        result = []
        total = 0
        count = 0
        
        for item in data:
            if isinstance(item, (int, float)):
                result.append(item * 2)
                total = total + item
                count = count + 1
        
        avg = total / count if count > 0 else 0
        return {
            'processed': result,
            'total': total,
            'average': avg,
            'count': count
        }
    
    def process_strings(self, data):
        """Process a list of strings"""
        result = []
        total = 0
        count = 0
        
        for item in data:
            if isinstance(item, str):
                result.append(item.upper())
                total = total + len(item)
                count = count + 1
        
        avg = total / count if count > 0 else 0
        return {
            'processed': result,
            'total': total,
            'average': avg,
            'count': count
        }
    
    def process_mixed(self, data):
        """Process mixed data"""
        result = []
        total = 0
        count = 0
        
        for item in data:
            if isinstance(item, (int, float)):
                result.append(item * 2)
                total = total + item
                count = count + 1
            elif isinstance(item, str):
                result.append(item.upper())
                total = total + len(item)
                count = count + 1
        
        avg = total / count if count > 0 else 0
        return {
            'processed': result,
            'total': total,
            'average': avg,
            'count': count
        }
    
    def calc_stats(self, numbers):
        """Calculate statistics"""
        if not numbers or len(numbers) == 0:
            return None
        
        s = sum(numbers)
        c = len(numbers)
        a = s / c
        
        mx = max(numbers)
        mn = min(numbers)
        
        return {
            'sum': s,
            'count': c,
            'avg': a,
            'max': mx,
            'min': mn
        }
