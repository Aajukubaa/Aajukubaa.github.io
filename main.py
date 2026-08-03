from pyscript import document

# A standard Python dictionary holding your portfolio data. 
# You can easily edit the text inside the quotes to match your real projects!
projects_data = {
    "project_1": "<h3>📊 Data Analysis Project</h3><p>I used Python to analyze data and find interesting trends. It was a great learning experience.</p>",
    "project_2": "<h3>🤖 Automating Tasks</h3><p>I built a script that automatically organizes files on my computer, saving me hours of manual work.</p>",
    "project_3": "<h3>🐍 PyScript Website</h3><p>I built this very website! I used GitHub Pages and PyScript to run Python directly in the browser.</p>"
}

# This function grabs the HTML display box and updates what is inside it
def update_display(content):
    display_box = document.querySelector("#display-area")
    display_box.innerHTML = content

# These functions are triggered when the HTML buttons are clicked
def load_project_1(event):
    update_display(projects_data["project_1"])

def load_project_2(event):
    update_display(projects_data["project_2"])

def load_project_3(event):
    update_display(projects_data["project_3"])
