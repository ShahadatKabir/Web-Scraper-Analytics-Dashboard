"""
Configuration file for Web Scraper Analytics
Modify these settings to customize the scraper behavior
"""

# Scraper Configuration
SCRAPER_CONFIG = {
    'headless': True,  # Run browser in headless mode
    'timeout': 30000,  # Page load timeout in milliseconds
    'wait_for': 'networkidle',  # Wait condition: 'load', 'domcontentloaded', 'networkidle'
    'retry_attempts': 3,  # Number of retry attempts on failure
    'delay_between_requests': 1,  # Delay in seconds between requests
}

# Target URLs - Add your own websites here
TARGET_URLS = [
    'https://webscraper.io/test-sites/e-commerce/allinone',
    # Add more URLs as needed
]

# Excel Configuration
EXCEL_CONFIG = {
    'header_color': '366092',  # Header background color (hex)
    'header_font_color': 'FFFFFF',  # Header font color (hex)
    'max_column_width': 50,  # Maximum column width
    'date_format': 'YYYY-MM-DD HH:MM:SS',
}

# Data Processing Configuration
DATA_CONFIG = {
    'price_categories': {
        'bins': [0, 50, 200, 500, float('inf')],
        'labels': ['Budget', 'Mid-Range', 'Premium', 'Luxury']
    },
    'remove_duplicates': True,
    'fill_missing_values': True,
}

# Output Configuration
OUTPUT_CONFIG = {
    'directory': './output',
    'file_prefix': 'product_analysis',
    'include_timestamp': True,
    'formats': ['xlsx', 'csv', 'json'],  # Output formats to generate
}

# Power BI Configuration
POWERBI_CONFIG = {
    'date_format': 'iso',  # Date format for Power BI: 'iso' or 'epoch'
    'include_metadata': True,
    'optimize_datatypes': True,
}

# Logging Configuration
LOGGING_CONFIG = {
    'level': 'INFO',  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    'format': '%(asctime)s - %(levelname)s - %(message)s',
    'save_to_file': True,
    'log_file': 'scraper.log',
}

# Email Notification (for future enhancement)
EMAIL_CONFIG = {
    'enabled': False,
    'smtp_server': 'smtp.gmail.com',
    'smtp_port': 587,
    'sender_email': '',
    'receiver_email': '',
    'send_on_completion': True,
    'send_on_error': True,
}

# Database Configuration (for future enhancement)
DATABASE_CONFIG = {
    'enabled': False,
    'type': 'postgresql',  # postgresql, mysql, mongodb, sqlite
    'host': 'localhost',
    'port': 5432,
    'database': 'scraper_db',
    'user': '',
    'password': '',
}
