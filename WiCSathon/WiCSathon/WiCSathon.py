from flask import Flask

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def show_world():
    return app.send_static_file('hackathon.html')




@app.route('/study', methods=['POST'])
def hello_world():
    html = html_header("<h1>Favorite Study Spots</h1>")
    html += """
    <form = action="/map" method="post">
    First Name: <input type="text" name="fname">
    Last Name: <input type="text" name="lname">
    <input type="submit" value="submit">
    </form>
    """
    html += html_closing()
    return html

@app.route('/map', methods=['POST'])
def displayInfo():
    html = """"""
    html += html_header("""<h1> Results </h1>""")
    html += html_closing()
    return html

def html_header(title):
    header = """
    <html>
    <header>
    <link rel="stylesheet" type="text/css" href="/static/DarkChocolate.css">
    """
    header += title
    header += """
    </header>
    <body class="info_body">
    """
    return header

def html_closing():
    closing = """
    </body>
    </html>
    """
    return closing

if __name__ == '__main__':
    app.run()
