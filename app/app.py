from flask import Flask, request,  Response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upscaler():
    return """
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
    </form>
    """