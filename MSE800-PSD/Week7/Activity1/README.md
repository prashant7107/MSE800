# Analysis of the Sample Code
## Classes and Subclasses
The code utilizes both abstract base classes (interfaces) and their subclasses to establish.
* Factory : Base Abstract class. 
* AnimalFactory, DogFactory, CatFactory - Subclasses of Factory. They implement specific logic for creating own products.
* Animal : Base Abstract class. 
Doc, Car: Subclasses of Factory

## Outcome:
* factory = DogFactory()
A DogFactory instance is created.
* dog = Dog()
A Dog instance is created directly 
* dog = factory.create_product()
factory.create_product() is called on the DogFactory
* dog.run()
dog.run() is invoked.

### Expected outccome
I'm a Dog, I can run!!
### Actual outcome
AttributeError: 'NoneType' object has no attribute 'run'

### Get expected outcome
Not getting the expected outcome because there is no return. FIX!

class DogFactory(Factory):
    def create_product(self, kind=None):
        return Dog()

add return Dog() instead of pass.