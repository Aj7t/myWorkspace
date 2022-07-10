
import asyncio
async def doMathematics(a,b):
    print("adding")
    print(a+b)
    print("multiple")
    print(a*b)
    print("end")
    await asyncio.sleep(1)
    return ("doMathematics")
    
print(doMathematics(2,3))