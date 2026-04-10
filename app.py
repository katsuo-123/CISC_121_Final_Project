import random
import gradio as gr


class SortingState:
    def __init__(self):
        self.arr = [random.randint(10, 121) for _ in range(7)]
        self.i = 0
        self.j = 0
        self.finished = False

    def get_status(self):
        if self.finished:
            return "Sorting Complete!"
        left = self.arr[self.j]
        right = self.arr[self.j + 1]
        return f"Comparing {left} and {right}."


def generate_html_view(state):
    html = """
    <div style="display:flex; justify-content:center; gap:14px; padding:40px 0; flex-wrap:wrap;">
    """

    for index, val in enumerate(state.arr):
        color = "#6b78b8"

        if state.finished:
            color = "#e16874"
        elif index == state.j or index == state.j + 1:
            color = "#ea84a2"

        html += f"""
        <div style="
            width:96px;
            height:96px;
            border-radius:18px;
            background:{color};
            display:flex;
            align-items:center;
            justify-content:center;
            font-weight:700;
            font-size:24px;
            color:white;
            box-shadow:0 4px 12px rgba(0,0,0,0.18);
        ">
            {val}
        </div>
        """

    html += "</div>"
    return html


def process_decision(user_choice, state):
    if state.finished:
        return state, generate_html_view(state), "Sorting Complete!", "Click **`Generate Random Array`** to start a new game."

    left = state.arr[state.j]
    right = state.arr[state.j + 1]
    correct = "Swap" if left > right else "Skip"

    if user_choice == correct:
        feedback = "Correct!"
        if correct == "Swap":
            state.arr[state.j], state.arr[state.j + 1] = state.arr[state.j + 1], state.arr[state.j]
    else:
        feedback = f"Wrong! The correct answer is {correct}."
        if correct == "Swap":
            state.arr[state.j], state.arr[state.j + 1] = state.arr[state.j + 1], state.arr[state.j]

    if state.j < len(state.arr) - 2 - state.i:
        state.j += 1
    else:
        state.i += 1
        state.j = 0

    if state.i >= len(state.arr) - 1:
        state.finished = True
        feedback = "Sorting Completed!"

    return state, generate_html_view(state), state.get_status(), feedback


def reset_game():
    state = SortingState()
    return (
        state,
        generate_html_view(state),
        state.get_status(),
        "New game started."
    )


with gr.Blocks(title="Bubble Sort", theme=gr.themes.Soft()) as demo:
    game_state = gr.State(SortingState())

    gr.Markdown("""
    # Bubble Sort

    Sort the array using the **Bubble Sort** algorithm.

    **Rules:**

    1. Take a look at the left number.  
    2. Take a look at the right number.  
    3. Swap if the left number is greater than the right number.  
    4. Skip if the left number is less than or equal to the right number.  
    5. Repeat until the entire array is sorted in ascending order.
    """)

    array_view = gr.HTML(value=generate_html_view(SortingState()))
    status_text = gr.Markdown("Click **Generate Random Array** to start.")
    feedback_text = gr.Markdown("")

    with gr.Row():
        generate_btn = gr.Button("Generate Random Array", scale=1)

    with gr.Row():
        swap_btn = gr.Button("Swap")
        skip_btn = gr.Button("Skip")

    generate_btn.click(
        fn=reset_game,
        inputs=[],
        outputs=[game_state, array_view, status_text, feedback_text]
    )

    swap_btn.click(
        fn=lambda state: process_decision("Swap", state),
        inputs=game_state,
        outputs=[game_state, array_view, status_text, feedback_text]
    )

    skip_btn.click(
        fn=lambda state: process_decision("Skip", state),
        inputs=game_state,
        outputs=[game_state, array_view, status_text, feedback_text]
    )

demo.launch()
    
