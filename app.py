from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


def get_response(message, language):
    """Choose a short reply using straightforward phrase matching."""
    text = message.strip().lower()

    if language == "sanskrit":
        if any(word in text for word in ("नमस्ते", "नमस्कार", "प्रणाम")):
            return "नमस्ते! भवतः सन्देशं पठित्वा अहं प्रसन्नः।"
        elif any(word in text for word in ("त्वं कः", "भवान् कः", "तव नाम", "किमसि")):
            return "अहं सूत्रबॉट् अस्मि, सरलः संवादसहायकः।"
        elif any(word in text for word in ("किं करोषि", "किं कर्तुं", "कार्याणि", "किं शक्नोषि")):
            return "अहं अभिवादनं, साहाय्यं, सामान्यप्रश्नान् च उत्तरितुं शक्नोमि।"
        elif any(word in text for word in ("कथम् असि", "कथं असि", "कुशलम्", "कथं भवति")):
            return "अहं कुशलः अस्मि। भवतः कथम्?"
        elif any(word in text for word in ("साहाय्य", "मदद", "सहाय्य", "उपकार")):
            return "कृपया अभिवादनं, परिचयं, अथवा मम कार्यं विषये पृच्छतु।"
        elif any(word in text for word in ("धन्यवाद", "कृतज्ञ", "आभार")):
            return "स्वागतम्! भवतः साहाय्यं कर्तुं मम हर्षः।"
        elif any(word in text for word in ("पुनर्मिलामः", "विदाय", "गच्छामि", "शुभरात्रि")):
            return "पुनर्मिलामः! भवतः दिनं शुभं भवतु।"
        else:
            return "क्षम्यताम्, एतत् वाक्यं मया न अवगतम्। अन्येन प्रकारेण पृच्छतु।"

    if any(word in text for word in ("hi", "hello", "hey", "good morning", "good evening")):
        return "Hello! Nice to have you here. What would you like to chat about?"
    elif any(word in text for word in ("who are you", "your name", "what are you")):
        return "I’m SutraBot, a small assistant built for simple conversations."
    elif any(word in text for word in ("what can you do", "your features", "what do you do", "capabilities")):
        return "I can respond to greetings, basic questions, requests for help, and farewells in English or Sanskrit."
    elif any(word in text for word in ("how are you", "how's it going", "how are things")):
        return "I’m running smoothly, thanks for asking. How are things with you?"
    elif any(word in text for word in ("help", "assist", "support")):
        return "Try asking who I am, what I can do, or simply say hello. You can also switch to Sanskrit."
    elif any(word in text for word in ("thank you", "thanks", "thx")):
        return "You’re welcome! I’m glad I could help."
    elif any(word in text for word in ("bye", "goodbye", "see you", "farewell")):
        return "Goodbye for now. Come back whenever you feel like chatting!"
    else:
        return "I don’t know that one yet. Try a greeting, ask for help, or ask what I can do."


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = data.get("message", "")
    language = data.get("language", "english")

    if not isinstance(message, str) or not message.strip():
        return jsonify({"response": "Please enter a message before sending."}), 400
    if language not in ("english", "sanskrit"):
        language = "english"

    return jsonify({"response": get_response(message, language)})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
