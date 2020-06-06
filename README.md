# Setup Project
1. `./scripts/init-project.sh`

# Run Project
1. Open 2 terminals at the project root
2. `./scripts/run-backend.sh`
3. `./scripts/run-frontend.sh`
4. Navigate to http://localhost:1234 in your favourite browser

Story
=====

As a user I would like to be able to click a button on a post so I can show that I like it.
I would like to be able to view the number of likes on the post.

Conditions of Satisfaction
==========================
- Visable like button which can be clicked to like a post
- Visable number of likes displayed for the post
- User must have clear instructions on how to run the application

Technical Requirements
======================
- MVVM (Model View ViewModel) pattern
- React (JavaScript) frontend
    - View and ViewModel
- Django (Python) backend
    - Model
- SQLite database
    - Persistance layer

Requirements for Consideration
==============================
- Use websockets for realtime updates
    - Django channels
- Mobile friendly
- Some thought into UI/UX
- Need to have something to like
    - Use an API for a quote
- TypeScript
- Production config
- Tests
    - Backend
        - pytest
    - Frontend
        - Jest
    - Integration
        - Selenium
- Users
- Linters and formatters

Plan
====
- Use parcel as the frontend bundler
    - Easy to setup and get running because it is low config
- Use react hooks
    - Modern practice and suite api requests well
- Use SCSS for styling
- Use django migrations
    - Makes testing django easier as it will set up a fresh database for us

Todo
====
- Pin npm packages
- Pin pip packages
