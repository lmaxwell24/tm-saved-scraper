from pywinauto.application import Application
from pywinauto.findwindows import find_elements

from flask import Flask

app = Application()
app.connect(
    # path="com.dwabtech.TM"
    # pid=6948
    pid=6888
    # pid = 7033
)
print(app)
# get the item directly after the "saved match" text

def get_saved_match_text():
    return app.TM.by(parent=app.TM["Saved Match"].parent(), title_re="Q[0-9]*", found_index=-1).texts()[0][1]

print(get_saved_match_text())

flapp = Flask(__name__)

@flapp.route("/")
def index():
    return get_saved_match_text()

if __name__ == "__main__":
    flapp.run()


# print(app.TM["Saved Match"].wrapper_object())
# window = app.window(title="TM")

# controlwindow =window["Match Field Set"].wrapper_object()

# app.Field.Saved


# for element in find_elements(title="TM"):
#     print(element.)

