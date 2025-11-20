# 🚀 Quick Start Guide

Get up and running in 5 minutes!

## Step 1: Setup Environment
```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

## Step 2: Install Dependencies
```bash
# Install Python packages
pip install -r requirements.txt

# Install Playwright browser
playwright install chromium
```

## Step 3: Run the Project
```bash
python web_scraper_analytics.py
```

## Step 4: View Results
Check the `output/` folder for:
- Excel report (`.xlsx`)
- Power BI dataset (`.csv`)
- JSON export (`.json`)
- Summary report (`.txt`)

## Step 5: Import to Power BI
1. Open Power BI Desktop
2. Get Data → Text/CSV
3. Select the generated `.csv` file
4. Create your visualizations!

## Troubleshooting

**Issue**: Module not found error
**Solution**: Run `pip install -r requirements.txt` again

**Issue**: Playwright browser not found
**Solution**: Run `playwright install chromium`

**Issue**: Permission denied on output folder
**Solution**: Create the folder manually: `mkdir output`

## What This Project Does

1. **Scrapes** product data from an e-commerce website
2. **Processes** the data (cleaning, calculations, categorization)
3. **Generates** a formatted Excel report with charts
4. **Exports** Power BI ready datasets
5. **Creates** summary statistics and reports

## Customization

Want to scrape a different website? Edit line 60 in `web_scraper_analytics.py`:
```python
await page.goto('YOUR_WEBSITE_URL')
```

Want to change output settings? Edit `config.py`

## Resume Tips

Mention these skills:
- Python automation
- Web scraping (Playwright)
- Data processing (Pandas)
- Excel automation (OpenPyXL)
- Power BI integration
- Async programming

## Next Steps

- Add your own target websites
- Customize the Excel formatting
- Create Power BI dashboards
- Schedule automated runs
- Add email notifications

---

**Need help?** Check the full README.md for detailed documentation.
