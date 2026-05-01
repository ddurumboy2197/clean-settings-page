class SettingsPage:
    def __init__(self):
        self.sections = {
            "profile": {
                "title": "Profile",
                "fields": [
                    {"label": "Name", "type": "text"},
                    {"label": "Email", "type": "email"},
                    {"label": "Phone Number", "type": "tel"}
                ]
            },
            "security": {
                "title": "Security",
                "fields": [
                    {"label": "Password", "type": "password"},
                    {"label": "Confirm Password", "type": "password"}
                ]
            },
            "notifications": {
                "title": "Notifications",
                "fields": [
                    {"label": "Email Notifications", "type": "checkbox"},
                    {"label": "Push Notifications", "type": "checkbox"}
                ]
            }
        }

    def display_settings(self):
        for section in self.sections.values():
            print(f"**{section['title']}**")
            for field in section["fields"]:
                if field["type"] == "checkbox":
                    print(f"  * {field['label']}: {field['type']}")
                else:
                    print(f"  * {field['label']}: {field['type']}")

    def save_settings(self):
        for section in self.sections.values():
            for field in section["fields"]:
                if field["type"] == "checkbox":
                    print(f"  * {field['label']}: {field['type']}")

def main():
    settings = SettingsPage()
    settings.display_settings()
    settings.save_settings()

if __name__ == "__main__":
    main()
```

```python
# settings.html
<!DOCTYPE html>
<html>
<head>
    <title>Settings</title>
</head>
<body>
    <h1>Settings</h1>
    <div id="profile">
        <h2>Profile</h2>
        <form>
            <label for="name">Name:</label>
            <input type="text" id="name" name="name"><br><br>
            <label for="email">Email:</label>
            <input type="email" id="email" name="email"><br><br>
            <label for="phone">Phone Number:</label>
            <input type="tel" id="phone" name="phone"><br><br>
        </form>
    </div>
    <div id="security">
        <h2>Security</h2>
        <form>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password"><br><br>
            <label for="confirm_password">Confirm Password:</label>
            <input type="password" id="confirm_password" name="confirm_password"><br><br>
        </form>
    </div>
    <div id="notifications">
        <h2>Notifications</h2>
        <form>
            <label for="email_notifications">Email Notifications:</label>
            <input type="checkbox" id="email_notifications" name="email_notifications"><br><br>
            <label for="push_notifications">Push Notifications:</label>
            <input type="checkbox" id="push_notifications" name="push_notifications"><br><br>
        </form>
    </div>
</body>
</html>
```

```python
# settings.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/settings")
def settings():
    return render_template("settings.html")

if __name__ == "__main__":
    app.run(debug=True)
