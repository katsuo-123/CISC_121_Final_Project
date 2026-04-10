import random
import gradio as gr


class SortingState:
    def __init__(self):
        # Generates random array as input
        self.arr = [random.randint(10, 121) for _ in range(7)]
        self.i = 0
        self.j = 0
        # Whether the sorting is finished
        self.finished = False

    def get_status(self):
        # Lets the player know which two numbers are being compared right now
        if self.finished:
            return "Sorting Complete!"
        left = self.arr[self.j]
        right = self.arr[self.j + 1]
        return f"COmparing {left} and {right}."


def generate_html_view(state):
    # Builds the array visualization.
    html = '<div style="display:flex; justify-content:center; gap:10px; padding:30px; flex-wrap:wrap;">'

    for index, val in enumerate(state.arr):
        color = "#5f6ba8"
        if state.finished:
            color = "#e15e67"
        elif index == state.j or index == state.j + 1:
            color = "#ed809c"

        html += f"""
        <div style="
            width:70px;
            height:70px;
            border-radius:12px;
            background:{color};
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:bold;
            font-size:20px;
            box-shadow:0 2px 8px rgba(0,0,0,0.12);
            color:white;
        ">
            {val}
        </div>
        """

    html += "</div>"
    return html


def process_decision(user_choice, state):
    if state.finished:
        return state, generate_html_view(state), "Sorting Complete!", "Done!"
    left = state.arr[state.j]
    right = state.arr[state.j + 1]
    correct = "Swap" if left > right else "Skip"
    feedback = ""

    if user_choice == correct:
        feedback = "Correct!."
        if correct == "Swap":
            state.arr[state.j], state.arr[state.j + 1] = state.arr[state.j + 1], state.arr[state.j]
    else:
        feedback = f"Wrong! The correct answer is {correct}."
        if correct == "Swap":
            state.arr[state.j], state.arr[state.j + 1] = state.arr[state.j + 1], state.arr[state.j]
    # Move forward to the next comparison
    # The -2 keeps j+1 inside the list
    if state.j < len(state.arr) - 2 - state.i:
        state.j += 1
    else:
        # Start from the beginning when the full pass is done.
        state.i += 1
        state.j = 0
    # When the array is sorted
    if state.i >= len(state.arr) - 1:
        state.finished = True
        feedback = ""
    return state, generate_html_view(state), state.get_status(), feedback


def reset_game():
    # Startsa new game with a new randomly generaated array.
    state = SortingState()
    return (
        state,
        generate_html_view(state),
        state.get_status(),
        "New game started."
    )
demo.launch()
