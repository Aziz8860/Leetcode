class Solution {
    void evaluate(stack<char>& optr, stack<char>& operand) {
        char op = optr.top(); // Get the operator at the top
        optr.pop(); // Remove the operator from the stack

        bool ans;

        if (op == '|') {
            ans = false; // for OR, initial value should be false
            while (operand.top() != '(') {
                ans = ans || (operand.top() == 't');
                operand.pop(); 
            }
            operand.pop(); // Pop the '(' from the stack
        }
        else if (op == '&') {
            ans = true; // for AND, initial value should be true
            while (operand.top() != '(') {
                ans = ans && (operand.top() == 't');
                operand.pop();
            }
            operand.pop(); // pop the '('
        }
        else if (op == '!') {
            ans = (operand.top() == 't');
            ans = !ans; // negate the value
            operand.pop(); // pop the value
            operand.pop(); // pop the '('
        }

        if (ans) operand.push('t'); // push true result back to the operand stack
        else operand.push('f'); // push false result back to the operand stack
}

public:
    bool parseBoolExpr(string expression) {
        stack<char> optr, operand;
        int idx = 0;

        while (expression[idx]) {
            if (expression[idx] == '!' || expression[idx] == '&' || expression[idx] == '|') {
                optr.push(expression[idx]);
            }
            else if (expression[idx] == 't' || expression[idx] == 'f') {
                operand.push(expression[idx]);
            }
            else if (expression[idx] == '(') {
                operand.push(expression[idx]);
            }
            else if (expression[idx] == ')') {
                evaluate(optr, operand); // evaluate when closing parenthesis is encountered
            }
            idx++;
        }

        return operand.top() == 't'; // Final result check
    }
};