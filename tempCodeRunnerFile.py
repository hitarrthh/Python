
currency_details = {
    "USA": {
        "Currency": "US Dollar",
        "Code": "USD",
        "Symbol": "$"
    },
    "UK": {
        "Currency": "British Pound",
        "Code": "GBP",
        "Symbol": "£"
    },
    "Japan": {
        "Currency": "Japanese Yen",
        "Code": "JPY",
        "Symbol": "¥"
    },
    "India": {
        "Currency": "Indian Rupee",
        "Code": "INR",
        "Symbol": "₹"
    },
    "Australia": {
        "Currency": "Australian Dollar",
        "Code": "AUD",
        "Symbol": "A$"
    }
}


for country, details in currency_details.items():
    print(f"Currency Details for {country}:")
    print(f"Currency: {details['Currency']}")
    print(f"Currency Code: {details['Code']}")
    print(f"Currency Symbol: {details['Symbol']}")
    print()
