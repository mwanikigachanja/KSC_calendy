import streamlit as st
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Define SQLAlchemy base
Base = declarative_base()

# Define SQLAlchemy model for marketing strategy
class MarketingStrategy(Base):
    __tablename__ = 'marketing_strategies'

    id = Column(Integer, primary_key=True)
    date = Column(Date)
    strategy_details = Column(String)
    target_audience = Column(String)
    platform = Column(String)

# Create SQLite database and connect to it
engine = create_engine('sqlite:///marketing_strategies.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Function to input marketing strategy
def input_marketing_strategy():
    st.title('Input Marketing Strategy')
    st.write('Please fill in the details below to input your digital marketing strategy for the week.')

    # Input fields for strategy details
    date = st.date_input('Date', datetime.today())
    strategy_details = st.text_area('Strategy Details')
    target_audience = st.text_input('Target Audience')
    platform = st.selectbox('Platform', ['Facebook', 'Instagram', 'Twitter', 'LinkedIn', 'Other'])
    # Add any other relevant fields here

    # Button to submit the strategy
    if st.button('Submit Strategy'):
        # Save the strategy data to the database
        save_strategy(date, strategy_details, target_audience, platform)
        st.success('Strategy Submitted Successfully!')

# Function to save strategy data to the database
def save_strategy(date, strategy_details, target_audience, platform):
    session = Session()
    strategy = MarketingStrategy(date=date, strategy_details=strategy_details, target_audience=target_audience, platform=platform)
    session.add(strategy)
    session.commit()
    session.close()

# Main function to run the app
def main():
    input_marketing_strategy()

if __name__ == "__main__":
    main()
