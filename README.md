# CISC_121_Final_Project


# Demo Video
https://github.com/user-attachments/assets/2a6d419f-b67c-4360-af88-c14284202a77


I chose bubble sort because it is one of the simplest and most basics algorithm. It only compares adjacent elements and uses a very clear rule. This make it very suiatble for demonstations and visualization.


# Probelm Breakdown
0. Wirte the core algorithm (Without using gradio).
   
1. Introduce the Bubble Sort algorithm to the user.
   
2. Generate a random array as input to ensure valid and varied test cases.
   
3. Allow the user to participate in the sorting process:
   - Compare two adjacent elements
   - Swap if left > right
   - Skip if left < right
   - Repeat until the array is sorted
     
4. Track the progress of the algorithm:
   - Keep track of the current pass (i)
   - Keep track of the current comparison index (j)
   - Ensure the process follows Bubble Sort logic correctly

5. Provide feedback to enhance the user's understanding :
   - Show "Correct" when the user makes the right decision
   - Show "Wrong" when the user makes the wrong decision, show the correct answer.
   - Move to the next step regardless of correctness

6. Display the sorted array when the entire process is completed.


# Testing
Randomly generated inputs ensure the codes run regardless of cases.
<img width="1282" height="614" alt="Screenshot 2026-04-09 at 9 40 10 PM" src="https://github.com/user-attachments/assets/3b55834c-2d2c-401b-ac1b-77a9f2db0878" />
Test 1
<img width="1345" height="634" alt="Screenshot 2026-04-09 at 9 41 10 PM" src="https://github.com/user-attachments/assets/f9f7fa81-6266-4e4b-b049-ffed2df35ca6" />
Test2


# How to Run

1. Clone the repository
2. Create virtual environment
   - Use  python3 -m venv myenv
3. Activate
   - Use  source myenv/bin/activate for Mac
   - Use  myenv\Scripts\activate for Windows
4. Install dependencies
   - Use  pip install -r requirements.txt
5. Run
   - Use  python app.py


# Acknowledgement
This implementation was in part coded by ChatGPT 5.3.
  



