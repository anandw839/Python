def is_right_angled_triangle(side1, side2, side3):
    # check if any side length is non-positive
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        return False
 
    # check each combination of sides to see if Pythagorean theorem holds
    if side1 * side1 == side2 * side2 + side3 * side3:
        return True
 
    if side2 * side2 == side1 * side1 + side3 * side3:
        return True
 
    if side3 * side3 == side1 * side1 + side2 * side2:
        return True
 
    # if none of the combinations hold, it's not a right-angled triangle
    return False
 
print(is_right_angled_triangle(3, 4, 5))  # Output: True
