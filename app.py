from flask import Flask, render_template, request, flash
import requests
import validators

app = Flask(__name__)
app.secret_key = "supersecretkey"  # For flash messages

@app.route("/", methods=["GET", "POST"])
def index():
    short_url = None
    error = None
    if request.method == "POST":
        long_url = request.form.get("long_url")
        # Validate URL
        if not validators.url(long_url):
            error = "Invalid URL. Please enter a valid URL."
        else:
            try:
                # Call TinyURL API
                response = requests.get(f"http://tinyurl.com/api-create.php?url={long_url}")
                if response.status_code == 200:
                    short_url = response.text
                else:
                    error = "Failed to shorten URL. Try again later."
            except requests.RequestException:
                error = "Network error. Please try again."
    return render_template("index.html", short_url=short_url, error=error)

if __name__ == "__main__":
    app.run(debug=True)
