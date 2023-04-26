class color:
    
    def __init__(self, R = 0, G = 0, B = 0, A = 1):

        #checking if Red, Green and Blue are in range of 0 - 255 and not float
        for num in [R, G, B]:
            if num > 255 or num < 0 or num != int(num):
                raise Exception(f"{num} is not in range of (0-255)")

        #checking if alpha is in range of 0 - 1
        if A > 1 or A < 0:
            raise Exception(f"{num} is not in range of (0 - 1)")
        
        self.R = R; self.G = G; self.B = B; self.A = A

    def __add__(self, OtherColor):

        #adding colors, each part of color by itself, multiplying it on alpha. Alpha of final color is 1
        
        A1 = self.A; A2 = OtherColor.A
        
        R = int(self.R * A1 + OtherColor.R * A2)
        if R > 255:
            R = 255
        G = int(self.G * A1 + OtherColor.G * A2)
        if G > 255:
            G = 255
        B = int(self.B * A1 + OtherColor.B * A2)
        if B > 255:
            B = 255
            
        return color(R, G, B, 1)

    def __sub__(self, OtherColor):

        #subtracting colors, each part of color by itself, multiplying it on alpha. Alpha of final color is 1
        
        A1 = self.A; A2 = OtherColor.A
        
        R = int(self.R * A1 - OtherColor.R * A2)
        if R < 0:
            R = 0
        G = int(self.G * A1 - OtherColor.G * A2)
        if G < 0:
            G = 0
        B = int(self.B * A1 - OtherColor.B * A2)
        if B < 0:
            B = 0
            
        return color(R, G, B, 1)

    def __mul__(self, Other):

        if type(Other) == type(1):

            R = int(self.R * Other)
            if R > 255:
                R = 255
            elif R < 0:
                R = 0

            G = int(self.G * Other)
            if G > 255:
                G = 255
            elif G < 0:
                G = 0

            B = int(self.B * Other)
            if B > 255:
                B = 255
            elif B < 0:
                B = 0

            return color(R, G, B, self.A)

        #multiplying colors, Alpha of color maters how much color channel will matter on result. Alpha of final color is 1
        
        A1 = self.A; A2 = Other.A
        
        R = int(self.R * A1 * Other.R * A2 / 255)
        G = int(self.G * A1 * Other.G * A2 / 255)
        B = int(self.B * A1 * Other.B * A2 / 255)
            
        return color(R, G, B, 1)

    def __truediv__(self, Other):

        if type(Other) == type(1):

            R = int(self.R / Other)
            if R > 255:
                R = 255
            elif R < 0:
                R = 0

            G = int(self.G / Other)
            if G > 255:
                G = 255
            elif G < 0:
                G = 0

            B = int(self.B / Other)
            if B > 255:
                B = 255
            elif B < 0:
                B = 0

            return color(R, G, B, self.A)

        #multiplying colors, Alpha of color maters how much color channel will matter on result. Alpha of final color is 1
        
        A1 = self.A; A2 = Other.A
        
        R = int(self.R * A1 / Other.R / A2 * 255)
        G = int(self.G * A1 / Other.G / A2 * 255)
        B = int(self.B * A1 / Other.B / A2 * 255)
            
        return color(R, G, B, 1)

    def __str__(self):
        return f'{self.R}, {self.G}, {self.B}, {self.A}'
