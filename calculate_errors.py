

class NotEnclosedError(Exception):
	message = "A non-closed bracket is found"

class SignError(Exception):
	message = "Error in signs"

class FunctionError(Exception):
	message = "Invalid function"

class ValueFuncError(Exception):
	message = "Invalid function value"

class UnknownSignError(Exception):
	message = "The unknown sign is found"
		