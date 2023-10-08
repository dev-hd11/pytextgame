class ExitNotSetError(Exception) :
    def __str__() :
        return "Exit is set to true but exit is not created"

