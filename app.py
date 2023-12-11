from flask import Flask, render_template, request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

app = Flask(__name__)

# Set your API key and OAuth client ID and secret
API_KEY = 'AIzaSyDCSF_qqhoQoXoAly5qnGMR-ZioJWq7d5opython'
CLIENT_ID = '48155095065-v2548g2qafoprq5qn5lkusfaap041d6m.apps.googleusercontent.com'
CLIENT_SECRET = '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'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

# Video ID entered by the user
video_id = ''

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_config({
        "web": {
            "client_id": CLIENT_ID,
            "project_id": "youtubecustomevideoplayer",
            "auth_uri": "https://accounts.google.com/o/oauth2/auth",
            "token_uri": "https://oauth2.googleapis.com/token",
            "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
            "client_secret": CLIENT_SECRET
        }
    }, SCOPES)
    credentials = flow.run_local_server(port=0)
    return build('youtube', 'v3', credentials=credentials)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play', methods=['POST'])
def play_video():
    global video_id
    video_id = request.form['video_id']
    return render_template('play.html', video_id=video_id, api_key=API_KEY)

if __name__ == '__main__':
    app.run(debug=True)
