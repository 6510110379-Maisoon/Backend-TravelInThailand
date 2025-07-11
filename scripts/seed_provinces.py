from sqlalchemy.orm import Session
from flasx.database import SessionLocal
from flasx.models.province_model import Province

def seed_provinces(db: Session):
    provinces = [
    {"name": "Bangkok", "is_secondary": False, "tax_reduction": 10},
    {"name": "Chiang Mai", "is_secondary": True, "tax_reduction": 20},
    {"name": "Phuket", "is_secondary": True, "tax_reduction": 20},
    {"name": "Nakhon Ratchasima", "is_secondary": False, "tax_reduction": 10},
    ]
    for p in provinces:
        existing = db.query(Province).filter(Province.name == p["name"]).first()
        if not existing:
            province = Province(
                name=p["name"],
                is_secondary=p["is_secondary"],
                tax_reduction=p["tax_reduction"],
            )
            db.add(province)
    db.commit()

if __name__ == "__main__":
    db = SessionLocal()
    seed_provinces(db)
    print("Seed provinces completed")
