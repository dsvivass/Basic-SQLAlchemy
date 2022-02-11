from sqlalchemy import create_engine, Column, Integer, String, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///database:database', echo=False)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    grade = Column(String(50))
    
Base.metadata.create_all(engine) # create table

# WRITE TO DB

student1 = Student(name='Daniel', age=20, grade='A')
student2 = Student(name='Santiago', age=21, grade='B')
student3 = Student(name='Juan', age=22, grade='C')

session.add(student1)

session.add_all([student2, student3])
session.commit()

# GET FROM DB
    # Get all data
    
students = session.query(Student)

for student in students:
    print(student.name, student.age, student.grade)

    # Get data in order
studentsSorted = session\
    .query(Student)\
    .order_by(Student.name)

for student in studentsSorted:
    print(student.name, student.age, student.grade)
    
    # Get data by filtering
studentFiltered = session \
    .query(Student)\
    .filter(Student.name=='Juan')\
    .first()

print(studentFiltered.name, studentFiltered.age, studentFiltered.grade)

    # Get data by filtering multiple
studentFilteredMultiple = session \
    .query(Student)\
    .filter(or_(Student.name == "Juan", Student.name == "Daniel"))
    
for student in studentFilteredMultiple:
    print(f'Filtro multiple: {student.name}, {student.age}, {student.grade}')
    
    # Get count of results
studentFilteredMultipleCount = session \
    .query(Student)\
    .filter(or_(Student.name == "Juan", Student.name == "Daniel"))\
    .count()
    
print(f'Contador de filtro: {studentFilteredMultipleCount}')

# UPDATE

studentToUpdate = session\
    .query(Student)\
    .filter(Student.name == "Santiago")\
    .first()
    
student.name = 'Santiago modificado'
session.commit()

# DELETE 
studentToDelete = session\
    .query(Student)\
    .filter(Student.name == "Daniel")\
    .first()
    
session.delete(studentToDelete)
session.commit()
