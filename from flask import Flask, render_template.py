from flask import Flask, render_template

app = Flask(__name__)

# Route for custom 404 error handling
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

# Your other routes and views go here

if __name__ == '__main__':
    app.run(debug=True)
    from flask import Flask
    from flask.testing import FlaskClient
    import pytest
    
    # Create a Flask app for testing
    @pytest.fixture
    def app():
        app = Flask(__name__)
        app.testing = True
        return app
    
    # Create a Flask client for testing
    @pytest.fixture
    def client(app):
        return app.test_client()
    
    # Test the custom 404 error page
    def test_404_page(client):
        response = client.get('/nonexistent-page')  # Make a request to a nonexistent page
        assert response.status_code == 404  # Assert that the response has a 404 status code
        assert b'404 - Page Not Found' in response.data  # Assert that the custom error page content is present in the response
    