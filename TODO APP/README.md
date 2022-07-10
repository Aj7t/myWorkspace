
## *features:*

Signup and Login
Add new TODO item
Get a list of all TODOs
Delete/Update a TODO item


##
class User(Base):
   __tablename__ = "users"
   id = Column(Integer, primary_key=True, index=True)
   lname = Column(String)
   fname = Column(String)
   email = Column(String, unique=True, index=True)
   todos = relationship("TODO", back_populates="owner", cascade="all, delete-orphan")
 
class TODO(Base):
   __tablename__ = "todos"
   id = Column(Integer, primary_key=True, index=True)
   text = Column(String, index=True)
   completed = Column(Boolean, default=False)
   owner_id = Column(Integer, ForeignKey("users.id"))
   owner = relationship("User", back_populates="todos")