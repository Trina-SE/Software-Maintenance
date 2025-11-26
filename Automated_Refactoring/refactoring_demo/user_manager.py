"""
User Management Module - Contains refactoring opportunities
"""

class UserManager:
    """Manages user operations"""
    
    def __init__(self):
        self.users = []
        self.user_count = 0
        self.max_users = 100
    
    def add_user(self, n, e, a, p):
        """Add a new user"""
        if len(self.users) >= self.max_users:
            return False
        
        u = {
            'nm': n,
            'em': e,
            'ag': a,
            'pwd': p
        }
        
        # Validation
        if len(n) < 3:
            return False
        if '@' not in e:
            return False
        if a < 18 or a > 120:
            return False
        if len(p) < 6:
            return False
        
        self.users.append(u)
        self.user_count = self.user_count + 1
        return True
    
    def remove_user(self, e):
        """Remove a user by email"""
        for i in range(len(self.users)):
            if self.users[i]['em'] == e:
                self.users.pop(i)
                self.user_count = self.user_count - 1
                return True
        return False
    
    def get_user(self, e):
        """Get user by email"""
        for i in range(len(self.users)):
            if self.users[i]['em'] == e:
                return self.users[i]
        return None
    
    def update_user(self, e, n, a):
        """Update user info"""
        for i in range(len(self.users)):
            if self.users[i]['em'] == e:
                if len(n) < 3:
                    return False
                if a < 18 or a > 120:
                    return False
                self.users[i]['nm'] = n
                self.users[i]['ag'] = a
                return True
        return False
    
    def list_users(self):
        """List all users"""
        result = []
        for i in range(len(self.users)):
            result.append(self.users[i])
        return result
    
    def get_user_count(self):
        """Get total users"""
        return self.user_count
