# Creative Agent - الوكيل الإبداعي

## Overview

A web application that transforms marketing briefs into creative Arabic content using Google's Gemini AI. The system analyzes briefs in Arabic, English, or mixed languages and generates Saudi-style creative outputs including summaries, insights, scripts, and social media captions. The interface is designed with RTL (right-to-left) support and features a clean, NOB-inspired aesthetic suitable for creative agency workflows.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture

**Technology Choice**: Vanilla HTML/CSS/JavaScript
- **Rationale**: Lightweight, no build process required, fast iteration for simple interactive forms
- **RTL Support**: CSS direction properties and Arabic font (Cairo) loaded from Google Fonts
- **Design Pattern**: Single-page application with client-side form handling and AJAX requests
- **Styling Approach**: Custom CSS with NOB-inspired minimalist design, featuring a hero section with overlay effects

**Key Components**:
- Form-based input system for client name, product description, and target audience
- Real-time error handling and loading states
- Dynamic result rendering

### Backend Architecture

**Framework**: Flask (Python)
- **Rationale**: Lightweight Python web framework ideal for simple API endpoints and template rendering
- **Request Handling**: Supports both GET (page render) and POST (AJAX API) requests on single route
- **Response Format**: JSON for API responses with error handling

**AI Integration Pattern**:
- Direct synchronous calls to Google Gemini API
- Structured prompt engineering for consistent Saudi Arabic creative outputs
- JSON response parsing from AI model

**Configuration Management**:
- Environment variables for sensitive data (GEMINI_API_KEY, SESSION_SECRET)
- Fallback values for development

### Content Generation Strategy

**Prompt Engineering**:
- Detailed system prompt defining tone, style, and output structure
- Tone consistency enforced through example-based learning
- Structured output requirements (Summary, Key Insights, Creative Script, Social Captions)
- Saudi Arabic dialect specification for cultural relevance

**Output Structure**:
1. Executive summary in Saudi Arabic
2. 3-5 key insights extraction
3. 2-3 paragraph emotional script with CTA
4. 3 social media captions optimized for Saudi audience

### Security Considerations

**Secrets Management**:
- API keys stored in environment variables (not in code)
- Session secret for Flask security features
- No user authentication (single-user or open-access model)

## External Dependencies

### AI Service
- **Google Gemini 2.5 Flash API** (`google-generativeai==0.8.3`)
  - Primary AI model for content generation
  - Requires `GEMINI_API_KEY` environment variable
  - Configured via `genai.configure()` method

### Python Framework & Libraries
- **Flask 3.0.0**: Web application framework
  - Handles routing, templating, JSON responses
  - Provides development server
  
- **python-dotenv 1.0.0**: Environment variable management
  - Loads `.env` file configurations (implied usage)

### Frontend Resources
- **Google Fonts**: Cairo font family
  - Weights: 400, 600, 700, 800
  - Optimized for Arabic typography
  - Loaded via CDN

### Static Assets
- **hero-bg.png**: Hero section background image
  - Local asset in `/static` directory
  - Used with CSS overlay effects

### Deployment Considerations
- No database dependency (stateless application)
- No persistent data storage required