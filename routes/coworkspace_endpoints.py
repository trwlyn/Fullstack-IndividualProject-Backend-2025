from fastapi import APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from models.feature import Feature
from models.pricing_plan import PricingPlan
from models.contact import Contact
from pydantic import EmailStr
from queries import feature_queries, pricing_queries, contact_queries
from decimal import Decimal

app = APIRouter(prefix="/api")

# Create CORS middleware to allow frontend to access the API
origins = [
    "http://localhost:5500",    # VS Code Live Server default
    "http://localhost:3000",    # Frontend development server
    "http://localhost:8000",    # Alternative local development port
    "http://127.0.0.1:5500",    # VS Code Live Server alternative
    "http://127.0.0.1:3000",    # Frontend alternative
    # Add your production domain when deploying
]

# GET endpoints for the features and pricing plans
@app.get("/features", response_model=List[Feature])
async def get_features():
    try:
        features_data = feature_queries.get_all_features()
        if features_data == "Connection Error":
            raise HTTPException(status_code=500, detail="Database connection error")
        
        features = []
        for feature_row in features_data:
            feature = Feature(
                id=feature_row[0],
                title=feature_row[1],
                description=feature_row[2],
                image_url=feature_row[3],
                is_active=feature_row[4]
            )
            features.append(feature)
        
        return features
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving features: {str(e)}")

@app.get("/pricing-plans", response_model=List[PricingPlan])
async def get_pricing_plans():
    try:
        pricing_data = pricing_queries.get_all_pricing_plans()
        if pricing_data == "Connection Error":
            raise HTTPException(status_code=500, detail="Database connection error")
        
        pricing_plans = []
        for plan_row in pricing_data:
            plan = PricingPlan(
                id=plan_row[0],
                name=plan_row[1],
                description=plan_row[2],
                price=Decimal(plan_row[3]),
                details=plan_row[4],
                is_popular=plan_row[5]
            )
            pricing_plans.append(plan)
        
        return pricing_plans
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error retrieving pricing plans: {str(e)}")

# POST endpoints for the contact form and newsletter subscription
@app.post("/contact", status_code=201)
async def submit_contact(contact: Contact):
    try:
        result = contact_queries.save_contact_message(
            contact.name, 
            contact.email, 
            contact.subject, 
            contact.message
        )
        
        if result == "Connection Error" or not result:
            raise HTTPException(status_code=500, detail="Failed to save contact message")
        
        return {"message": "Contact message received successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error submitting contact form: {str(e)}")

@app.post("/newsletter-subscribe", status_code=201)
async def subscribe_to_newsletter(email: EmailStr):
    try:
        result = contact_queries.save_newsletter_subscription(email)
        
        if result == "Connection Error" or not result:
            raise HTTPException(status_code=500, detail="Failed to subscribe to newsletter")
        
        return {"message": "Successfully subscribed to newsletter"}
    except Exception as e:
        if "duplicate key" in str(e).lower():
            return {"message": "You are already subscribed to our newsletter"}
        raise HTTPException(status_code=500, detail=f"Error subscribing to newsletter: {str(e)}")
