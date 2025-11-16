# مُبدِع

**AI-Powered Creative Marketing Brief Analyzer for Saudi Arabian Brands**

مُبدِع is a web-based tool that transforms marketing briefs into structured creative outputs using Google Gemini AI. It analyzes briefs written in Arabic, English, or mixed languages and generates authentic Saudi-Arabic creative content including insights, cinematic scripts, and social media captions.

---

##  Overview

This tool is designed for creative agencies, marketers, and content creators working with Saudi Arabian brands. It takes unstructured marketing briefs and converts them into polished, ready-to-use creative deliverables in Saudi conversational Arabic.

**What it does:**
- Analyzes marketing briefs 
- Extracts key insights and strategic points
- Generates emotional Saudi-Arabic creative scripts with storytelling
- Creates social media captions optimized for Saudi audiences
- Provides structured JSON output for easy integration

---

## Features

- **Brief Analysis**: Paste marketing briefs in Arabic, English, or both
- **Intelligent Insights**: Extracts 3-5 key strategic points from the brief
- **Creative Scripting**: Generates 2-3 paragraph Saudi-style cinematic scripts with natural storytelling and CTAs
- **Social Media Captions**: Creates 3 platform-ready Saudi-Arabic captions
- **RTL Arabic Interface**: Clean, modern web UI with right-to-left support
- **Real-time Processing**: Instant AI-powered generation with loading states
- **Consistent Tone**: Maintains warm, conversational Saudi Arabic style across all outputs

---

## Tech Stack

| Component | Technology |
|-----------|-----------|
| **Backend** | Python 3.11+ |
| **Web Framework** | Flask |
| **AI Model** | Google Gemini 2.5 Flash |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Styling** | Custom CSS  |
| **API Integration** | Google Generative AI SDK |

---

## Installation & Setup

### Prerequisites
- Python 3.11 or higher
- Google Gemini API key (free tier available)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <project-folder>
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:
```bash
GEMINI_API_KEY=your_gemini_api_key_here
SESSION_SECRET=your_random_secret_key_here
```

**Getting your API key:**
- Visit [Google AI Studio](https://aistudio.google.com/app/apikey)
- Create a new API key (free tier available)
- Copy and paste it into your `.env` file

### 5. Run the Application
```bash
python main.py
```

The application will start on `http://localhost:5000`

---

## Project Structure

```
مُبدِع/
│
├── main.py                 # Flask application & API routes
├── requirements.txt        # Python dependencies
├── .env.example           # Environment variables template
├── .gitignore             # Git ignore configuration
├── README.md              # This file
│
├── templates/
│   └── index.html         # RTL Arabic web interface
│
└── static/
    └── style.css          # Custom styling
```


---

## How It Works

### Step-by-Step Flow

1. **User Input**
   - User fills out a form with client name, product description, target audience, and desired tone
   - Form data is collected and formatted into a marketing brief string

2. **API Request**
   - Frontend sends POST request to Flask backend with brief data
   - Backend receives JSON payload with the marketing brief

3. **AI Processing**
   - Flask sends structured prompt to Google Gemini 2.5 Flash API
   - Prompt includes tone examples, output format requirements, and the user's brief
   - AI model processes the brief using creative temperature (0.8) and max tokens (4096)

4. **Response Parsing**
   - Gemini returns structured JSON with 4 fields:
     - `summary`: Executive summary in Saudi Arabic
     - `insights`: Array of 3-5 key strategic insights
     - `creative_script`: 2-3 paragraph emotional script with CTA
     - `social_captions`: Array of 3 social media captions

5. **Frontend Rendering**
   - Flask returns JSON to frontend
   - JavaScript dynamically renders results in clean, organized cards
   - User can copy outputs for immediate use

### API Configuration

```python
model = genai.GenerativeModel('gemini-2.5-flash')

generation_config = {
    "temperature": 0.8,           # Creative, varied outputs
    "max_output_tokens": 4096,    # Prevents truncation
    "response_mime_type": "application/json"  # Structured output
}
```

---

##  Writing Style

The AI maintains a consistent Saudi-Arabic conversational style:

- **Light Saudi dialect** (not heavy formal Arabic)
- **Warm and relatable** (human, not robotic)
- **Visual storytelling** (short sentences that paint mental images)
- **Natural flow** (no exaggerated drama)
- **Emotional connection** followed by clear call-to-action

**Example Tone:**
```
تخيّل معاي…
الساعة ٢ الظهر، حرّ الرياض اللي ما يرحم، وتوّك طالع من الجامعة...
```

This tone example is embedded in the prompt to ensure consistency across all generated content.

---



## Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| `GEMINI_API_KEY` | Yes | Your Google Gemini API key from AI Studio |
| `SESSION_SECRET` | No | Flask session secret (defaults to 'dev-secret-key' if not set) |

---

##  Usage Example

1. Open the web interface
2. Fill in the form:
   - **Client Name**: عصير ليمون
   - **Product Description**: مشروب طبيعي منعش بنكهة الليمون والنعناع
   - **Target Audience**: شباب سعودي (18-30 سنة)
   - **Tone**: مرح، منعش، شبابي
3. Click "تحليل "
4. Receive structured output:
   - Executive summary
   - Key insights
   - Creative script
   - Social media captions

---

##  Contributing

This project was developed as a technical assignment. Contributions, issues, and feature requests are welcome.

---

##  License

This project is available for personal and commercial use.


---

**Built for Saudi Arabian creative professionals by Shrouq Aldalbahi**
