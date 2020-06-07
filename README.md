# Setup Project

1. `git clone git@github.com:SamDudley/likes.git`
2. `cd likes`
3. `./scripts/init-project.sh`

# Run Project

1. Open 2 terminals at the project root
2. `./scripts/run-backend.sh`
3. `./scripts/run-frontend.sh`
4. Navigate to http://localhost:1234 in your favourite browser

# Scripts

- `init-project.sh` - Setup the project
- `run-backend.sh` - Run the backend server
- `run-frontend.sh` - Run the frontend server
- `run-tests.sh` - Run all automated tests
- `run-formatters.sh` - Format code to pass pre-commit hook
- `./.githooks/pre-commit` - You can run the pre-commit hook directly to perform the checks without a commit

# Story

As a user I would like to be able to click a button on a post so I can show that I like it.
I would like to be able to view the number of likes on the post.

## Conditions of Satisfaction

- Visable like button which can be clicked to like a post
- Visable number of likes displayed for the post
- User must have clear instructions on how to run the application

## Technical Requirements

- MVVM (Model View ViewModel) pattern
- React (JavaScript) frontend
  - View and ViewModel
- Django (Python) backend
  - Model
- SQLite database
  - Persistance layer

# Plan

- Use parcel as the frontend bundler
  - Easy to setup and get running because it is low config
- Use react hooks
  - Modern practice and suite api requests well
- Use SCSS for styling
  - More powerful than standard CSS and allows us to use tailwind for quick UI design
- Use django migrations
  - Makes testing django easier as it will set up a fresh database for us

## Additions

- Auto formatters
  - Black (Python)
  - Prettier (JavaScript)
- Linters
  - Flake8 (Python)
  - ESLint (JavaScript)
- Type checking
  - Mypy (Python)
- Tests
  - Backend tests using the Django test framework
- All of the above integrated into a pre-commit git hook
- Docstrings and comments in the code
- TODOs in the code for further work
- Detailed README
- Mobile friendly
- Simple UI/UX design
- Scripts to make the project easy to setup, run and manage

## Rejected Additions:

- Users
- Use websockets for realtime updates (Django Channels)
- Use an API to generate a post
- TypeScript
- Production configuration
- Frontend tests (Jest)
- Integration tests (Selenium)
