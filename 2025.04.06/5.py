def orth_triangle(cathetus1: float = 0, cathetus2: float = 0, hypotenuse: float = 0) -> float | None:
   
    if (cathetus1 > 0) + (cathetus2 > 0) + (hypotenuse > 0) > 2:
        return None  

    if (cathetus1 == 0) + (cathetus2 == 0) + (hypotenuse == 0) == 3:
        return None  

    if (cathetus1 > 0) and (cathetus2 > 0):
        return (cathetus1 ** 2 + cathetus2 ** 2) ** (1/2)  

    if (cathetus1 > 0) and (hypotenuse > 0):
        if hypotenuse < cathetus1:
            return None  
        return (hypotenuse ** 2 - cathetus1 ** 2) ** (1/2)   

    if (cathetus2 > 0) and (hypotenuse > 0):
        if hypotenuse < cathetus2:
            return None  
        return (hypotenuse ** 2 - cathetus2 ** 2) ** (1/2)  