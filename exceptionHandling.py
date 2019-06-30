# Compile Time - Syntax errors
# Runtime errors - may be wrong input - DIVISION BY ZERO
# logical errors


a = 5
b = 0
c= 0

try:
    print(a/b)
except Exception as e:
    print("ERROR:", e)

finally:
    print("I am gona execute anyway")


# Error specific exceptions
try:
    print(a/c)
except ZeroDivisionError as e:
    print("error", e)
except ValueError as e:
    print("invalid")

except Exception as e:
    print("All other  errors ", e)

finally:
    print("Stop me if you can")