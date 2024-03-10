import requests
from bs4 import BeautifulSoup

def extract_text_from_website(url):
    try:
        # Fetch the HTML content of the website
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text from the HTML
        text = soup.get_text(separator='\n')

        # Remove empty lines
        text = "\n".join([line for line in text.split("\n") if line.strip()])

        return text
    except Exception as e:
        print(f"Error occurred while processing {url}: {e}")
        return None

def main():
    # List of websites to extract text from
    websites = [
        # tips to buy a house
        "https://www.nerdwallet.com/article/mortgages/tips-for-first-time-home-buyers",
        "https://www.rocketmortgage.com/learn/first-time-home-buyer-tips",
        "https://www.bankrate.com/real-estate/how-to-buy-a-house/",
        "https://www.nerdwallet.com/article/mortgages/home-buying-checklist-steps-to-buying-house",
        "https://www.ramseysolutions.com/real-estate/tips-for-first-time-home-buyers",
        #"https://realestate.usnews.com/real-estate/articles/how-to-buy-a-house",
        "https://www.hgtv.com/lifestyle/clean-and-organize/10-best-kept-secrets-for-buying-a-home",
        # tip to invest in residencial real estate
        "https://www.avail.co/education/articles/real-estate-investment-tips",
        "https://www.noradarealestate.com/blog/10-ways-successful-real-estate-investment/",
        "https://learn.roofstock.com/blog/real-estate-investing-tips-from-successful-investors",
        "https://www.nerdwallet.com/article/investing/5-ways-to-invest-in-real-estate",
        "https://www.investopedia.com/investing/simple-ways-invest-real-estate/",
        "https://time.com/personal-finance/article/how-to-invest-in-real-estate/",
        "https://www.linkedin.com/pulse/10-essential-tips-beginner-real-estate-investors-success-kris-de-leon/"
    ]

    # Open www.txt in append mode
    with open('www.txt', 'a', encoding='utf-8') as www_file:
        for url in websites:
            print(f"Extracting text from {url}")
            text = extract_text_from_website(url)
            if text:
                www_file.write(f"Text extracted from {url}:\n")
                www_file.write(text)
                www_file.write("\n" + "-" * 50 + "\n")

    print("All text extracted and saved to www.txt")

if __name__ == "__main__":
    main()
