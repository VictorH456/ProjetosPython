x = [1, 2, 3]
y = 3

try:
    x + y
    
except Exception as e:
    print(f"Error: {e}")
finally:
    print("oi")