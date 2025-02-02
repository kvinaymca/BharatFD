# GlobalFAQHub

GlobalFAQHub is a Django-based web application for managing FAQs (Frequently Asked Questions) with multi-language support. It includes features like WYSIWYG editor integration, REST API, caching, and automated translations.

## Features
- **Multi-language FAQ Management**: Add FAQs in multiple languages (English, Hindi, Tamil, Telugu).
- **WYSIWYG Editor**: Use Django CKEditor for rich text formatting.
- **REST API**: Fetch FAQs with language-specific translations.
- **Caching**: Improve performance using Redis for caching translations.
- **Automated Translations**: Automatically translate FAQs using Google Translate API.

## Installation

### Prerequisites
- Python 3.9 or higher
- Redis (for caching)
- Docker (optional, for containerization)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/GlobalFAQHub.git
   cd GlobalFAQHub
