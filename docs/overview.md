# Project Overview

This project implements a mood-based recipe recommendation system with the following features developed according to Jira issues SCRUM-447 to SCRUM-453:

- **SCRUM-447:** Mood Input Interface and Recommendation Engine
  - Users input their current mood.
  - Backend maps mood to recipe categories and returns matched recipes efficiently.

- **SCRUM-448:** Recipe Browsing and Favorites Management
  - Browse recommended recipes with detailed views.
  - Add or remove recipes to/from user-specific favorites.

- **SCRUM-449:** User Profiles and Preferences Management
  - Maintain user profiles including dietary preferences.
  - Update user preferences via API and integrate preferences in filtering recommendations.

- **SCRUM-450:** User Interaction History Tracking
  - Track user mood and recipe interaction history.
  - Provide APIs to retrieve user history for analytics and improved recommendations.

- **SCRUM-451:** Social Sharing Integration (Future)
  - Planned OAuth social login.
  - Share moods and recipes on social platforms securely.

- **SCRUM-452:** AI-Enhanced Recommendation Engine (Future)
  - Integrate AI/ML models to personalize recommendations using historical and preference data.

- **SCRUM-453:** Multi-language Support and Localization (Future)
  - Support UI and content in multiple languages using localization frameworks.

# Architecture

- Backend: Flask API implementing core recommendation and user management features.
- Frontend: Simple HTML/JS UI for mood input and recipe browsing.
- Data Model: In-memory storage for demo; intended for database-backed implementation.

For detailed design and implementation specs, see [Design Document](https://docs.google.com/document/d/1xjYt9Z2Q4NwTpC6UipnEMX40ycDXHxts5yXqXUm9BNk/edit).

# How to Run

- Backend: `python backend/app.py`
- Frontend: Open `frontend/index.html` in a modern browser.

This repository is publicly available at: https://github.com/Alonaz101/idea-2025-11-14-3255
