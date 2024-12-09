class MathLib:

    @classmethod
    def execute(cls, mathRequest):
        """
        Execute the mathematical operation based on the MathRequest.

        :param mathRequest: An instance of MathRequest containing operands and operator.
        """
        operator = mathRequest.get_oper()
        operand1 = mathRequest.get_ope1()
        operand2 = mathRequest.get_ope2()

        match operator:
            case 'add':
                mathRequest.set_res(operand1 + operand2)

            case 'sub':
                mathRequest.set_res(operand1 - operand2)
            case 'mul':
                mathRequest.set_res(operand1 * operand2)
            case 'div':
                if operand2 == 0:
                    raise ValueError("Division by zero is not allowed.")
                mathRequest.set_res(operand1 / operand2)
            case 'pow':
                mathRequest.set_res(operand1 ** operand2)
