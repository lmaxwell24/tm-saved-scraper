from pywinauto.application import Application
from pywinauto.findwindows import find_elements

app = Application()
app.connect(
    # path="com.dwabtech.TM"
    # pid=6948
    pid=6888
    # pid = 7033
)
print(app)
# get the item directly after the "saved match" text
print(app.TM.by(parent=app.TM["Saved Match"].parent(), best_match="Q", found_index=-1).texts())
