from app import app

def main():
    """
    Starts the Flask application on port 5003 with debugging enabled.
    """
    app.run(port=5006, debug=True)

if __name__ == '__main__':
    main()
