@app.route('/')
def index():
    users = User.get_all()
    print(friends)
    return render_template("index.html", all_friends = friends)
