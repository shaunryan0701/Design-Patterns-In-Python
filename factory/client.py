from chair_factory import ChairFactory

# The Client
chair_type = input("What type of chair do you want - (Small, Medium or Large)? ")
if chair_type == 'Small':
    CHAIR = ChairFactory.get_chair('SmallChair')
elif chair_type == 'Medium':
    CHAIR = ChairFactory.get_chair('MediumChair')
else:
    CHAIR = ChairFactory.get_chair('BigChair')

print(CHAIR.get_dimensions())