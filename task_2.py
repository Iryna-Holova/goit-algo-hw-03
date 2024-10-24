"""
Draws a Koch snowflake using recursion with the turtle module. The depth
of the recursion is entered by the user.
"""

import turtle


def koch_curve(t: turtle.Turtle, order: int, size: float) -> None:
    """
    Draws a single Koch curve using recursion.

    Args:
        t (turtle.Turtle): The turtle object used for drawing.
        order (int): The recursion depth (order of the curve).
        size (float): The length of the line segment.
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)


def draw_koch_snowflake(order: int, size: float = 300) -> None:
    """
    Draws a complete Koch snowflake by drawing three Koch curves
    in the shape of an equilateral triangle.

    Args:
        order (int): The recursion depth (order of the snowflake).
        size (float): The size of the snowflake.
    """
    window = turtle.Screen()
    window.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / 3)  # Center the snowflake
    t.pendown()

    # Draw three sides of the snowflake
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()


def input_integer() -> int:
    """
    Prompts the user to enter an integer and validates the input.
    """
    while True:
        try:
            user_input = int(input("Enter the recursion depth: "))
            if user_input < 0:
                raise ValueError("Depth must be a non-negative integer.")
            return user_input
        except ValueError as e:
            print(f"Invalid input: {e}")


if __name__ == "__main__":
    user_order = input_integer()
    draw_koch_snowflake(user_order)
