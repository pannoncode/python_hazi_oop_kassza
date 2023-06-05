from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, String, Integer, Float
from sqlalchemy import create_engine


Base = declarative_base()


class StockDb(Base):
    __tablename__ = 'stock'
    __table_args__ = {'schema': 'stock_db'}
    id = Column(Integer, primary_key=True)
    product_name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


class StockHandler:

    def __init__(self, stock_list=list) -> None:
        self.stock_list = stock_list
        self.engine = create_engine(
            'postgresql://postgres:postgres@localhost:5432/postgres')
        self.Session = sessionmaker(self.engine)
        self.session = self.Session()

    def insert_data(self):
        new_stock = StockDb(
            product_name=self.stock_list["product_name"],
            price=self.stock_list["price"],
            quantity=self.stock_list["quantity"]
        )
        self.session.add(new_stock)
        self.session.commit()
        self.session.close()

    def update_stock(self, id):
        selected_product = self.session.query(StockDb).filter_by(id=id)

    def query_all_stock(self):
        stock = self.session.query(StockDb).all()
        return stock


if __name__ == "__main__":
    stock_all = StockHandler().query_all_stock()
    for item in stock_all:
        print(item.product_name)
        print(item.price)
        print(item.quantity)
