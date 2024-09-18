from flask import Flask, request, jsonify, render_template
import webbrowser as web
import wikipedia as wiki
import datetime as dt

app = Flask(__name__)

def chatbot_response(user_input):
    responses = {
        "hello" : "hi there",
        "how are you" : "I am doing fine",
        "thanks" : "no worries",
        "nice": "i guess output was correct",
        "yo": "hey",
        "how you doing": "better than never",
        "-h": '''
            1. for searching enter -s (your search query)
            2. for youtube enter -yt (your yt query)
            3. for wikipedia search enter -wiki (your search query)
            note. do not forget to leave a whitespace between above commands
        ''',
        "what can you do" : "type -h",
        "jokes": "none of jokes are programmed"
    }

    if user_input not in responses:

        if "-s " in user_input:
            result = ""
            search_raw_url = "https://www.google.com/search?q="
            for i in range(3, len(user_input)):
                result += user_input[i]
            splitURL = "+".join(result.split())
            sQuery = search_raw_url + splitURL
            web.open_new_tab(sQuery)
            return f"finding results for {result} query"
        
        elif "-yt " in user_input:
            result = ""
            yt_raw_url = "https://www.youtube.com/results?search_query="
            for i in range(4, len(user_input)):
                result += user_input[i]

            splitURL = "+".join(result.split())
            ytQuery = yt_raw_url + splitURL
            web.open_new_tab(ytQuery)
            return f"Searching for {result} videos"
        
        elif "-wiki " in user_input:
            result = ""
            for i in range(6, len(user_input)):
                result += user_input[i]
            data = wiki.summary(result)
            # print(data)
            return data

        elif "-o outlook" in user_input:
            web.open_new_tab("https://outlook.office.com/mail/?actSwt=true")
            return "Opening outlook"

        elif "-o classroom" in user_input:
            web.open_new_tab("https://classroom.google.com/")
            return "Opening classroom"

        else:
            return "Command not found..."

    else:
        response = responses.get(user_input.lower(), "Command not found...")
        return response

@app.route('/')
def index():
    return render_template('FridayUI.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_query = request.json.get('message')
    bot_response = chatbot_response(user_query)
    return jsonify({"reply": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
