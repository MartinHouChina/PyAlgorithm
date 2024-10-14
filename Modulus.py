class Modulus:
    def __init__(self, num, mod):
        
        if num < 0: num += mod
        elif num >= mod: num -= mod
        
        self.num = num
        self.mod = mod
    
    def __add__(self, other):  
        if isinstance(other, int):  
            return Modulus(self.num + other % self.mod, self.mod)  
        elif isinstance(other, Modulus):  
            if other.mod != self.mod:  
                raise ValueError
            else:  
                return Modulus(self.num + other.num, self.mod) 
        else:  
            raise TypeError
        
    def __iadd__(self, other):
        if isinstance(other, int):  
            self = Modulus(self.num + other % self.mod, self.mod)  
            return self
        elif isinstance(other, Modulus):  
            if other.mod != self.mod:  
                raise ValueError
            else:  
                self = Modulus(self.num + other.num, self.mod) 
                return self
        else:  
            raise TypeError
        
    def __mul__(self, other):  
        if isinstance(other, int):  
            return Modulus(self.num * other % self.mod, self.mod)
        elif isinstance(other, Modulus):  
            if other.mod != self.mod:  
                raise ValueError
            else:  
                return Modulus(self.num * other.num % self.mod, self.mod)   
        else:  
            raise TypeError
        
    def __imul__(self, other):  
        if isinstance(other, int):  
            self = Modulus(self.num * other % self.mod, self.mod)
            return self
        elif isinstance(other, Modulus):  
            if other.mod != self.mod:  
                raise ValueError 
            else:  
                self = Modulus(self.num * other.num % self.mod, self.mod)   
                return self
        else:  
            raise TypeError
        
    def __sub__(self, other):  
        if isinstance(other, int):  
            return Modulus(self.num - other % self.mod, self.mod)
        elif isinstance(other, Modulus):  
            if other.mod != self.mod:  
                raise ValueError  
            else:  
                return Modulus(self.num - other.num, self.mod)
        else:  
            raise TypeError
        
    def __isub__(self, other):  
        if isinstance(other, int):  
            self = Modulus(self.num - other % self.mod, self.mod)
            return self
        elif isinstance(other, Modulus):  
            if other.mod != self.mod:  
                raise ValueError
            else:  
                return Modulus(self.num - other.num, self.mod)
        else:  
            raise TypeError
        
    def __ipow__(self, other):
        if isinstance(other, int):  
            self = Modulus(pow(self.num, other, self.mod), self.mod)
            return self
        else:
            raise TypeError
    
    def __pow__(self, other):
        if isinstance(other, int):  
            return Modulus(pow(self.num, other, self.mod), self.mod)
        else:
            raise TypeError
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Modulus):
            if self.mod == other.mod:
                return self.num == other.num
            else:
                raise ValueError
        else:
            raise TypeError
    
    def __floordiv__(self, other):
        if isinstance(other, int):  
            return Modulus(self.num * pow(other, self.mod - 2, self.mod) % self.mod, self.mod)
        elif isinstance(other, Modulus):  
            if other.mod != self.mod:  
                raise ValueError  
            else:  
                return Modulus(self.num * pow(other.num, self.mod - 2, self.mod) % self.mod, self.mod)
        else:  
            raise TypeError
    
    def inv(self):
        return Modulus(pow(self.num, self.mod - 2, self.mod), self.mod)

    def __ifloordiv__(self, other):
        if isinstance(other, int):  
            self = Modulus(self.num * pow(other, self.mod - 2, self.mod) % self.mod, self.mod)
            return self
        elif isinstance(other, Modulus):  
            if other.mod != self.mod:  
                raise ValueError  
            else:  
                self = Modulus(self.num * other.inv(), self.mod)
                return self
        else:  
            raise TypeError
    
    def __rfloordiv__(self, other):
        return other * self.inv()
        
    def __radd__(self, other):
        return self + other
    
    def __rmul__(self, other):
        return self * other

    def __neg__(self):
        return Modulus(-self.num, self.mod)

    def __rsub__(self, other):
        return -self + other
        
    def __repr__(self) -> str:
        return f"Modulus({self.num}, mod={self.mod})"