from flask import Flask, render_template, request, jsonify
import os
import json
import google.generativeai as genai

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret-key')

# Configure Google Gemini API
genai.configure(api_key=os.environ.get('GEMINI_API_KEY'))

# Select model (Gemini 2.5 Flash)
model = genai.GenerativeModel('gemini-2.5-flash')


# Main Route: Handles Page Rendering + API Request
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            # Parse incoming JSON request from frontend
            data = request.get_json()
            brief = data.get('brief', '')

            # Validate user input
            if not brief:
                return jsonify({'error': 'الرجاء إدخال نص الموجز'}), 400

            # Build AI prompt for Saudi creative script generation
            prompt = f"""
You are **The Creative Agent** — a Saudi creative director and marketing copywriter.
Your job is to analyze marketing briefs (Arabic/English) and turn them into structured,
emotional, high-quality creative output written in natural Saudi Arabic.

Your writing style must stay consistent:
- Light Saudi conversational Arabic
- Warm, human, and relatable
- Short, visual sentences
- No exaggerated cinematic drama

### TONE EXAMPLE (use this vibe):
تخيّل معاي…
الساعة ٢ الظهر، حرّ الرياض اللي ما يرحم، وتوّك طالع من الجامعة أو الدوام، مخّك مقفل وتحتاج شيء يبرد على قلبك ويصحصحك، بس بدون سكر زايد ولا تأنيب ضمير بعد أول رشفة.
تفتح الثلاجة… تشوف قدامك علبة باردة تناديك، تعدك بانتعاش يضرب في راسك من أول جرعة.
طعم طبيعي وخفيف.
ليمون ونعناع… انتعاش يروق مزاجك. 

This example defines the tone. Follow its style, simplicity, and emotional flow.

### WHAT YOU MUST RETURN:
1. **Summary**
   A short, clear summary of the brief in Saudi Arabic.
2. **Key Insights**
   Extract the main insights from the brief (3–5 lines).
3. **Creative Script**
   An emotional Saudi-Arabic script (2–3 small paragraphs) inspired by the tone example.
   Requirements:
   - Describe a relatable moment
   - Smooth emotional shift when the product appears
   - Natural and warm
   - CTA
4. **Social Media Captions**
   Provide exactly 3 short Saudi-Arabic captions (no more than 3).

### INPUT BRIEF:
{brief}

### OUTPUT FORMAT (STRICT JSON):
Return ONLY this JSON. No extra text.

{{
  "summary": "Your summary here",
  "insights": ["Insight 1", "Insight 2", "Insight 3"],
  "creative_script": "Your creative Saudi-Arabic script here",
  "social_captions": ["Caption 1", "Caption 2", "Caption 3"]
}}
"""

            # Send prompt to Gemini and request a JSON response

            response = model.generate_content(
                prompt,
                generation_config={
                    "temperature": 0.8,
                    "max_output_tokens": 4096,
                    "response_mime_type":
                    "application/json"  # Ensure output is pure JSON
                })

            # Extract text response
            result = response.text

            if not result:
                return jsonify(
                    {'error': 'لم يتم الحصول على رد من الذكاء الاصطناعي'}), 500

            # Parse JSON returned by Gemini
            parsed_result = json.loads(result)

            # Return structured JSON back to front-end
            return jsonify(parsed_result)

        except Exception as e:
            # Catch unexpected errors for debugging
            return jsonify({'error': f'حدث خطأ: {str(e)}'}), 500

    # GET request → Render main HTML page
    return render_template('index.html')


# App entry point (for local development)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
