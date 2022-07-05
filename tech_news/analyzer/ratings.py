# Requisito 10
from tech_news.database import db, get_collection


def top_5_news():
    top_noticias = db.news.find().sort("comments_count", -1).limit(5)
    list = []
    for item in top_noticias:
        list.append((item["title"], item["url"]))
    return list


# Requisito 11
def top_5_categories():
    top_noticias = get_collection().aggregate(
        [
            {"$group": {"_id": "$category", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 5},
        ]
    )
    return [item["_id"] for item in top_noticias]
