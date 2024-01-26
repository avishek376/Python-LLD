from UserRegisterImpl import *
from User import *


class Client:
    # create the register instance
    register = UserRegisterImpl()

    # create the prototype instance
    prototype = User(121, "Alok Batra", "alokbatra32@gmail.com", 9892656430)

    # add prototype instance to the registry
    register.add_prototype("employee", prototype)

    # create clone instance
    clone = register.clone("employee")
    clone.id = 22

    print(prototype.id, "|", clone.id)
    print(id(prototype), id(clone))
