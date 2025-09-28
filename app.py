from flask import Flask, render_template, request, jsonify
import markdown
import os

app = Flask(__name__)

@app.route("/view", methods=['GET'])
def view():
	return render_template("view.html")

@app.route("/view", methods=["POST"])
def viewPage():
	data = request.json
	filename = data['filename']
	try:
		with open(filename) as file:
			text = file.read()
	except FileNotFoundError:
		return jsonify({
            "text": "filenotfound"
            }), 404
	mdText = markdown(text)
	return jsonify({"text": mdText})


if __name__ == '__main__':
	app.run(debug=True)
