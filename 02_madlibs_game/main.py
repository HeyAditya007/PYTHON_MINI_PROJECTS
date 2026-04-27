#  SIMPLE MADLIBS GAME WITH A GHOST GIRL LOVE STORY
import time
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QVBoxLayout, QPushButton, QLineEdit, QLabel, QTextEdit, QHBoxLayout, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon




app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Madlibs love  Horror game")
window.setWindowIcon(QIcon("image.123"))
window.setGeometry(0, 0 ,300  ,300 )
window.setStyleSheet("""
QWidget {
    background-color: #0d0d0d;
    color: white;
    font-family: Consolas;
}

QLineEdit {
    background-color: #1a1a1a;
    border: 1px solid #ff0000;
    padding: 5px;
    color: white;
}

QPushButton {
    background-color: #990000;
    border: none;
    padding: 10px;
    color: white;
}

QPushButton:hover {
    background-color: #cc0000;
}
""")

main_layout = QVBoxLayout()
title = QLabel("HORROR LOVE")
subtitle = QLabel("MADLIBS GAME")


title.setStyleSheet("font-size: 40px; color: #ff1a1a; font-weight: bold;")
subtitle.setStyleSheet("font-size: 20px; color: white; margin-bottom: 10px;")
title.setAlignment(Qt.AlignCenter)
subtitle.setAlignment(Qt.AlignCenter)

main_layout.addWidget(title)
main_layout.addWidget(subtitle)

# HORIZONTAL SPLIT
content_layout = QHBoxLayout()

# LEFT PANEL (INPUTS)
left_panel = QFrame()
left_layout = QVBoxLayout()
def create_input(placeholder):
    inp = QLineEdit()
    inp.setPlaceholderText(placeholder)
    return inp

scary_adjective_input = QLineEdit()
scary_adjective_input.setPlaceholderText("scary adjective")       
       
scary_place_input = QLineEdit()
scary_place_input.setPlaceholderText("scary place ")

danger_adjective_input = QLineEdit()
danger_adjective_input.setPlaceholderText("danger adjective")

strange_sound_input = QLineEdit()
strange_sound_input.setPlaceholderText("strange sound")
       
sad_adjective_input = QLineEdit() 
sad_adjective_input.setPlaceholderText("sad adjective")       
       
object_input = QLineEdit()
object_input.setPlaceholderText("object")

coruscant_adjective_input = QLineEdit()
coruscant_adjective_input.setPlaceholderText("coruscant adjective ")
       
noun_input = QLineEdit()
noun_input.setPlaceholderText("noun")


emotion_input = QLineEdit()
emotion_input.setPlaceholderText("emotion")
       
verb_input = QLineEdit()
verb_input.setPlaceholderText("verb")



adjective1_input = QLineEdit()
adjective1_input.setPlaceholderText("adjective 1")
       
emotion1_input = QLineEdit()
emotion1_input.setPlaceholderText("emotion 1")
      
      
verb1_input = QLineEdit()
verb1_input.setPlaceholderText("verb 1")
       
       
       
adjective2_input = QLineEdit()
adjective2_input.setPlaceholderText("adjective 2")
       
adjective3_input = QLineEdit()
adjective3_input.setPlaceholderText("adjective 3")
       
       
emotion2_input = QLineEdit()
emotion2_input.setPlaceholderText(" emotion 2")
       
       
supernaturalbeing_input = QLineEdit()
supernaturalbeing_input.setPlaceholderText("super natural beings")
       
       
emotion3_input = QLineEdit()
emotion3_input.setPlaceholderText("emotion 3")
       
emotion4_input = QLineEdit()
emotion4_input.setPlaceholderText(" emotion 4")
       
       
adjective4_input = QLineEdit()
adjective4_input.setPlaceholderText("adjective 4 ")

output = QTextEdit()
output.setReadOnly(True)


generate_button = QPushButton("Generate story")
clear_button = QPushButton("play agian")

layout = QHBoxLayout()

def generate_story():
    story = f"""It was a {scary_adjective_input.text()} night when I decided to walk through the {scary_place_input.text()} alone.
The air felt {danger_adjective_input.text()}, and every sound made my heart beat rapidly.

Suddenly, I heard a {strange_sound_input.text()} behind me.
When I turned around, I saw a {sad_adjective_input.text()} girl standing near a {object_input.text()}.

Her eyes were {coruscant_adjective_input.text()}, and her voice sounded like a {noun_input.text()} whispering in the dark.
Even though I felt {emotion_input.text()}, I couldn’t stop myself from {verb_input.text()} closer to her.

She said she had been waiting for someone {adjective1_input.text()} for a very long time.
Instead of running away, I felt something {emotion1_input.text()} in my heart.

We started to {verb1_input.text()} together under the {adjective2_input.text()} sky, as if time had stopped.
She smiled in a way that felt both {adjective3_input.text()} and {emotion2_input.text()}.

Then she softly said, “No one has ever stayed this long… you are different.”

I realized she wasn’t just any girl… she was a {supernaturalbeing_input.text()}.

But instead of fear, I felt {emotion3_input.text()}.

As the night faded, she looked at me with {emotion4_input.text()} and whispered,
“Will you come back tomorrow?”

And for the first time, the darkness didn’t feel {adjective4_input.text()} anymore."""
    
    output.setText(story)

def clear_all():
    for widget in window, findChildren(QLineEdit):
        widget.clear()
    output.clear()    

generate_button.clicked.connect(generate_story)
clear_button.clicked.connect(clear_all)

for widget in [ 
    scary_adjective_input, scary_place_input, danger_adjective_input,
    strange_sound_input, sad_adjective_input, object_input,
    coruscant_adjective_input, noun_input, emotion_input, verb_input,
    adjective1_input, emotion1_input, verb1_input,
    adjective2_input, adjective3_input, emotion2_input,
    supernaturalbeing_input, emotion3_input, emotion4_input,
    adjective4_input,
    generate_button, clear_button, output
]:
    layout.addWidget(widget)











       
   




window.setLayout(layout)
window.show()
sys.exit(app.exec_())  #code after this don't run this is the last stop of your code 

