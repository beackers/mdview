from flask import Flask, render_template
import markdown
import os

app = Flask(__name__)

@app.route("/view/<mdPage>")
def view(mdPage):
	# Define the path to your Markdown fil

	try:
		page = f"/storage/emulated/0/Documents/foxkids1/{mdPage}.md"
		with open(page, 'r', encoding='utf-8') as f:
			markdown_text = f.read()
		html_content = markdown.markdown(markdown_text)
		return render_template('view.html', content=html_content)
	except FileNotFoundError:
		print("exception caught! filenotfound error")
		return f"Markdown file not found. Page: {page}"

if __name__ == '__main__':
	app.run(debug=True)
