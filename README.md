
# Web Accessibility Checker

## Overview

The Web Accessibility Checker is a Flask-based web application designed to analyze websites for accessibility issues. Users can input a website URL, and the application generates a report highlighting areas of concern regarding web accessibility standards. This tool aims to help developers improve the usability of their sites for people with disabilities, ensuring compliance with WCAG (Web Content Accessibility Guidelines).

## Features

- Analyze websites for accessibility issues.
- Generates reports in HTML format.
- Supports both mobile and desktop views for analysis.
- Simple interface for easy use.

## Prerequisites

Before installing, ensure you have the following installed on your system:

- Python 3.x
- Node.js and npm (for running Lighthouse)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Programmer-Arvind/Web-Accessibility-Checker.git

cd Web-Accessibility-Checker

```
2. Install flask:

```bash
pip install flask
```

3. Install Node.js dependencies:

```bash
npm install
```

## Running the Application

1. Start the Flask application 
```python
python app.py
```

2. Access the application at `http://127.0.0.1:5000/` in your web browser.

## Usage

1. Navigate to the Web Accessibility Checker homepage.
2. Enter the URL of the website you wish to analyze in the provided form.
3. Select the view mode (Mobile View or Desktop View).
4. Click "Check" to start the analysis.
5. Review the generated report for accessibility insights.

