from flask import Flask, render_template

if __name__ == "__main__":
    # create flask app
    app = Flask(__name__)
    # register endpoints

    @app.route("/", methods=["GET"])
    def get_index():
        """
        Each call to the API, which doesn't start with `/api` will be covered by this function providing the index.html
        to the caller. The index.html will load the index.js in the browser, which will render the frontend. The
        frontend will then decide what view to render. The backend is not responsible for that.

        **IMPORTANT**
        This function needs to be updated whenever new frontend routes are added to the React router. You can provide
        multiple @app.route(..) lines for multiple frontend routes that all just return the frontend (because the
        frontend has it's own router which decides what page to render)

        :return: the index.html as file (basically delivering the whole frontend)
        """
        return render_template("index.html")

    # prevent caching of the frontend during development
    @app.after_request
    def add_header(r):
        """
        Add headers to both force latest IE rendering engine or Chrome Frame,
        and also to cache the rendered page for 10 minutes.
        """
        r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
        r.headers["Pragma"] = "no-cache"
        r.headers["Expires"] = "0"
        r.headers['Cache-Control'] = 'public, max-age=0'
        return r

    # start flask app
    app.run(host='0.0.0.0', port=5555)
