ad_campaigns = [
    {"campaign": "Summer Sale", "revenue": 50000, "cost": 10000},
    {"campaign": "Free Promo", "revenue": 2000, "cost": 0},
    {"campaign": "Winter Fest", "revenue": 100000, "cost": 25000},
    {"campaign": "Organic Social", "revenue": 15000, "cost": 0},
    {"campaign": "Email Blast", "revenue": 30000, "cost": 5000},
    {"campaign": "Word of Mouth", "revenue": 8000, "cost": 0},
    {"campaign": "Google Ads", "revenue": 75000, "cost": 20000},
    {"campaign": "Partnership", "revenue": 5000, "cost": 0}
]
total = 0
for campaign in ad_campaigns:
    try:
        roi = (campaign["revenue"] - campaign["cost"]) / campaign["cost"]
    except ZeroDivisionError:
        roi = 0
    print(f"{campaign['campaign']}, {roi}")
