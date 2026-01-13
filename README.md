# DocPhysics AI

Researchers, students, and professionals lose hours fixing Word formatting issues that software tools and grammar checkers cannot solve—such as broken page flow, orphan headings, floating images, extra blank pages, and misaligned sections that often cause paper rejections. Most authors focus on content, not "document physics," yet submission guidelines demand strict layout quality. 

**DocPhysics AI** fills this critical gap by automatically enforcing professional pagination rules, allowing users to concentrate on research and reporting instead of fighting Word.

## Core Capabilities
- **Advanced Pagination Logic**: Automatically resolves orphan headings, widow lines, and awkward page breaks.
- **Intelligent Asset Placement**: Ensures images and tables are positioned correctly relative to their references.
- **AI-Powered Structural Analysis**: Leverages Google Gemini to identify formatting inconsistencies and suggest structural improvements.
- **Journal-Standard Formatting**: Applies consistent typography (e.g., Times New Roman) and hierarchical heading styles aligned with academic standards.
- **Reference Integrity**: Scans for missing citations and verifies bibliographic formatting.

## Visual Documentation
![Dashboard Overview](file:///c:/Users/Hemhalatha%20V%20R/Hackathon/docx_formatter/AI-teaching-bot/Screenshot%202026-01-12%20144413.png)
*Professional interface for document analysis and formatting.*

<div align="center">
  <img src="file:///C:\Users\Hemhalatha V R\Hackathon\docx_formatter\AI-teaching-bot\Screenshot 2026-01-12 144659.png" width="400" />
  <img src="file:///c:/Users/Hemhalatha%20V%20R/Hackathon/docx_formatter/AI-teaching-bot/Screenshot%202026-01-12%20153754.png" width="400" />
</div>
*Left: AI Analysis | Right: Document Reconstruction*

## System Architecture
The repository is organized into a modular full-stack architecture:
- `backend/`: FastAPI server handling document processing and AI integration.
  - `app/services`: Core logic for DOCX manipulation and Gemini API interaction.
  - `app/routers`: RESTful API endpoints.
- `frontend/`: Modern React dashboard built with Vite and Tailwind CSS.
  - `src/components`: UI components designed for document workflow efficiency.

## Installation and Setup

### Prerequisites
- Python 3.9 or higher
- Node.js 16 or higher
- Google Gemini API Key

### Backend Configuration
1. Navigate to the backend directory:
   ```bash
   cd backend
   ```
2. Initialize and activate a virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\activate # Windows
   # source venv/bin/activate # Unix/macOS
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure environment variables in `.env`:
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```
5. Launch the server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Configuration
1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```
2. Install project dependencies:
   ```bash
   npm install
   ```
3. Start the development server:
   ```bash
   npm run dev
   ```

## Technical Foundation
DocPhysics AI is built on a robust stack designed for performance and reliability:
- **Backend**: FastAPI, Python-Docx, Google Generative AI
- **Frontend**: React, Vite, Tailwind CSS, PostCSS
- **AI Engine**: Google Gemini Pro
