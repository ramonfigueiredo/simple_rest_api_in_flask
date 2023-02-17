from application import db
db.create_all()

drink = Drink(name="Grape Soda", description="Taste like grapes")
db.session.add(drink)
db.session.commit()

db.session.add(Drink(name="Cherry Soda", description="Taste like cherry"))
db.session.commit()

db.session.commit()
